import json
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext

with open('GB/opcodes.json') as f:
    opcodes = json.loads(f.read())


def disassemble(file_path):
    ROM_PATH = file_path
    CARTRIDGE = bytearray()

    PC = 0x0000

    with open(ROM_PATH, 'rb') as f:
        for (cycle_count, b) in enumerate(f.read()):
            CARTRIDGE.append(b)

    def int_to_hex(value):
        return '0x' + hex(value)[2:].zfill(2).upper()

    def opcode_output(PC, opcode):
        ops = []
        for operand in opcode['operands']:
            if 'bytes' in operand:
                ops.append(int_to_hex(int.from_bytes(
                    bytes(CARTRIDGE[PC+1:PC+1+int(operand['bytes'])])[::-1])))
                continue
            ops.append(operand['name'])
        return f"{opcode['mnemonic']} {', '.join(ops)}"

    rows = []
    print(len(CARTRIDGE))
    while PC < len(CARTRIDGE):
        if PC >= 0x104 and PC < 0x150:
            # TODO CARTRIDGE HEADER
            PC = PC + 1
            continue

        data = int_to_hex(CARTRIDGE[PC])
        if (data == 0xCB):
            data = int_to_hex(CARTRIDGE[PC + 1])
            opcode = opcodes['cbprefixed'][data]
            rows.append(f"{int_to_hex(PC)} {opcode_output(PC + 1, opcode)}")
            PC = PC + opcode['bytes'] + 1
            continue
        opcode = opcodes['unprefixed'][data]
        rows.append(f"{int_to_hex(PC)} {opcode_output(PC, opcode)}")
        PC = PC + opcode['bytes']
    return rows


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("GB Files", "*.gb"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    textw.configure(state="normal")
    textw.insert(tk.END, '\n'.join(disassemble(filepath)))
    textw.configure(state="disabled")


# CANVAS_SIZE = (800, 450)
window = tk.Tk()
window.title("GB Dissasembler")

frame_a = tk.Frame()
btn_open = tk.Button(frame_a, text="Open", command=open_file)
btn_open.pack()

frame_b = tk.Frame()
textw = scrolledtext.ScrolledText(frame_b, width=70, height=30)
textw.configure(state="disabled")
textw.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
