import time
import random
import sys
import pygame

# ROM path
ROM = 'Chip-8/ROM/morse_demo.ch8'

# Initialize starting bytes
PC = 0x200
RAM = bytearray(4096)
V = bytearray(16)
I = 0x000
STACK = []
KEYS = bytearray(16)

# Timers
delay_timer = 0
sound_timer = 0

pygame.init()

# Variables
PIXEL_SIZE = 8
CANVAS_SIZE = (64 * PIXEL_SIZE, 32 * PIXEL_SIZE)

# Pixel States
ON = (255, 255, 255)
OFF = (0, 0, 0)

# Canvas
canvas = pygame.display.set_mode(CANVAS_SIZE)
pygame.display.set_caption("Chip-8")


def update_display():
    """Update the display to render the current canvas"""
    pygame.display.update()


def get_pixel(x_y):
    """True or False if pixel at x_y is ON or OFF"""
    x = x_y[0] * PIXEL_SIZE
    y = x_y[1] * PIXEL_SIZE

    return canvas.get_at((x, y)) == ON


def draw(x_y, on=True):
    """Draw a pixel to the canvas"""
    x = x_y[0] * PIXEL_SIZE
    y = x_y[1] * PIXEL_SIZE

    canvas.fill(ON if on else OFF, pygame.Rect(x, y, PIXEL_SIZE, PIXEL_SIZE))


def clear():
    """Clear the canvas"""
    canvas.fill(OFF, pygame.Rect(0, 0, CANVAS_SIZE[0], CANVAS_SIZE[1]))


# Each line is hex from 0 - F
FONT = '''
F0 90 90 90 F0
20 60 20 20 70
F0 10 F0 80 F0
F0 10 F0 10 F0
90 90 F0 10 10
F0 80 F0 10 F0
F0 80 F0 90 F0
F0 10 20 40 40
F0 90 F0 90 F0
F0 90 F0 10 F0
F0 90 F0 90 90
E0 90 E0 90 E0
F0 80 80 80 F0
E0 90 90 90 E0
F0 80 F0 80 F0
F0 80 F0 80 80
'''

# Add font to memory
for (cycle_count, c) in enumerate(bytes.fromhex(FONT)):
    RAM[cycle_count] = c

# Read ROM file into memory
with open(ROM, 'rb') as f:
    for (cycle_count, b) in enumerate(f.read()):
        RAM[PC + cycle_count] = b


# Starting RAM
print(bytearray.hex(RAM, ' '))
print()


def incrementPC():
    """ Increment pointer address by 2 bytes
    """
    global PC
    PC += 2


def fetch():
    """ Fetch next 2 bytes from memory
    """
    global PC
    inst = RAM[PC:PC+2]
    incrementPC()
    return inst


