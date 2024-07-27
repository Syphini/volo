import time
import pygame
import helpers


class PPU:
    def __init__(self, mmu):
        self.mmu = mmu

        self.LCDC = Control_Bits(0x91)  # FF40
        self.STAT = 0x85  # FF41
        self.SCY = 0x00  # FF42
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

        self._OAM_OFFSET = 0xFE00

        self._DEBUG_TIME = time.time() * 1000

        self.PALETTE = [
            (255, 246, 211),
            (249, 168, 117),
            (235, 107, 111),
            (124, 63, 88),
        ]

        self.init_pygame()

    @property
    def DMA(self):
        return 0x0

    @DMA.setter
    def DMA(self, value):
        for i in range(0xA0):
            source_mem = self.mmu.get_memory(value << 8 | i)
            self.mmu.set_memory(0xFE00 + i, source_mem)

    def init_pygame(self):
        self.PIXEL_SIZE = 2
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

        self.canvas = pygame.display.set_mode(self.CANVAS_SIZE)
        pygame.display.set_caption("GB Test")

        self.clear_display()
        pygame.display.flip()

    def dump(self):
        return bytearray(
            [
                self.LCDC.get(),
                self.STAT,
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

    def get(self, addr):
        match addr:
            case 0xFF40:
                return self.LCDC.get()
            case 0xFF41:
                return self.STAT
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

    def set(self, addr, value):
        match addr:
            case 0xFF40:
                self.LCDC.set(value)
            case 0xFF41:
                self.STAT = value
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

    def tick(self, cycles: int):
        if self.LCDC.BIT_7 == 1:
            for _ in range(cycles):
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
                            pygame.display.flip()
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

                                # region DEBUG
                                newTime = time.time() * 1000
                                print("Frame Drawn:", newTime - self._DEBUG_TIME)
                                self._DEBUG_TIME = newTime
                                # endregion
                self._CLOCK += 1
        else:
            self._CLOCK = 0
            self.clear_display()

    def get_tile_colour(
        self, tile_bytes: bytearray, tileX, tileY, attributes: int = None
    ):
        """Convert byte data into tile data"""
        if len(tile_bytes) < 16:
            raise Exception("Invalid Tile Data")

        # priority = 0
        yFlip = 0
        xFlip = 0

        tileY *= 2

        if attributes:
            # priority = attributes >> 7 & 1
            yFlip = attributes >> 6 & 1
            xFlip = attributes >> 5 & 1

        B1 = (
            tile_bytes[15 - tileY if yFlip else tileY]
            >> (tileX if xFlip else (7 - tileX))
            & 1
        )
        B2 = (
            tile_bytes[15 - (tileY + 1) if yFlip else (tileY + 1)]
            >> (tileX if xFlip else (7 - tileX))
            & 1
        )

        return B2 << 1 | B1

    def get_bg_tile(self, x, y):
        """Get tile given current pixel X & Y"""
        use_alt_block = self.LCDC.BIT_4 == 1
        use_alt_tilemap = self.LCDC.BIT_3 == 1

        vramTileBlock = 0x0000 if use_alt_block else 0x1000
        tileMap = 0x9C00 if use_alt_tilemap else 0x9800

        tileIndex = self.mmu.get_memory(tileMap + ((y // 8) * 32) + (x // 8))
        offset = (
            tileIndex if use_alt_block == 1 else helpers.signed_value(tileIndex)
        ) * 16
        # TODO change this to get_memory
        return self.mmu.VRAM[vramTileBlock + offset : vramTileBlock + offset + 16]

    def draw_oam_line(self):
        line = helpers.wrap_8bit(self._LY + self.SCY)

        sprite_height = 8
        sprite_count = 0
        sprites_list = []

        # find sprites on this line
        for i in range(0, 0xA0, 4):
            y = self.mmu.get_memory(self._OAM_OFFSET + i) - 16

            if y <= line < y + sprite_height:
                sprites_list.append(i)
                sprite_count += 1
                if sprite_count == 10:
                    break

        # render the sprites onto the line
        for i in range(sprite_count):
            spriteIndex = sprites_list[i]
            y = self.mmu.get_memory(self._OAM_OFFSET + spriteIndex) - 16
            x = self.mmu.get_memory(self._OAM_OFFSET + spriteIndex + 1) - 8
            tileIndex = self.mmu.get_memory(self._OAM_OFFSET + spriteIndex + 2) * 16
            attributes = self.mmu.get_memory(self._OAM_OFFSET + spriteIndex + 3)

            tile = self.mmu.VRAM[tileIndex : tileIndex + 16]

            for lineX in range(8):
                colour = self.get_tile_colour(tile, lineX, line % 8, attributes)
                self.draw_pixel(x + lineX, line, colour, True)

    def draw_pixel(self, x, y, colourId, transparent=False):
        """Draw pixel at (x,y)"""
        if transparent and colourId == 0:
            return

        self.canvas.fill(
            self.PALETTE[colourId],
            pygame.Rect(
                x * self.PIXEL_SIZE,
                y * self.PIXEL_SIZE,
                self.PIXEL_SIZE,
                self.PIXEL_SIZE,
            ),
        )

    def drawline(self):
        """Draw the current scanline"""
        # TODO make faster
        # aim:(<40ms/24fps) current:(~70ms/14fps)
        y = self._LY
        scrollY = helpers.wrap_8bit(y + self.SCY)

        for x in range(self.SCREEN_X):
            tile = self.get_bg_tile(helpers.wrap_8bit(x + self.SCX), scrollY)  # ~10ms
            colour = self.get_tile_colour(tile, x % 8, y % 8)  # ~5ms
            self.draw_pixel(x, y, colour)  # ~20ms

    def clear_display(self):
        """Clear the canvas"""
        self.canvas.fill(
            (255, 255, 255), pygame.Rect(0, 0, self.CANVAS_SIZE[0], self.CANVAS_SIZE[1])
        )


class Control_Bits:
    def __init__(self, value):
        self.set(value)

    def set(self, value):
        self.BIT_7 = value >> 7 & 1
        self.BIT_6 = value >> 6 & 1
        self.BIT_5 = value >> 5 & 1
        self.BIT_4 = value >> 4 & 1
        self.BIT_3 = value >> 3 & 1
        self.BIT_2 = value >> 2 & 1
        self.BIT_1 = value >> 1 & 1
        self.BIT_0 = value & 1

    def get(self):
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
