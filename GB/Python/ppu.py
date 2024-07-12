import sys
import pygame


class PPU:
    def __init__(self, mmu):
        self.mmu = mmu

        self.LCDC = 0x91  # FF40
        self.STAT = 0x85  # FF41
        self.SCY = 0x00  # FF42
        self.SCX = 0x00  # FF43
        self._LY = 0x00  # FF44 -- read-only
        self.LYC = 0x00  # FF45
        self.DMA = 0x00  # FF46
        self.BGP = 0xFC  # FF47
        self.OBP0 = 0x00  # FF48
        self.OBP1 = 0x00  # FF49
        self.WY = 0x00  # FF4A
        self.WX = 0x00  # FF4B

        self._MODE = 2
        self._LX = 0x0
        self._TILEMAP = 0x9800
        self._CLOCK = 0

        self.PALETTE = [
            (255, 246, 211),
            (249, 168, 117),
            (235, 107, 111),
            (124, 63, 88),
        ]

        self.init_pygame()

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

    def get(self, addr):
        match addr:
            case 0xFF40:
                return self.LCDC
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
                raise Exception("Unknown IO Register:", addr)

    def set(self, addr, value):
        match addr:
            case 0xFF40:
                self.LCDC = value
            case 0xFF41:
                self.STAT = value
            case 0xFF42:
                self.SCY = value
            case 0xFF43:
                self.SCX = value
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
                raise Exception("Unknown IO Register:", addr)

    # Tilemap 1 9800 -> 9BFF
    # Tilemap 2 9C00 -> 9FFF

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.mmu.dump()
                pygame.quit()
                sys.exit()

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
            case 0:  # H-Blank
                if self._CLOCK == 204:
                    self._LY += 1

                    if self._LY == 143:
                        self._MODE = 1
                    else:
                        self._MODE = 2
                    self._CLOCK = 0
            case 1:  # V-Blank
                if self._CLOCK == 456:
                    self._LY += 1

                    if self._LY > 153:
                        self._MODE = 2
                        self._LY = 0
                    self._CLOCK = 0

        self._CLOCK += 1

    def tile_to_colours(self, tile_bytes: bytearray):
        """Convert byte data into tile data"""
        data = []
        if len(tile_bytes) < 16:
            raise Exception("Invalid Tile Data")

        for c in range(len(tile_bytes) - 1):
            if c % 2 == 1:
                continue

            BYTE_1 = tile_bytes[c]
            BYTE_2 = tile_bytes[c + 1]

            colours = []
            for i in range(8):
                b1 = bin(BYTE_1)[2:].zfill(8)
                b2 = bin(BYTE_2)[2:].zfill(8)
                calc = b2[i] + b1[i]
                colours.append(int(calc, 2))

            data.append(colours)
        return data

    def get_tile(self, x, y):
        """Get tile given current pixel X & Y"""
        tileBlock = 0x0

        offsetX = x  # TODO scx
        offsetY = y  # TODO scy

        tileIndex = self.mmu.get_memory(
            self._TILEMAP + ((offsetY // 8) * 32) + (offsetX // 8)
        )
        offset = tileIndex * 16
        return self.mmu.VRAM[tileBlock + offset : tileBlock + offset + 16]

    def drawline(self):
        """Draw the current scanline"""
        y = self._LY

        for x in range(self.SCREEN_X):
            print("drawing:", x, y)
            tileData = self.tile_to_colours(self.get_tile(x, y))

    def clear_display(self):
        """Clear the canvas"""
        self.canvas.fill(
            self.PALETTE[0], pygame.Rect(0, 0, self.CANVAS_SIZE[0], self.CANVAS_SIZE[1])
        )
