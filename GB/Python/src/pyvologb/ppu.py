import pygame
from pyvologb.helpers import formatted_hex

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyvologb.mmu import MMU


class PPU:
    def __init__(self, mmu: "MMU", debugging=False) -> None:
        self.mmu = mmu
        self.DEBUGGING_MODE = False  # debugging

        self.LCDC = LCDC(0x91)  # FF40
        self.STAT = STAT(0x85)  # FF41
        self.SCY = 0x00  # FF42F
        self.SCX = 0x00  # FF43
        self._LY = 0x00  # FF44 -- read-only
        self.LYC = 0x00  # FF45
        # DMA  # FF46
        self.BGP = 0xFC  # FF47
        self.OBP0 = 0x00  # FF48
        self.OBP1 = 0x00  # FF49
        self.WY = 0x00  # FF4A
        self.WX = 0x00  # FF4B

        self._MODE = 2
        self._LX = 0x0
        self._CLOCK = 0

        self.PALETTE = [
            (255, 246, 211),
            (249, 168, 117),
            (235, 107, 111),
            (124, 63, 88),
        ]

        self.init_pygame()

    @property
    def PPU_MODE(self) -> int:
        return self._MODE

    @PPU_MODE.setter
    def PPU_MODE(self, value: int) -> None:
        self._MODE = value
        self.STAT.set_mode(value)
        match value:
            case 0:
                if self.STAT.MODE_0_SELECT:
                    self.mmu.IO.IF.LCD = 1
            case 1:
                if self.STAT.MODE_1_SELECT:
                    self.mmu.IO.IF.LCD = 1
            case 2:
                if self.STAT.MODE_2_SELECT:
                    self.mmu.IO.IF.LCD = 1

    @property
    def DMA(self) -> int:
        return 0x0

    @DMA.setter
    def DMA(self, value: int) -> None:
        for i in range(0xA0):
            source_mem = self.mmu.get_memory(value << 8 | i)
            self.mmu.set_memory(0xFE00 + i, source_mem)

    @property
    def LY(self) -> int:
        return self._LY

    @LY.setter
    def LY(self, value) -> None:
        self._LY = value
        self.check_lyc()

    def init_pygame(self) -> None:
        pygame.init()
        self.CYCLE_COUNTER = 0

        self.PIXEL_SIZE = 3
        self.TILE_SIZE = 1

        # 160 x 144 screen size
        self.SCREEN_X = 160
        self.SCREEN_Y = 144

        self.CANVAS_SIZE = (
            self.SCREEN_X * self.PIXEL_SIZE,
            self.SCREEN_Y * self.PIXEL_SIZE,
        )

        if self.DEBUGGING_MODE:
            self.PIXEL_SIZE = 2
            # 2 (256 x 256) tilemaps
            # Tilemap 1 9800 -> 9BFF
            # Tilemap 2 9C00 -> 9FFF
            self.DEBUG_SCREEN_X = 256 * 2
            self.DEBUG_SCREEN_Y = 256
            self.DEBUG_CANVAS_SIZE = (
                (self.SCREEN_X + self.DEBUG_SCREEN_X) * self.PIXEL_SIZE,
                self.DEBUG_SCREEN_Y * self.PIXEL_SIZE,
            )
            self.CANVAS = pygame.display.set_mode(self.DEBUG_CANVAS_SIZE)
        else:
            self.CANVAS = pygame.display.set_mode(self.CANVAS_SIZE)

        pygame.display.set_caption("PY-VOLO GB")

        self.clear_display()
        pygame.display.flip()

    def debug(self) -> None:
        offset_x = self.SCREEN_X
        offset_y = 0

        vram_block = 0x1000

        for y in range(256):
            yPos = offset_y + y
            for z in range(2):
                bg_tilemap = 0x1C00 if z == 1 else 0x1800
                for x in range(0, 256, 8):
                    xPos = offset_x + x + (256 * z)
                    bg_tile_index = self.mmu.VRAM[
                        bg_tilemap + ((y // 8) * 32) + ((x & 0xFF) // 8)
                    ]
                    bg_vram_block_offset = ((bg_tile_index ^ 0x80) - 0x80) * 16
                    bg_tile = self.mmu.VRAM[
                        vram_block
                        + bg_vram_block_offset : vram_block
                        + bg_vram_block_offset
                        + 16
                    ]
                    bg_colours = self.get_tile_colours(bg_tile, yPos % 8)

                    for xi in range(8):
                        self.draw_pixel(xPos + xi, yPos, bg_colours[xi])

    def dump(self) -> bytearray:
        return bytearray(
            [
                self.LCDC.get(),
                self.STAT.get(),
                self.SCY,
                self.SCX,
                self.LY,
                self.LYC,
                self.DMA,
                self.BGP,
                self.OBP0,
                self.OBP1,
                self.WY,
                self.WX,
            ]
        )

    def get(self, addr: int) -> int:
        match addr:
            case 0xFF40:
                return self.LCDC.get()
            case 0xFF41:
                return self.STAT.get()
            case 0xFF42:
                return self.SCY
            case 0xFF43:
                return self.SCX
            case 0xFF44:
                return self.LY
            case 0xFF45:
                return self.LYC
            case 0xFF46:
                return self.DMA
            case 0xFF47:
                return self.BGP
            case 0xFF48:
                return self.OBP0
            case 0xFF49:
                return self.OBP1
            case 0xFF4A:
                return self.WY
            case 0xFF4B:
                return self.WX
            case _:
                raise Exception("Unknown IO Register:", formatted_hex(addr))

    def set(self, addr: int, value: int) -> None:
        match addr:
            case 0xFF40:
                self.LCDC.set(value)
            case 0xFF41:
                self.STAT.set(value)
            case 0xFF42:
                self.SCY = value
            case 0xFF43:
                self.SCX = value
            case 0xFF44:
                pass  # readonly
            case 0xFF45:
                self.LYC = value
            case 0xFF46:
                self.DMA = value
            case 0xFF47:
                self.BGP = value
            case 0xFF48:
                self.OBP0 = value
            case 0xFF49:
                self.OBP1 = value
            case 0xFF4A:
                self.WY = value
            case 0xFF4B:
                self.WX = value
            case _:
                raise Exception("Unknown IO Register:", formatted_hex(addr))

    def tick(self, cycles: int) -> None:
        if self.LCDC.LCD_ENABLE == 1:
            for _ in range(cycles):

                match self.PPU_MODE:
                    case 2:  # OAM
                        if self._CLOCK == 80:
                            self.PPU_MODE = 3
                            self._CLOCK = 0
                    case 3:  # Pixel
                        if self._CLOCK == 172:
                            self.PPU_MODE = 0
                            self._CLOCK = 0

                            self.drawline()
                            if self.LCDC.OBJ_ENABLE == 1:
                                self.draw_oam_line()
                    case 0:  # H-Blank
                        if self._CLOCK == 204:
                            self.LY += 1

                            if self.LY == 143:
                                self.mmu.IO.IF.VBLANK = 1
                                self.PPU_MODE = 1
                            else:
                                self.PPU_MODE = 2
                            self._CLOCK = 0
                    case 1:  # V-Blank
                        if self._CLOCK == 456:
                            self.LY += 1
                            self._CLOCK = 0

                            if self.LY > 153:
                                self.PPU_MODE = 2
                                self.LY = 0

                                # update screen
                                pygame.display.flip()
                self._CLOCK += 1
        else:
            self.LY = 0
            self.STAT.set_lyc_equal(0)
            self._CLOCK = 0
            self.STAT.set_mode(0)
            self.clear_display()

    def check_lyc(self):
        if self.LYC == self.LY:
            self.STAT.set_lyc_equal(1)
            if self.STAT.LYC_SELECT == 1:
                self.mmu.IO.IF.LCD = 1
        else:
            self.STAT.set_lyc_equal(0)

    def draw_pixel(
        self,
        x: int,
        y: int,
        colourId: int | None,
    ) -> None:
        """Draw pixel at (x,y)"""
        if colourId is None:
            return

        pygame.draw.rect(
            self.CANVAS,
            self.PALETTE[colourId],
            [
                x * self.PIXEL_SIZE,
                y * self.PIXEL_SIZE,
                self.PIXEL_SIZE,
                self.PIXEL_SIZE,
            ],
        )

    def get_tile_colours(
        self, tile_bytes: bytearray, tileY: int, attributes: int | None = None
    ) -> list[int | None]:
        """Convert byte data into tile data"""

        # priority = 0
        yFlip = 0
        xFlip = 0
        palette = self.BGP
        transparent: int | None = None

        tileY *= 2

        if attributes is not None:
            # priority = attributes >> 7 & 1
            yFlip = attributes >> 6 & 1
            xFlip = attributes >> 5 & 1
            palette = self.OBP1 if attributes >> 4 & 1 == 1 else self.OBP0
            transparent = palette & 3

        return [
            None if transparent == c else c
            for c in [
                palette
                >> (
                    (
                        (
                            tile_bytes[15 - (tileY + 1) if yFlip else (tileY + 1)]
                            >> (i if xFlip else (7 - i))
                            & 1
                        )
                        << 1
                    )
                    | (
                        tile_bytes[15 - tileY if yFlip else tileY]
                        >> (i if xFlip else (7 - i))
                        & 1
                    )
                )
                * 2
                & 3
                for i in range(8)
            ]
        ]

    def drawline(self) -> None:
        """Draw the current scanline"""
        y = self.LY
        scrollY = (y + self.SCY) & 0xFF

        # attempting to reduce the number of tile calcs by stepping 8 pixels at a time
        # performance drop at max SCX is negligable compared to recalculating tiles per pixel
        # i'm sure there's a better way to do this but here we are
        if self.LCDC.BG_WIN_ENABLE == 1:
            for x in range(0, self.SCREEN_X + self.SCX, 8):
                use_alt_vram_block = self.LCDC.ALT_BG_WIN_TILES == 1

                vram_block = 0x0000 if use_alt_vram_block else 0x1000
                bg_tilemap = 0x1C00 if self.LCDC.ALT_BG_TILEMAP == 1 else 0x1800
                win_tilemap = 0x1C00 if self.LCDC.ALT_WIN_TILEMAP == 1 else 0x1800

                # BG
                bg_tile_index = self.mmu.VRAM[
                    bg_tilemap + ((scrollY // 8) * 32) + ((x & 0xFF) // 8)
                ]
                bg_vram_block_offset = (
                    bg_tile_index
                    if use_alt_vram_block == 1
                    else (bg_tile_index ^ 0x80) - 0x80
                ) * 16
                bg_tile = self.mmu.VRAM[
                    vram_block
                    + bg_vram_block_offset : vram_block
                    + bg_vram_block_offset
                    + 16
                ]
                bg_colours = self.get_tile_colours(bg_tile, scrollY % 8)

                # WIN
                if self.LCDC.WIN_ENABLE == 1:
                    win_tile_index = self.mmu.VRAM[
                        win_tilemap + ((y // 8) * 32) + ((x & 0xFF) // 8)
                    ]
                    win_vram_block_offset = (
                        win_tile_index
                        if use_alt_vram_block == 1
                        else (win_tile_index ^ 0x80) - 0x80
                    ) * 16
                    win_tile = self.mmu.VRAM[
                        vram_block
                        + win_vram_block_offset : vram_block
                        + win_vram_block_offset
                        + 16
                    ]

                    win_colours = self.get_tile_colours(win_tile, y % 8)

                # reducing draw calls by discarding pixels offscreen
                for xi in range(8):
                    if self.LCDC.WIN_ENABLE == 1:
                        pixelX = x + xi
                        if 0 <= pixelX < self.SCREEN_X:
                            self.draw_pixel(pixelX, y, win_colours[xi])
                    else:
                        pixelX = (x + xi) - self.SCX
                        if 0 <= pixelX < self.SCREEN_X:
                            self.draw_pixel(pixelX, y, bg_colours[xi])
        else:
            for x in range(self.SCREEN_X):
                self.draw_pixel(x, y, 0)

    def draw_oam_line(self) -> None:
        line = self.LY

        tall_tile = bool(self.LCDC.OBJ_SIZE)

        sprite_height = 16 if tall_tile else 8
        sprite_count = 0
        sprites_list = []

        # find sprites on this line
        for i in range(0, 0xA0, 4):
            yPos = self.mmu.OAM[i] - 16

            if yPos <= line < yPos + sprite_height:
                sprites_list.append(i)
                sprite_count += 1
                if sprite_count == 10:
                    break

        # render the sprites onto the line
        for i in range(sprite_count):
            spriteIndex = sprites_list[i]
            yPos = self.mmu.OAM[spriteIndex] - 16
            xPos = self.mmu.OAM[spriteIndex + 1] - 8
            tileIndex = self.mmu.OAM[spriteIndex + 2]
            attributes = self.mmu.OAM[spriteIndex + 3]

            if tall_tile and (line % 16 < 8):
                tileIndex &= 0xFE
            elif tall_tile:
                tileIndex |= 0x01

            tile = self.mmu.VRAM[tileIndex * 16 : (tileIndex * 16) + 16]
            colours = self.get_tile_colours(tile, (line - yPos) % 8, attributes)

            for lineX in range(8):
                xPixel = xPos + lineX
                if 0 <= xPixel < self.SCREEN_X and 0 <= line < self.SCREEN_Y:
                    self.draw_pixel(xPixel, line, colours[lineX])

    def clear_display(self) -> None:
        """Clear the canvas"""
        self.CANVAS.fill(
            (255, 255, 255), pygame.Rect(0, 0, self.CANVAS_SIZE[0], self.CANVAS_SIZE[1])
        )


class LCDC:
    def __init__(self, value: int) -> None:
        self.set(value)

    def set(self, value: int) -> None:
        self.LCD_ENABLE = value >> 7 & 1
        self.ALT_WIN_TILEMAP = value >> 6 & 1
        self.WIN_ENABLE = value >> 5 & 1
        self.ALT_BG_WIN_TILES = value >> 4 & 1
        self.ALT_BG_TILEMAP = value >> 3 & 1
        self.OBJ_SIZE = value >> 2 & 1
        self.OBJ_ENABLE = value >> 1 & 1
        self.BG_WIN_ENABLE = value & 1

    def get(self) -> int:
        return (
            self.LCD_ENABLE << 7
            | self.ALT_WIN_TILEMAP << 6
            | self.WIN_ENABLE << 5
            | self.ALT_BG_WIN_TILES << 4
            | self.ALT_BG_TILEMAP << 3
            | self.OBJ_SIZE << 2
            | self.OBJ_ENABLE << 1
            | self.BG_WIN_ENABLE
        )


class STAT:
    def __init__(self, value: int) -> None:
        self.LYC_EQUAL = 0
        self.PPU_MODE = 0
        self.set(value)

    def set(self, value: int) -> None:
        self.LYC_SELECT = value >> 6 & 1
        self.MODE_2_SELECT = value >> 5 & 1
        self.MODE_1_SELECT = value >> 4 & 1
        self.MODE_0_SELECT = value >> 3 & 1

    def get(self) -> int:
        return (
            1 << 7
            | self.LYC_SELECT << 6
            | self.MODE_2_SELECT << 5
            | self.MODE_1_SELECT << 4
            | self.MODE_0_SELECT << 3
            | self.LYC_EQUAL << 2
            | (self.PPU_MODE >> 1) << 1
            | self.PPU_MODE & 1
        )

    def set_mode(self, value: int) -> None:
        self.PPU_MODE = value & 3

    def set_lyc_equal(self, value: int) -> None:
        self.LYC_EQUAL = value & 1
