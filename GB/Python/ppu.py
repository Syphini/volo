class PPU:
    def __init__(self):
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
        self._FRAMETICK = 0

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
        match self._MODE:
            case 2:  # OAM
                if self._FRAMETICK == 40:
                    self._LX = 0

                    self._MODE = 3
            case 3:  # Pixel

                # Pixel Fetcher

                self._LX += 1
                if self._LX == 160:
                    self._MODE = 0
            case 0:  # H-Blank
                if self._FRAMETICK == 456:
                    self._FRAMETICK = 0
                    self._LY += 1
                    if self._LY == 144:
                        self._MODE = 1
                    else:
                        self._MODE = 2
            case 1:  # V-Blank
                if self._FRAMETICK == 456:
                    self._FRAMETICK = 0
                    self._LY += 1
                    if self._LY == 153:
                        self._LY = 0
                        self._MODE = 2

        self._FRAMETICK += 1
