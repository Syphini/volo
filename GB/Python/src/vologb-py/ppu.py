import pygame
import helpers

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mmu import MMU


class PPU:
    def __init__(self, mmu: "MMU") -> None:
        self.mmu = mmu

        self.LCDC = Control_Bits(0x91)  # FF40
        self.STAT = Control_Bits(0x85)  # FF41
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
    def DMA(self) -> int:
        return 0x0

    @DMA.setter
    def DMA(self, value: int) -> None:
        for i in range(0xA0):
            source_mem = self.mmu.get_memory(value << 8 | i)
            self.mmu.set_memory(0xFE00 + i, source_mem)

    def init_pygame(self) -> None:
        self.PIXEL_SIZE = 3
        self.TILE_SIZE = 1
        # 160 x 144 screen size
        # 256 x 256 tilemap
        self.SCREEN_X = 160
        self.SCREEN_Y = 144
        self.CANVAS_SIZE = (
            self.SCREEN_X * self.PIXEL_SIZE,
            self.SCREEN_Y * self.PIXEL_SIZE,
        )

        pygame.init()
        self.CYCLE_COUNTER = 0

        self.CANVAS = pygame.display.set_mode(self.CANVAS_SIZE)
        pygame.display.set_caption("FPS: 0")

        self.clear_display()
        pygame.display.flip()

    def dump(self) -> bytearray:
        return bytearray(
            [
                self.LCDC.get(),
                self.STAT.get(),
                self.SCY,
                self.SCX,
                self._LY,
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
                return self._LY
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
                raise Exception("Unknown IO Register:", helpers.formatted_hex(addr))

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
                raise Exception("Unknown IO Register:", helpers.formatted_hex(addr))

    # Tilemap 1 9800 -> 9BFF
    # Tilemap 2 9C00 -> 9FFF

    def tick(self, cycles: int) -> None:
        if self.LCDC.BIT_7 == 1:
            for _ in range(cycles):

                if self.LYC == self._LY:
                    self.STAT.BIT_2 = 1
                    if self.STAT.BIT_6 == 1:
                        self.mmu.IO.IF.LCD = 1

                self.STAT.BIT_0 = self._MODE & 1
                self.STAT.BIT_1 = (self._MODE & 2) >> 1

                match self._MODE:
                    case 2:  # OAM
                        if self._CLOCK == 80:
                            self._MODE = 3
                            self._CLOCK = 0
                    case 3:  # Pixel
                        if self._CLOCK == 172:
                            self._MODE = 0
                            self._CLOCK = 0

                            self.drawline()
                            self.draw_oam_line()
                    case 0:  # H-Blank
                        if self._CLOCK == 204:
                            self._LY += 1

                            if self._LY == 143:
                                self.mmu.IO.IF.VBLANK = 1
                                self._MODE = 1
                            else:
                                self._MODE = 2
                            self._CLOCK = 0
                    case 1:  # V-Blank
                        if self._CLOCK == 456:
                            self._LY += 1
                            self._CLOCK = 0

                            if self._LY > 153:
                                self._MODE = 2
                                self._LY = 0
                                pygame.display.flip()
                self._CLOCK += 1
        else:
            self._LY = 0
            self._CLOCK = 0
            self.clear_display()

    def get_tile_colours(
        self, tile_bytes: bytearray, tileY: int, attributes: int = 0
    ) -> list[int]:
        """Convert byte data into tile data"""

        # priority = 0
        yFlip = 0
        xFlip = 0

        tileY *= 2

        if attributes:
            # priority = attributes >> 7 & 1
            yFlip = attributes >> 6 & 1
            xFlip = attributes >> 5 & 1

        return [
            (
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
            for i in range(8)
        ]

    def draw_oam_line(self) -> None:
        line = self._LY

        sprite_height = 8
        sprite_count = 0
        sprites_list = []

        # find sprites on this line
        for i in range(0, 0xA0, 4):
            y = self.mmu.OAM[i] - 16

            if y <= line < y + sprite_height:
                sprites_list.append(i)
                sprite_count += 1
                if sprite_count == 10:
                    break

        # render the sprites onto the line
        for i in range(sprite_count):
            spriteIndex = sprites_list[i]
            y = self.mmu.OAM[spriteIndex] - 16
            x = self.mmu.OAM[spriteIndex + 1] - 8
            tileIndex = self.mmu.OAM[spriteIndex + 2] * 16
            attributes = self.mmu.OAM[spriteIndex + 3]

            tile = self.mmu.VRAM[tileIndex : tileIndex + 16]
            colours = self.get_tile_colours(tile, line % 8, attributes)

            for lineX in range(8):
                self.draw_pixel(x + lineX, line, colours[lineX], True)

    def draw_pixel(
        self,
        x: int,
        y: int,
        colourId: int,
        transparent: bool = False,
    ) -> None:
        """Draw pixel at (x,y)"""
        if transparent and colourId == 0:
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

    def drawline(self) -> None:
        """Draw the current scanline"""
        # TODO make faster
        # aim: 40ms
        # per 20 cycles @ 10000 ticks
        y = self._LY
        scrollY = (y + self.SCY) & 0xFF

        for x in range(0, self.SCREEN_X, 8):
            use_alt_block = self.LCDC.BIT_4 == 1
            use_alt_tilemap = self.LCDC.BIT_3 == 1

            vramTileBlock = 0x0000 if use_alt_block else 0x1000
            tileMap = 0x1C00 if use_alt_tilemap else 0x1800

            tileIndex = self.mmu.VRAM[tileMap + ((scrollY // 8) * 32) + (x // 8)]
            offset = (
                tileIndex if use_alt_block == 1 else (tileIndex ^ 0x80) - 0x80
            ) * 16
            tile = self.mmu.VRAM[vramTileBlock + offset : vramTileBlock + offset + 16]
            colours = self.get_tile_colours(tile, scrollY % 8)

            for xi in range(8):
                scrollX = (x + xi - self.SCX) & 0xFF
                self.draw_pixel(scrollX, y, colours[xi])

    def clear_display(self) -> None:
        """Clear the canvas"""
        self.CANVAS.fill(
            (255, 255, 255), pygame.Rect(0, 0, self.CANVAS_SIZE[0], self.CANVAS_SIZE[1])
        )


class Control_Bits:
    def __init__(self, value: int) -> None:
        self.set(value)

    def set(self, value: int) -> None:
        self.BIT_7 = value >> 7 & 1
        self.BIT_6 = value >> 6 & 1
        self.BIT_5 = value >> 5 & 1
        self.BIT_4 = value >> 4 & 1
        self.BIT_3 = value >> 3 & 1
        self.BIT_2 = value >> 2 & 1
        self.BIT_1 = value >> 1 & 1
        self.BIT_0 = value & 1

    def get(self) -> int:
        return (
            self.BIT_7 << 7
            | self.BIT_6 << 6
            | self.BIT_5 << 5
            | self.BIT_4 << 4
            | self.BIT_3 << 3
            | self.BIT_2 << 2
            | self.BIT_1 << 1
            | self.BIT_0
        )