def decode(inst):
    global I, V, PC, sound_timer, delay_timer

    # Debug
    # print('instruction', bytearray.hex(inst, ' '))

    # First nibble
    nibble = (inst[0] >> 4)
    # Second nibble
    X = (inst[0] & 0b1111)
    # Third nibble
    Y = (inst[1] >> 4)
    # Fourth nibble
    N = (inst[1] & 0b1111)
    # Last byte
    NN = inst[1]
    # (0bXXXX00000000 | 0bYYYY0000 | 0bNNNN) == 0bXXXXYYYYNNNN
    NNN = X << 8 | Y << 4 | N

    # Instruction Matching
    match nibble:
        case 0x0:
            match int.from_bytes(inst, 'big'):
                case 0x00E0:
                    clear()
                case 0x00EE:
                    PC = STACK.pop()
        case 0x1:
            PC = NNN
        case 0x2:
            STACK.append(PC)
            PC = NNN
        case 0x3:
            incrementPC() if V[X] == NN else None
        case 0x4:
            incrementPC() if V[X] != NN else None
        case 0x5:
            incrementPC() if V[X] == V[Y] else None
        case 0x6:
            V[X] = NN
        case 0x7:
            V[X] = (V[X] + NN) % 0x100
        case 0x8:
            match N:
                case 0x0:
                    V[X] = V[Y]
                case 0x1:
                    V[X] = V[X] | V[Y]
                case 0x2:
                    V[X] = V[X] & V[Y]
                case 0x3:
                    V[X] = V[X] ^ V[Y]
                case 0x4:
                    val = V[X] + V[Y]
                    V[X] = val % 0x100
                    V[0xF] = 1 if val > 0xFF else 0
                case 0x5:
                    V[X] = (V[X] - V[Y]) % 0x100
                    V[0xF] = 1 if V[X] > V[Y] else 0
                case 0x6:
                    # TODO quirk selection
                    V[X] = (V[X] >> 1) % 0x100
                    V[0xF] = V[X] & 1
                case 0x7:
                    V[X] = (V[Y] - V[X]) % 0x100
                    V[0xF] = V[Y] > V[X]
                case 0xE:
                    # TODO quirk selection
                    V[X] = (V[X] << 1) % 0x100
                    V[0xF] = V[X] >> 7
        case 0x9:
            incrementPC() if V[X] != V[Y] else None
        case 0xA:
            I = NNN
        case 0xB:
            # TODO quirk selection
            PC = NNN + V[X]
        case 0xC:
            V[X] = random.randint(0, 255) & NN
        case 0xD:
            # DRAW
            y = V[Y] % 32
            V[0xF] = 0

            for i in range(N):
                if (y > 31):
                    break
                x = V[X] % 64
                for bit in [int(b) for b in format(RAM[I+i], '08b')]:
                    if (x > 63):
                        break
                    if (bit == 1):
                        isOn = get_pixel((x, y))
                        draw((x, y), not isOn)
                        V[0xF] = isOn
                    x += 1
                y += 1
        case 0xE:
            match NN:
                case 0x9E:
                    if KEYS[V[X]] == 1:
                        PC += 2
                case 0xA1:
                    if KEYS[V[X]] == 0:
                        PC += 2
        case 0xF:
            match NN:
                case 0x07:
                    V[X] = delay_timer
                case 0x0A:
                    key_down = False
                    key_up = False
                    while not key_down or not key_up:
                        for event in pygame.event.get(): 
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()     
                            if event.type == pygame.KEYDOWN:
                                if event.scancode in keycodes.keys():
                                    key_down = keycodes[event.scancode]
                            if event.type == pygame.KEYUP:
                                if event.scancode in keycodes.keys():
                                    if key_down == keycodes[event.scancode]:
                                        key_up = True
                                        break
                    V[X] = key_down

                case 0x15:
                    delay_timer = V[X]
                case 0x18:
                    sound_timer = V[X]
                case 0x1E:
                    val = I + V[X]
                    V[0xF] = 1 if val > 0xFFF else 0
                    I = val % 0x1000
                case 0x29:
                    I = V[X] * 5
                case 0x33:
                    val = V[X]
                    RAM[I] = V[X] // 100
                    RAM[I+1] = V[X] // 10 % 10
                    RAM[I+2] = V[X] % 10
                case 0x55:
                    for i in range(X+1):
                        RAM[I + i] = V[i]
                case 0x65:
                    for i in range(X+1):
                        V[i] = RAM[I + i]

        case _:
            print('unknown instruction')


keycodes = {
    pygame.KSCAN_1: 0x1,
    pygame.KSCAN_2: 0x2,
    pygame.KSCAN_3: 0x3,
    pygame.KSCAN_Q: 0x4,
    pygame.KSCAN_W: 0x5,
    pygame.KSCAN_E: 0x6,
    pygame.KSCAN_A: 0x7,
    pygame.KSCAN_S: 0x8,
    pygame.KSCAN_D: 0x9,
    pygame.KSCAN_X: 0x0,
    pygame.KSCAN_Z: 0xA,
    pygame.KSCAN_C: 0xB,
    pygame.KSCAN_4: 0xC,
    pygame.KSCAN_R: 0xD,
    pygame.KSCAN_F: 0xE,
    pygame.KSCAN_V: 0xF,
}

clock = time.time()
while True:
    curr = time.time()
    if (curr > clock + 1/60):
        clock = curr
        if delay_timer > 0:
            delay_timer -= 1
        if sound_timer > 0:
            sound_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.scancode in keycodes.keys():
                KEYS[keycodes[event.scancode]] = 1
        if event.type == pygame.KEYUP:
            if event.scancode in keycodes.keys():
                KEYS[keycodes[event.scancode]] = 0

    if (sound_timer > 0):
        #TODO find a way to play a static long sound rather than a clip that can "end"
        pass

    # Operation
    data = fetch()
    decode(data)
    update_display()
    time.sleep(1/700)
