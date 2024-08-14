from pyvologb.helpers import formatted_hex
from pyvologb.mmu import MMU
from pyvologb.registers import Registers


class Opcodes:
    def __init__(self, mmu: MMU, registers: Registers) -> None:
        self.mmu = mmu
        self.R = registers

    def read_bytes(self, count: int) -> int:
        data = int.from_bytes(
            bytes([self.mmu.get_memory(self.R.PC + i) for i in range(count)]),
            "little",
        )
        self.R.PC += count
        return data

    def execute(self, opcode: int) -> int:
        self.R.PC += 1

        match opcode:
            case 0x00:
                return self.NOP_00()
            case 0x01:
                return self.LD_01(self.read_bytes(2))
            case 0x02:
                return self.LD_02()
            case 0x03:
                return self.INC_03()
            case 0x04:
                return self.INC_04()
            case 0x05:
                return self.DEC_05()
            case 0x06:
                return self.LD_06(self.read_bytes(1))
            case 0x07:
                return self.RLCA_07()
            case 0x08:
                return self.LD_08(self.read_bytes(2))
            case 0x09:
                return self.ADD_09()
            case 0x0A:
                return self.LD_0A()
            case 0x0B:
                return self.DEC_0B()
            case 0x0C:
                return self.INC_0C()
            case 0x0D:
                return self.DEC_0D()
            case 0x0E:
                return self.LD_0E(self.read_bytes(1))
            case 0x0F:
                return self.RRCA_0F()
            case 0x10:
                return self.STOP_10()
            case 0x11:
                return self.LD_11(self.read_bytes(2))
            case 0x12:
                return self.LD_12()
            case 0x13:
                return self.INC_13()
            case 0x14:
                return self.INC_14()
            case 0x15:
                return self.DEC_15()
            case 0x16:
                return self.LD_16(self.read_bytes(1))
            case 0x17:
                return self.RLA_17()
            case 0x18:
                return self.JR_18(self.read_bytes(1))
            case 0x19:
                return self.ADD_19()
            case 0x1A:
                return self.LD_1A()
            case 0x1B:
                return self.DEC_1B()
            case 0x1C:
                return self.INC_1C()
            case 0x1D:
                return self.DEC_1D()
            case 0x1E:
                return self.LD_1E(self.read_bytes(1))
            case 0x1F:
                return self.RRA_1F()
            case 0x20:
                return self.JR_20(self.read_bytes(1))
            case 0x21:
                return self.LD_21(self.read_bytes(2))
            case 0x22:
                return self.LD_22()
            case 0x23:
                return self.INC_23()
            case 0x24:
                return self.INC_24()
            case 0x25:
                return self.DEC_25()
            case 0x26:
                return self.LD_26(self.read_bytes(1))
            case 0x27:
                return self.DAA_27()
            case 0x28:
                return self.JR_28(self.read_bytes(1))
            case 0x29:
                return self.ADD_29()
            case 0x2A:
                return self.LD_2A()
            case 0x2B:
                return self.DEC_2B()
            case 0x2C:
                return self.INC_2C()
            case 0x2D:
                return self.DEC_2D()
            case 0x2E:
                return self.LD_2E(self.read_bytes(1))
            case 0x2F:
                return self.CPL_2F()
            case 0x30:
                return self.JR_30(self.read_bytes(1))
            case 0x31:
                return self.LD_31(self.read_bytes(2))
            case 0x32:
                return self.LD_32()
            case 0x33:
                return self.INC_33()
            case 0x34:
                return self.INC_34()
            case 0x35:
                return self.DEC_35()
            case 0x36:
                return self.LD_36(self.read_bytes(1))
            case 0x37:
                return self.SCF_37()
            case 0x38:
                return self.JR_38(self.read_bytes(1))
            case 0x39:
                return self.ADD_39()
            case 0x3A:
                return self.LD_3A()
            case 0x3B:
                return self.DEC_3B()
            case 0x3C:
                return self.INC_3C()
            case 0x3D:
                return self.DEC_3D()
            case 0x3E:
                return self.LD_3E(self.read_bytes(1))
            case 0x3F:
                return self.CCF_3F()
            case 0x40:
                return self.LD_40()
            case 0x41:
                return self.LD_41()
            case 0x42:
                return self.LD_42()
            case 0x43:
                return self.LD_43()
            case 0x44:
                return self.LD_44()
            case 0x45:
                return self.LD_45()
            case 0x46:
                return self.LD_46()
            case 0x47:
                return self.LD_47()
            case 0x48:
                return self.LD_48()
            case 0x49:
                return self.LD_49()
            case 0x4A:
                return self.LD_4A()
            case 0x4B:
                return self.LD_4B()
            case 0x4C:
                return self.LD_4C()
            case 0x4D:
                return self.LD_4D()
            case 0x4E:
                return self.LD_4E()
            case 0x4F:
                return self.LD_4F()
            case 0x50:
                return self.LD_50()
            case 0x51:
                return self.LD_51()
            case 0x52:
                return self.LD_52()
            case 0x53:
                return self.LD_53()
            case 0x54:
                return self.LD_54()
            case 0x55:
                return self.LD_55()
            case 0x56:
                return self.LD_56()
            case 0x57:
                return self.LD_57()
            case 0x58:
                return self.LD_58()
            case 0x59:
                return self.LD_59()
            case 0x5A:
                return self.LD_5A()
            case 0x5B:
                return self.LD_5B()
            case 0x5C:
                return self.LD_5C()
            case 0x5D:
                return self.LD_5D()
            case 0x5E:
                return self.LD_5E()
            case 0x5F:
                return self.LD_5F()
            case 0x60:
                return self.LD_60()
            case 0x61:
                return self.LD_61()
            case 0x62:
                return self.LD_62()
            case 0x63:
                return self.LD_63()
            case 0x64:
                return self.LD_64()
            case 0x65:
                return self.LD_65()
            case 0x66:
                return self.LD_66()
            case 0x67:
                return self.LD_67()
            case 0x68:
                return self.LD_68()
            case 0x69:
                return self.LD_69()
            case 0x6A:
                return self.LD_6A()
            case 0x6B:
                return self.LD_6B()
            case 0x6C:
                return self.LD_6C()
            case 0x6D:
                return self.LD_6D()
            case 0x6E:
                return self.LD_6E()
            case 0x6F:
                return self.LD_6F()
            case 0x70:
                return self.LD_70()
            case 0x71:
                return self.LD_71()
            case 0x72:
                return self.LD_72()
            case 0x73:
                return self.LD_73()
            case 0x74:
                return self.LD_74()
            case 0x75:
                return self.LD_75()
            case 0x76:
                return self.HALT_76()
            case 0x77:
                return self.LD_77()
            case 0x78:
                return self.LD_78()
            case 0x79:
                return self.LD_79()
            case 0x7A:
                return self.LD_7A()
            case 0x7B:
                return self.LD_7B()
            case 0x7C:
                return self.LD_7C()
            case 0x7D:
                return self.LD_7D()
            case 0x7E:
                return self.LD_7E()
            case 0x7F:
                return self.LD_7F()
            case 0x80:
                return self.ADD_80()
            case 0x81:
                return self.ADD_81()
            case 0x82:
                return self.ADD_82()
            case 0x83:
                return self.ADD_83()
            case 0x84:
                return self.ADD_84()
            case 0x85:
                return self.ADD_85()
            case 0x86:
                return self.ADD_86()
            case 0x87:
                return self.ADD_87()
            case 0x88:
                return self.ADC_88()
            case 0x89:
                return self.ADC_89()
            case 0x8A:
                return self.ADC_8A()
            case 0x8B:
                return self.ADC_8B()
            case 0x8C:
                return self.ADC_8C()
            case 0x8D:
                return self.ADC_8D()
            case 0x8E:
                return self.ADC_8E()
            case 0x8F:
                return self.ADC_8F()
            case 0x90:
                return self.SUB_90()
            case 0x91:
                return self.SUB_91()
            case 0x92:
                return self.SUB_92()
            case 0x93:
                return self.SUB_93()
            case 0x94:
                return self.SUB_94()
            case 0x95:
                return self.SUB_95()
            case 0x96:
                return self.SUB_96()
            case 0x97:
                return self.SUB_97()
            case 0x98:
                return self.SBC_98()
            case 0x99:
                return self.SBC_99()
            case 0x9A:
                return self.SBC_9A()
            case 0x9B:
                return self.SBC_9B()
            case 0x9C:
                return self.SBC_9C()
            case 0x9D:
                return self.SBC_9D()
            case 0x9E:
                return self.SBC_9E()
            case 0x9F:
                return self.SBC_9F()
            case 0xA0:
                return self.AND_A0()
            case 0xA1:
                return self.AND_A1()
            case 0xA2:
                return self.AND_A2()
            case 0xA3:
                return self.AND_A3()
            case 0xA4:
                return self.AND_A4()
            case 0xA5:
                return self.AND_A5()
            case 0xA6:
                return self.AND_A6()
            case 0xA7:
                return self.AND_A7()
            case 0xA8:
                return self.XOR_A8()
            case 0xA9:
                return self.XOR_A9()
            case 0xAA:
                return self.XOR_AA()
            case 0xAB:
                return self.XOR_AB()
            case 0xAC:
                return self.XOR_AC()
            case 0xAD:
                return self.XOR_AD()
            case 0xAE:
                return self.XOR_AE()
            case 0xAF:
                return self.XOR_AF()
            case 0xB0:
                return self.OR_B0()
            case 0xB1:
                return self.OR_B1()
            case 0xB2:
                return self.OR_B2()
            case 0xB3:
                return self.OR_B3()
            case 0xB4:
                return self.OR_B4()
            case 0xB5:
                return self.OR_B5()
            case 0xB6:
                return self.OR_B6()
            case 0xB7:
                return self.OR_B7()
            case 0xB8:
                return self.CP_B8()
            case 0xB9:
                return self.CP_B9()
            case 0xBA:
                return self.CP_BA()
            case 0xBB:
                return self.CP_BB()
            case 0xBC:
                return self.CP_BC()
            case 0xBD:
                return self.CP_BD()
            case 0xBE:
                return self.CP_BE()
            case 0xBF:
                return self.CP_BF()
            case 0xC0:
                return self.RET_C0()
            case 0xC1:
                return self.POP_C1()
            case 0xC2:
                return self.JP_C2(self.read_bytes(2))
            case 0xC3:
                return self.JP_C3(self.read_bytes(2))
            case 0xC4:
                return self.CALL_C4(self.read_bytes(2))
            case 0xC5:
                return self.PUSH_C5()
            case 0xC6:
                return self.ADD_C6(self.read_bytes(1))
            case 0xC7:
                return self.RST_C7()
            case 0xC8:
                return self.RET_C8()
            case 0xC9:
                return self.RET_C9()
            case 0xCA:
                return self.JP_CA(self.read_bytes(2))
            case 0xCB:
                raise Exception(f"Invalid Execution Order: {formatted_hex(opcode)}")
            case 0xCC:
                return self.CALL_CC(self.read_bytes(2))
            case 0xCD:
                return self.CALL_CD(self.read_bytes(2))
            case 0xCE:
                return self.ADC_CE(self.read_bytes(1))
            case 0xCF:
                return self.RST_CF()
            case 0xD0:
                return self.RET_D0()
            case 0xD1:
                return self.POP_D1()
            case 0xD2:
                return self.JP_D2(self.read_bytes(2))
            case 0xD3:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xD4:
                return self.CALL_D4(self.read_bytes(2))
            case 0xD5:
                return self.PUSH_D5()
            case 0xD6:
                return self.SUB_D6(self.read_bytes(1))
            case 0xD7:
                return self.RST_D7()
            case 0xD8:
                return self.RET_D8()
            case 0xD9:
                return self.RETI_D9()
            case 0xDA:
                return self.JP_DA(self.read_bytes(2))
            case 0xDB:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xDC:
                return self.CALL_DC(self.read_bytes(2))
            case 0xDD:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xDE:
                return self.SBC_DE(self.read_bytes(1))
            case 0xDF:
                return self.RST_DF()
            case 0xE0:
                return self.LDH_E0(self.read_bytes(1))
            case 0xE1:
                return self.POP_E1()
            case 0xE2:
                return self.LDH_E2()
            case 0xE3:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xE4:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xE5:
                return self.PUSH_E5()
            case 0xE6:
                return self.AND_E6(self.read_bytes(1))
            case 0xE7:
                return self.RST_E7()
            case 0xE8:
                return self.ADD_E8(self.read_bytes(1))
            case 0xE9:
                return self.JP_E9()
            case 0xEA:
                return self.LD_EA(self.read_bytes(2))
            case 0xEB:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xEC:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xED:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xEE:
                return self.XOR_EE(self.read_bytes(1))
            case 0xEF:
                return self.RST_EF()
            case 0xF0:
                return self.LDH_F0(self.read_bytes(1))
            case 0xF1:
                return self.POP_F1()
            case 0xF2:
                return self.LDH_F2()
            case 0xF3:
                return self.DI_F3()
            case 0xF4:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xF5:
                return self.PUSH_F5()
            case 0xF6:
                return self.OR_F6(self.read_bytes(1))
            case 0xF7:
                return self.RST_F7()
            case 0xF8:
                return self.LD_F8(self.read_bytes(1))
            case 0xF9:
                return self.LD_F9()
            case 0xFA:
                return self.LD_FA(self.read_bytes(2))
            case 0xFB:
                return self.EI_FB()
            case 0xFC:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xFD:
                raise Exception(f"Illegal Opcode: {formatted_hex(opcode)}")
            case 0xFE:
                return self.CP_FE(self.read_bytes(1))
            case 0xFF:
                return self.RST_FF()
            case 0x100:
                return self.RLC_CB00()
            case 0x101:
                return self.RLC_CB01()
            case 0x102:
                return self.RLC_CB02()
            case 0x103:
                return self.RLC_CB03()
            case 0x104:
                return self.RLC_CB04()
            case 0x105:
                return self.RLC_CB05()
            case 0x106:
                return self.RLC_CB06()
            case 0x107:
                return self.RLC_CB07()
            case 0x108:
                return self.RRC_CB08()
            case 0x109:
                return self.RRC_CB09()
            case 0x10A:
                return self.RRC_CB0A()
            case 0x10B:
                return self.RRC_CB0B()
            case 0x10C:
                return self.RRC_CB0C()
            case 0x10D:
                return self.RRC_CB0D()
            case 0x10E:
                return self.RRC_CB0E()
            case 0x10F:
                return self.RRC_CB0F()
            case 0x110:
                return self.RL_CB10()
            case 0x111:
                return self.RL_CB11()
            case 0x112:
                return self.RL_CB12()
            case 0x113:
                return self.RL_CB13()
            case 0x114:
                return self.RL_CB14()
            case 0x115:
                return self.RL_CB15()
            case 0x116:
                return self.RL_CB16()
            case 0x117:
                return self.RL_CB17()
            case 0x118:
                return self.RR_CB18()
            case 0x119:
                return self.RR_CB19()
            case 0x11A:
                return self.RR_CB1A()
            case 0x11B:
                return self.RR_CB1B()
            case 0x11C:
                return self.RR_CB1C()
            case 0x11D:
                return self.RR_CB1D()
            case 0x11E:
                return self.RR_CB1E()
            case 0x11F:
                return self.RR_CB1F()
            case 0x120:
                return self.SLA_CB20()
            case 0x121:
                return self.SLA_CB21()
            case 0x122:
                return self.SLA_CB22()
            case 0x123:
                return self.SLA_CB23()
            case 0x124:
                return self.SLA_CB24()
            case 0x125:
                return self.SLA_CB25()
            case 0x126:
                return self.SLA_CB26()
            case 0x127:
                return self.SLA_CB27()
            case 0x128:
                return self.SRA_CB28()
            case 0x129:
                return self.SRA_CB29()
            case 0x12A:
                return self.SRA_CB2A()
            case 0x12B:
                return self.SRA_CB2B()
            case 0x12C:
                return self.SRA_CB2C()
            case 0x12D:
                return self.SRA_CB2D()
            case 0x12E:
                return self.SRA_CB2E()
            case 0x12F:
                return self.SRA_CB2F()
            case 0x130:
                return self.SWAP_CB30()
            case 0x131:
                return self.SWAP_CB31()
            case 0x132:
                return self.SWAP_CB32()
            case 0x133:
                return self.SWAP_CB33()
            case 0x134:
                return self.SWAP_CB34()
            case 0x135:
                return self.SWAP_CB35()
            case 0x136:
                return self.SWAP_CB36()
            case 0x137:
                return self.SWAP_CB37()
            case 0x138:
                return self.SRL_CB38()
            case 0x139:
                return self.SRL_CB39()
            case 0x13A:
                return self.SRL_CB3A()
            case 0x13B:
                return self.SRL_CB3B()
            case 0x13C:
                return self.SRL_CB3C()
            case 0x13D:
                return self.SRL_CB3D()
            case 0x13E:
                return self.SRL_CB3E()
            case 0x13F:
                return self.SRL_CB3F()
            case 0x140:
                return self.BIT_CB40()
            case 0x141:
                return self.BIT_CB41()
            case 0x142:
                return self.BIT_CB42()
            case 0x143:
                return self.BIT_CB43()
            case 0x144:
                return self.BIT_CB44()
            case 0x145:
                return self.BIT_CB45()
            case 0x146:
                return self.BIT_CB46()
            case 0x147:
                return self.BIT_CB47()
            case 0x148:
                return self.BIT_CB48()
            case 0x149:
                return self.BIT_CB49()
            case 0x14A:
                return self.BIT_CB4A()
            case 0x14B:
                return self.BIT_CB4B()
            case 0x14C:
                return self.BIT_CB4C()
            case 0x14D:
                return self.BIT_CB4D()
            case 0x14E:
                return self.BIT_CB4E()
            case 0x14F:
                return self.BIT_CB4F()
            case 0x150:
                return self.BIT_CB50()
            case 0x151:
                return self.BIT_CB51()
            case 0x152:
                return self.BIT_CB52()
            case 0x153:
                return self.BIT_CB53()
            case 0x154:
                return self.BIT_CB54()
            case 0x155:
                return self.BIT_CB55()
            case 0x156:
                return self.BIT_CB56()
            case 0x157:
                return self.BIT_CB57()
            case 0x158:
                return self.BIT_CB58()
            case 0x159:
                return self.BIT_CB59()
            case 0x15A:
                return self.BIT_CB5A()
            case 0x15B:
                return self.BIT_CB5B()
            case 0x15C:
                return self.BIT_CB5C()
            case 0x15D:
                return self.BIT_CB5D()
            case 0x15E:
                return self.BIT_CB5E()
            case 0x15F:
                return self.BIT_CB5F()
            case 0x160:
                return self.BIT_CB60()
            case 0x161:
                return self.BIT_CB61()
            case 0x162:
                return self.BIT_CB62()
            case 0x163:
                return self.BIT_CB63()
            case 0x164:
                return self.BIT_CB64()
            case 0x165:
                return self.BIT_CB65()
            case 0x166:
                return self.BIT_CB66()
            case 0x167:
                return self.BIT_CB67()
            case 0x168:
                return self.BIT_CB68()
            case 0x169:
                return self.BIT_CB69()
            case 0x16A:
                return self.BIT_CB6A()
            case 0x16B:
                return self.BIT_CB6B()
            case 0x16C:
                return self.BIT_CB6C()
            case 0x16D:
                return self.BIT_CB6D()
            case 0x16E:
                return self.BIT_CB6E()
            case 0x16F:
                return self.BIT_CB6F()
            case 0x170:
                return self.BIT_CB70()
            case 0x171:
                return self.BIT_CB71()
            case 0x172:
                return self.BIT_CB72()
            case 0x173:
                return self.BIT_CB73()
            case 0x174:
                return self.BIT_CB74()
            case 0x175:
                return self.BIT_CB75()
            case 0x176:
                return self.BIT_CB76()
            case 0x177:
                return self.BIT_CB77()
            case 0x178:
                return self.BIT_CB78()
            case 0x179:
                return self.BIT_CB79()
            case 0x17A:
                return self.BIT_CB7A()
            case 0x17B:
                return self.BIT_CB7B()
            case 0x17C:
                return self.BIT_CB7C()
            case 0x17D:
                return self.BIT_CB7D()
            case 0x17E:
                return self.BIT_CB7E()
            case 0x17F:
                return self.BIT_CB7F()
            case 0x180:
                return self.RES_CB80()
            case 0x181:
                return self.RES_CB81()
            case 0x182:
                return self.RES_CB82()
            case 0x183:
                return self.RES_CB83()
            case 0x184:
                return self.RES_CB84()
            case 0x185:
                return self.RES_CB85()
            case 0x186:
                return self.RES_CB86()
            case 0x187:
                return self.RES_CB87()
            case 0x188:
                return self.RES_CB88()
            case 0x189:
                return self.RES_CB89()
            case 0x18A:
                return self.RES_CB8A()
            case 0x18B:
                return self.RES_CB8B()
            case 0x18C:
                return self.RES_CB8C()
            case 0x18D:
                return self.RES_CB8D()
            case 0x18E:
                return self.RES_CB8E()
            case 0x18F:
                return self.RES_CB8F()
            case 0x190:
                return self.RES_CB90()
            case 0x191:
                return self.RES_CB91()
            case 0x192:
                return self.RES_CB92()
            case 0x193:
                return self.RES_CB93()
            case 0x194:
                return self.RES_CB94()
            case 0x195:
                return self.RES_CB95()
            case 0x196:
                return self.RES_CB96()
            case 0x197:
                return self.RES_CB97()
            case 0x198:
                return self.RES_CB98()
            case 0x199:
                return self.RES_CB99()
            case 0x19A:
                return self.RES_CB9A()
            case 0x19B:
                return self.RES_CB9B()
            case 0x19C:
                return self.RES_CB9C()
            case 0x19D:
                return self.RES_CB9D()
            case 0x19E:
                return self.RES_CB9E()
            case 0x19F:
                return self.RES_CB9F()
            case 0x1A0:
                return self.RES_CBA0()
            case 0x1A1:
                return self.RES_CBA1()
            case 0x1A2:
                return self.RES_CBA2()
            case 0x1A3:
                return self.RES_CBA3()
            case 0x1A4:
                return self.RES_CBA4()
            case 0x1A5:
                return self.RES_CBA5()
            case 0x1A6:
                return self.RES_CBA6()
            case 0x1A7:
                return self.RES_CBA7()
            case 0x1A8:
                return self.RES_CBA8()
            case 0x1A9:
                return self.RES_CBA9()
            case 0x1AA:
                return self.RES_CBAA()
            case 0x1AB:
                return self.RES_CBAB()
            case 0x1AC:
                return self.RES_CBAC()
            case 0x1AD:
                return self.RES_CBAD()
            case 0x1AE:
                return self.RES_CBAE()
            case 0x1AF:
                return self.RES_CBAF()
            case 0x1B0:
                return self.RES_CBB0()
            case 0x1B1:
                return self.RES_CBB1()
            case 0x1B2:
                return self.RES_CBB2()
            case 0x1B3:
                return self.RES_CBB3()
            case 0x1B4:
                return self.RES_CBB4()
            case 0x1B5:
                return self.RES_CBB5()
            case 0x1B6:
                return self.RES_CBB6()
            case 0x1B7:
                return self.RES_CBB7()
            case 0x1B8:
                return self.RES_CBB8()
            case 0x1B9:
                return self.RES_CBB9()
            case 0x1BA:
                return self.RES_CBBA()
            case 0x1BB:
                return self.RES_CBBB()
            case 0x1BC:
                return self.RES_CBBC()
            case 0x1BD:
                return self.RES_CBBD()
            case 0x1BE:
                return self.RES_CBBE()
            case 0x1BF:
                return self.RES_CBBF()
            case 0x1C0:
                return self.SET_CBC0()
            case 0x1C1:
                return self.SET_CBC1()
            case 0x1C2:
                return self.SET_CBC2()
            case 0x1C3:
                return self.SET_CBC3()
            case 0x1C4:
                return self.SET_CBC4()
            case 0x1C5:
                return self.SET_CBC5()
            case 0x1C6:
                return self.SET_CBC6()
            case 0x1C7:
                return self.SET_CBC7()
            case 0x1C8:
                return self.SET_CBC8()
            case 0x1C9:
                return self.SET_CBC9()
            case 0x1CA:
                return self.SET_CBCA()
            case 0x1CB:
                return self.SET_CBCB()
            case 0x1CC:
                return self.SET_CBCC()
            case 0x1CD:
                return self.SET_CBCD()
            case 0x1CE:
                return self.SET_CBCE()
            case 0x1CF:
                return self.SET_CBCF()
            case 0x1D0:
                return self.SET_CBD0()
            case 0x1D1:
                return self.SET_CBD1()
            case 0x1D2:
                return self.SET_CBD2()
            case 0x1D3:
                return self.SET_CBD3()
            case 0x1D4:
                return self.SET_CBD4()
            case 0x1D5:
                return self.SET_CBD5()
            case 0x1D6:
                return self.SET_CBD6()
            case 0x1D7:
                return self.SET_CBD7()
            case 0x1D8:
                return self.SET_CBD8()
            case 0x1D9:
                return self.SET_CBD9()
            case 0x1DA:
                return self.SET_CBDA()
            case 0x1DB:
                return self.SET_CBDB()
            case 0x1DC:
                return self.SET_CBDC()
            case 0x1DD:
                return self.SET_CBDD()
            case 0x1DE:
                return self.SET_CBDE()
            case 0x1DF:
                return self.SET_CBDF()
            case 0x1E0:
                return self.SET_CBE0()
            case 0x1E1:
                return self.SET_CBE1()
            case 0x1E2:
                return self.SET_CBE2()
            case 0x1E3:
                return self.SET_CBE3()
            case 0x1E4:
                return self.SET_CBE4()
            case 0x1E5:
                return self.SET_CBE5()
            case 0x1E6:
                return self.SET_CBE6()
            case 0x1E7:
                return self.SET_CBE7()
            case 0x1E8:
                return self.SET_CBE8()
            case 0x1E9:
                return self.SET_CBE9()
            case 0x1EA:
                return self.SET_CBEA()
            case 0x1EB:
                return self.SET_CBEB()
            case 0x1EC:
                return self.SET_CBEC()
            case 0x1ED:
                return self.SET_CBED()
            case 0x1EE:
                return self.SET_CBEE()
            case 0x1EF:
                return self.SET_CBEF()
            case 0x1F0:
                return self.SET_CBF0()
            case 0x1F1:
                return self.SET_CBF1()
            case 0x1F2:
                return self.SET_CBF2()
            case 0x1F3:
                return self.SET_CBF3()
            case 0x1F4:
                return self.SET_CBF4()
            case 0x1F5:
                return self.SET_CBF5()
            case 0x1F6:
                return self.SET_CBF6()
            case 0x1F7:
                return self.SET_CBF7()
            case 0x1F8:
                return self.SET_CBF8()
            case 0x1F9:
                return self.SET_CBF9()
            case 0x1FA:
                return self.SET_CBFA()
            case 0x1FB:
                return self.SET_CBFB()
            case 0x1FC:
                return self.SET_CBFC()
            case 0x1FD:
                return self.SET_CBFD()
            case 0x1FE:
                return self.SET_CBFE()
            case 0x1FF:
                return self.SET_CBFF()
            case _:
                raise Exception(f"Unknown Instruction: {formatted_hex(opcode)}")

    def NOP_00(self) -> int:
        """NOP"""
        return 4

    def LD_01(self, value: int) -> int:
        """LD BC, n16"""
        self.R.BC = value
        return 12

    def LD_02(self) -> int:
        """LD [BC], A"""
        self.mmu.set_memory(self.R.BC, self.R.A)
        return 8

    def INC_03(self) -> int:
        """INC BC"""
        self.R.BC = (self.R.BC + 1) & 0xFFFF
        return 8

    def INC_04(self) -> int:
        """INC B"""
        calc = self.R.B + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.B & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF

        self.R.B = calc
        return 4

    def DEC_05(self) -> int:
        """DEC B"""
        calc = self.R.B - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.B & 0xF) - 1 < 0) & 1
        calc &= 0xFF

        self.R.B = calc
        return 4

    def LD_06(self, value: int) -> int:
        """LD B, n8"""
        self.R.B = value
        return 8

    def RLCA_07(self) -> int:
        """RLCA"""
        initial = self.R.A
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110 | carryBit
        self.R.A = calc

        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return 4

    def LD_08(self, address: int) -> int:
        """LD [n16],SP"""
        self.mmu.set_memory(address, self.R.SP & 0xFF)
        self.mmu.set_memory(address + 1, self.R.SP >> 8)
        return 20

    def ADD_09(self) -> int:
        """ADD HL, BC"""
        calc = self.R.HL + self.R.BC

        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.HL & 0xFFF) + (self.R.BC & 0xFFF) > 0xFFF) & 1
        self.R.CARRY = (calc > 0xFFFF) & 1

        self.R.HL = calc & 0xFFFF
        return 8

    def LD_0A(self) -> int:
        """LD A, [BC]"""
        self.R.A = self.mmu.get_memory(self.R.BC)
        return 8

    def DEC_0B(self) -> int:
        """DEC BC"""
        self.R.BC = (self.R.BC - 1) & 0xFFFF
        return 8

    def INC_0C(self) -> int:
        """INC C"""
        calc = self.R.C + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.C & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF

        self.R.C = calc
        return 4

    def DEC_0D(self) -> int:
        """DEC C"""
        calc = self.R.C - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.C & 0xF) - 1 < 0) & 1
        calc &= 0xFF

        self.R.C = calc
        return 4

    def LD_0E(self, value: int) -> int:
        """LD C, n8"""
        self.R.C = value
        return 8

    def RRCA_0F(self) -> int:
        """RRCA"""
        initial = self.R.A
        carryBit = initial & 1
        calc = (carryBit << 7) | initial >> 1
        self.R.A = calc

        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return 4

    def STOP_10(self) -> int:
        """STOP 0"""
        return 4

    def LD_11(self, value: int) -> int:
        """LD DE, n16"""
        self.R.DE = value
        return 12

    def LD_12(self) -> int:
        """LD [DE], A"""
        self.mmu.set_memory(self.R.DE, self.R.A)
        return 8

    def INC_13(self) -> int:
        """INC DE"""
        self.R.DE = (self.R.DE + 1) & 0xFFFF
        return 8

    def INC_14(self) -> int:
        """INC D"""
        calc = self.R.D + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.D & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF

        self.R.D = calc
        return 4

    def DEC_15(self) -> int:
        """DEC D"""
        calc = self.R.D - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.D & 0xF) - 1 < 0) & 1
        calc &= 0xFF

        self.R.D = calc
        return 4

    def LD_16(self, value: int) -> int:
        """LD D, n8"""
        self.R.D = value
        return 8

    def RLA_17(self) -> int:
        """RLA"""
        initial = self.R.A
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110 | self.R.CARRY
        self.R.A = calc

        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return 4

    def JR_18(self, value: int) -> int:
        """JR e8"""
        addr = (value ^ 0x80) - 0x80
        self.R.PC += addr
        return 12

    def ADD_19(self) -> int:
        """ADD HL, DE"""
        calc = self.R.HL + self.R.DE

        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.HL & 0xFFF) + (self.R.DE & 0xFFF) > 0xFFF) & 1
        self.R.CARRY = (calc > 0xFFFF) & 1

        self.R.HL = calc & 0xFFFF
        return 8

    def LD_1A(self) -> int:
        """LD A, [DE]"""
        self.R.A = self.mmu.get_memory(self.R.DE)
        return 8

    def DEC_1B(self) -> int:
        """DEC DE"""
        self.R.DE = (self.R.DE - 1) & 0xFFFF
        return 8

    def INC_1C(self) -> int:
        """INC E"""
        calc = self.R.E + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.E & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF
        self.R.E = calc
        return 4

    def DEC_1D(self) -> int:
        """DEC E"""
        calc = self.R.E - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.E & 0xF) - 1 < 0) & 1
        calc &= 0xFF
        self.R.E = calc
        return 4

    def LD_1E(self, value: int) -> int:
        """LD E, n8"""
        self.R.E = value
        return 8

    def RRA_1F(self) -> int:
        """RRA"""
        initial = self.R.A
        carryBit = initial & 1
        calc = (self.R.CARRY << 7) | initial >> 1
        self.R.A = calc
        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return 4

    def JR_20(self, value: int) -> int:
        """JR NZ,e8"""
        if self.R.ZERO == 0:
            addr = (value ^ 0x80) - 0x80
            self.R.PC += addr
            return 12
        return 8

    def LD_21(self, value: int) -> int:
        """LD HL, n16"""
        self.R.HL = value
        return 12

    def LD_22(self) -> int:
        """LD [HLI],A"""
        self.mmu.set_memory(self.R.HL, self.R.A)
        self.R.HL = (self.R.HL + 1) & 0xFFFF
        return 8

    def INC_23(self) -> int:
        """INC HL"""
        self.R.HL = (self.R.HL + 1) & 0xFFFF
        return 8

    def INC_24(self) -> int:
        """INC H"""
        calc = self.R.H + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.H & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF
        self.R.H = calc
        return 4

    def DEC_25(self) -> int:
        """DEC H"""
        calc = self.R.H - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.H & 0xF) - 1 < 0) & 1
        calc &= 0xFF
        self.R.H = calc
        return 4

    def LD_26(self, value: int) -> int:
        """LD H, n8"""
        self.R.H = value
        return 8

    def DAA_27(self) -> int:
        """DAA"""
        # Credit to https://blog.ollien.com/posts/gb-daa/ for the logic
        offset = 0
        carryBit = 0

        if (self.R.SUBTRACTION == 0 and self.R.A & 0xF > 0x09) or self.R.HALFCARRY == 1:
            offset |= 0x06
        if (self.R.SUBTRACTION == 0 and self.R.A > 0x99) or self.R.CARRY == 1:
            offset |= 0x60
            carryBit = 1

        final = (
            (self.R.A + offset) & 0xFF
            if self.R.SUBTRACTION == 0
            else (self.R.A - offset) & 0xFF
        )
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return 4

    def JR_28(self, value: int) -> int:
        """JR Z,e8"""
        if self.R.ZERO == 1:
            addr = (value ^ 0x80) - 0x80
            self.R.PC += addr
            return 12
        return 8

    def ADD_29(self) -> int:
        """ADD HL, HL"""
        calc = self.R.HL + self.R.HL
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.HL & 0xFFF) + (self.R.HL & 0xFFF) > 0xFFF) & 1
        self.R.CARRY = (calc > 0xFFFF) & 1
        self.R.HL = calc & 0xFFFF
        return 8

    def LD_2A(self) -> int:
        """LD A, [HLI]"""
        self.R.A = self.mmu.get_memory(self.R.HL)
        self.R.HL = (self.R.HL + 1) & 0xFFFF
        return 8

    def DEC_2B(self) -> int:
        """DEC HL"""
        self.R.HL = (self.R.HL - 1) & 0xFFFF
        return 8

    def INC_2C(self) -> int:
        """INC L"""
        calc = self.R.L + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.L & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF
        self.R.L = calc
        return 4

    def DEC_2D(self) -> int:
        """DEC L"""
        calc = self.R.L - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.L & 0xF) - 1 < 0) & 1
        calc &= 0xFF
        self.R.L = calc
        return 4

    def LD_2E(self, value: int) -> int:
        """LD L, n8"""
        self.R.L = value
        return 8

    def CPL_2F(self) -> int:
        """CPL"""
        self.R.A = self.R.A ^ 0xFF
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = 1
        return 4

    def JR_30(self, value: int) -> int:
        """JR NC,e8"""
        if self.R.CARRY == 0:
            addr = (value ^ 0x80) - 0x80
            self.R.PC += addr
            return 12
        return 8

    def LD_31(self, value: int) -> int:
        """LD SP, n16"""
        self.R.SP = value
        return 12

    def LD_32(self) -> int:
        """LD [HLD],A"""
        self.mmu.set_memory(self.R.HL, self.R.A)
        self.R.HL = (self.R.HL - 1) & 0xFFFF
        return 8

    def INC_33(self) -> int:
        """INC SP"""
        self.R.SP = (self.R.SP + 1) & 0xFFFF
        return 8

    def INC_34(self) -> int:
        """INC [HL]"""
        initial = self.mmu.get_memory(self.R.HL)
        final = (initial + 1) & 0xFF
        self.mmu.set_memory(self.R.HL, final)
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + 1 > 0xF) & 1
        return 12

    def DEC_35(self) -> int:
        """DEC [HL]"""
        initial = self.mmu.get_memory(self.R.HL)
        final = (initial - 1) & 0xFF
        self.mmu.set_memory(self.R.HL, final)
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - 1 < 0) & 1
        return 12

    def LD_36(self, value: int) -> int:
        """LD [HL], n8"""
        self.mmu.set_memory(self.R.HL, value)
        return 12

    def SCF_37(self) -> int:
        """SCF"""
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 1
        return 4

    def JR_38(self, value: int) -> int:
        """JR C, e8"""
        if self.R.CARRY == 1:
            addr = (value ^ 0x80) - 0x80
            self.R.PC += addr
            return 12
        return 8

    def ADD_39(self) -> int:
        """ADD HL, SP"""
        calc = self.R.HL + self.R.SP
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.HL & 0xFFF) + (self.R.SP & 0xFFF) > 0xFFF) & 1
        self.R.CARRY = (calc > 0xFFFF) & 1
        self.R.HL = calc & 0xFFFF
        return 8

    def LD_3A(self) -> int:
        """LD A, [HLD]"""
        self.R.A = self.mmu.get_memory(self.R.HL)
        self.R.HL = (self.R.HL - 1) & 0xFFFF
        return 8

    def DEC_3B(self) -> int:
        """DEC SP"""
        self.R.SP = (self.R.SP - 1) & 0xFFFF
        return 8

    def INC_3C(self) -> int:
        """INC A"""
        calc = self.R.A + 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((self.R.A & 0xF) + 1 > 0xF) & 1
        calc &= 0xFF
        self.R.A = calc
        return 4

    def DEC_3D(self) -> int:
        """DEC A"""
        calc = self.R.A - 1
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - 1 < 0) & 1
        calc &= 0xFF
        self.R.A = calc
        return 4

    def LD_3E(self, value: int) -> int:
        """LD A, n8"""
        self.R.A = value
        return 8

    def CCF_3F(self) -> int:
        """CCF"""
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = (self.R.CARRY == 0) & 1
        return 4

    def LD_40(self) -> int:
        """LD B, B"""
        self.R.B = self.R.B
        return 4

    def LD_41(self) -> int:
        """LD B, C"""
        self.R.B = self.R.C
        return 4

    def LD_42(self) -> int:
        """LD B, D"""
        self.R.B = self.R.D
        return 4

    def LD_43(self) -> int:
        """LD B, E"""
        self.R.B = self.R.E
        return 4

    def LD_44(self) -> int:
        """LD B, H"""
        self.R.B = self.R.H
        return 4

    def LD_45(self) -> int:
        """LD B, L"""
        self.R.B = self.R.L
        return 4

    def LD_46(self) -> int:
        """LD B, [HL]"""
        self.R.B = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_47(self) -> int:
        """LD B, A"""
        self.R.B = self.R.A
        return 4

    def LD_48(self) -> int:
        """LD C, B"""
        self.R.C = self.R.B
        return 4

    def LD_49(self) -> int:
        """LD C, C"""
        self.R.C = self.R.C
        return 4

    def LD_4A(self) -> int:
        """LD C, D"""
        self.R.C = self.R.D
        return 4

    def LD_4B(self) -> int:
        """LD C, E"""
        self.R.C = self.R.E
        return 4

    def LD_4C(self) -> int:
        """LD C, H"""
        self.R.C = self.R.H
        return 4

    def LD_4D(self) -> int:
        """LD C, L"""
        self.R.C = self.R.L
        return 4

    def LD_4E(self) -> int:
        """LD C, [HL]"""
        self.R.C = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_4F(self) -> int:
        """LD C, A"""
        self.R.C = self.R.A
        return 4

    def LD_50(self) -> int:
        """LD D, B"""
        self.R.D = self.R.B
        return 4

    def LD_51(self) -> int:
        """LD D, C"""
        self.R.D = self.R.C
        return 4

    def LD_52(self) -> int:
        """LD D, D"""
        self.R.D = self.R.D
        return 4

    def LD_53(self) -> int:
        """LD D, E"""
        self.R.D = self.R.E
        return 4

    def LD_54(self) -> int:
        """LD D, H"""
        self.R.D = self.R.H
        return 4

    def LD_55(self) -> int:
        """LD D, L"""
        self.R.D = self.R.L
        return 4

    def LD_56(self) -> int:
        """LD D, [HL]"""
        self.R.D = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_57(self) -> int:
        """LD D, A"""
        self.R.D = self.R.A
        return 4

    def LD_58(self) -> int:
        """LD E, B"""
        self.R.E = self.R.B
        return 4

    def LD_59(self) -> int:
        """LD E, C"""
        self.R.E = self.R.C
        return 4

    def LD_5A(self) -> int:
        """LD E, D"""
        self.R.E = self.R.D
        return 4

    def LD_5B(self) -> int:
        """LD E, E"""
        self.R.E = self.R.E
        return 4

    def LD_5C(self) -> int:
        """LD E, H"""
        self.R.E = self.R.H
        return 4

    def LD_5D(self) -> int:
        """LD E, L"""
        self.R.E = self.R.L
        return 4

    def LD_5E(self) -> int:
        """LD E, [HL]"""
        self.R.E = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_5F(self) -> int:
        """LD E, A"""
        self.R.E = self.R.A
        return 4

    def LD_60(self) -> int:
        """LD H, B"""
        self.R.H = self.R.B
        return 4

    def LD_61(self) -> int:
        """LD H, C"""
        self.R.H = self.R.C
        return 4

    def LD_62(self) -> int:
        """LD H, D"""
        self.R.H = self.R.D
        return 4

    def LD_63(self) -> int:
        """LD H, E"""
        self.R.H = self.R.E
        return 4

    def LD_64(self) -> int:
        """LD H, H"""
        self.R.H = self.R.H
        return 4

    def LD_65(self) -> int:
        """LD H, L"""
        self.R.H = self.R.L
        return 4

    def LD_66(self) -> int:
        """LD H, [HL]"""
        self.R.H = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_67(self) -> int:
        """LD H, A"""
        self.R.H = self.R.A
        return 4

    def LD_68(self) -> int:
        """LD L, B"""
        self.R.L = self.R.B
        return 4

    def LD_69(self) -> int:
        """LD L, C"""
        self.R.L = self.R.C
        return 4

    def LD_6A(self) -> int:
        """LD L, D"""
        self.R.L = self.R.D
        return 4

    def LD_6B(self) -> int:
        """LD L, E"""
        self.R.L = self.R.E
        return 4

    def LD_6C(self) -> int:
        """LD L, H"""
        self.R.L = self.R.H
        return 4

    def LD_6D(self) -> int:
        """LD L, L"""
        self.R.L = self.R.L
        return 4

    def LD_6E(self) -> int:
        """LD L, [HL]"""
        self.R.L = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_6F(self) -> int:
        """LD L, A"""
        self.R.L = self.R.A
        return 4

    def LD_70(self) -> int:
        """LD [HL], B"""
        self.mmu.set_memory(self.R.HL, self.R.B)
        return 8

    def LD_71(self) -> int:
        """LD [HL], C"""
        self.mmu.set_memory(self.R.HL, self.R.C)
        return 8

    def LD_72(self) -> int:
        """LD [HL], D"""
        self.mmu.set_memory(self.R.HL, self.R.D)
        return 8

    def LD_73(self) -> int:
        """LD [HL], E"""
        self.mmu.set_memory(self.R.HL, self.R.E)
        return 8

    def LD_74(self) -> int:
        """LD [HL], H"""
        self.mmu.set_memory(self.R.HL, self.R.H)
        return 8

    def LD_75(self) -> int:
        """LD [HL], L"""
        self.mmu.set_memory(self.R.HL, self.R.L)
        return 8

    def HALT_76(self) -> int:
        """HALT"""
        self.mmu.HALT = True
        return 4

    def LD_77(self) -> int:
        """LD [HL], A"""
        self.mmu.set_memory(self.R.HL, self.R.A)
        return 8

    def LD_78(self) -> int:
        """LD A, B"""
        self.R.A = self.R.B
        return 4

    def LD_79(self) -> int:
        """LD A, C"""
        self.R.A = self.R.C
        return 4

    def LD_7A(self) -> int:
        """LD A, D"""
        self.R.A = self.R.D
        return 4

    def LD_7B(self) -> int:
        """LD A, E"""
        self.R.A = self.R.E
        return 4

    def LD_7C(self) -> int:
        """LD A, H"""
        self.R.A = self.R.H
        return 4

    def LD_7D(self) -> int:
        """LD A, L"""
        self.R.A = self.R.L
        return 4

    def LD_7E(self) -> int:
        """LD A, [HL]"""
        self.R.A = self.mmu.get_memory(self.R.HL)
        return 8

    def LD_7F(self) -> int:
        """LD A, A"""
        self.R.A = self.R.A
        return 4

    def ADD_80(self) -> int:
        """ADD A, B"""
        initial = self.R.A
        calc = initial + self.R.B
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.B & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADD_81(self) -> int:
        """ADD A, C"""
        initial = self.R.A
        calc = initial + self.R.C
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.C & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADD_82(self) -> int:
        """ADD A, D"""
        initial = self.R.A
        calc = initial + self.R.D
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.D & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADD_83(self) -> int:
        """ADD A, E"""
        initial = self.R.A
        calc = initial + self.R.E
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.E & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADD_84(self) -> int:
        """ADD A, H"""
        initial = self.R.A
        calc = initial + self.R.H
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.H & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADD_85(self) -> int:
        """ADD A, L"""
        initial = self.R.A
        calc = initial + self.R.L
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.L & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADD_86(self) -> int:
        """ADD A, [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        initial = self.R.A
        calc = initial + mem
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (mem & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 8

    def ADD_87(self) -> int:
        """ADD A, A"""
        initial = self.R.A
        calc = initial + self.R.A
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (self.R.A & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_88(self) -> int:
        """ADC A, B"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.B + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.B & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_89(self) -> int:
        """ADC A, C"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.C + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.C & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_8A(self) -> int:
        """ADC A, D"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.D + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.D & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_8B(self) -> int:
        """ADC A, E"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.E + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.E & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_8C(self) -> int:
        """ADC A, H"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.H + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.H & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_8D(self) -> int:
        """ADC A, L"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.L + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.L & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def ADC_8E(self) -> int:
        """ADC A, [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + mem + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (mem & 0xF) + (carryBit & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 8

    def ADC_8F(self) -> int:
        """ADC A, A"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + self.R.A + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (self.R.A & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 4

    def SUB_90(self) -> int:
        """SUB A, B"""
        initial = self.R.A
        calc = initial - self.R.B
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.B & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SUB_91(self) -> int:
        """SUB A, C"""
        initial = self.R.A
        calc = initial - self.R.C
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.C & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SUB_92(self) -> int:
        """SUB A, D"""
        initial = self.R.A
        calc = initial - self.R.D
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.D & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SUB_93(self) -> int:
        """SUB A, E"""
        initial = self.R.A
        calc = initial - self.R.E
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.E & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SUB_94(self) -> int:
        """SUB A, H"""
        initial = self.R.A
        calc = initial - self.R.H
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.H & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SUB_95(self) -> int:
        """SUB A, L"""
        initial = self.R.A
        calc = initial - self.R.L
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.L & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SUB_96(self) -> int:
        """SUB A, [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        initial = self.R.A
        calc = initial - mem
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (mem & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 8

    def SUB_97(self) -> int:
        """SUB A, A"""
        initial = self.R.A
        calc = initial - self.R.A
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (self.R.A & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_98(self) -> int:
        """SBC A, B"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.B + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.B & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_99(self) -> int:
        """SBC A, C"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.C + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.C & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_9A(self) -> int:
        """SBC A, D"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.D + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.D & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_9B(self) -> int:
        """SBC A, E"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.E + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.E & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_9C(self) -> int:
        """SBC A, H"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.H + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.H & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_9D(self) -> int:
        """SBC A, L"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.L + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.L & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def SBC_9E(self) -> int:
        """SBC A, [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (mem + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - ((mem & 0xF) + (carryBit & 0xF)) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 8

    def SBC_9F(self) -> int:
        """SBC A, A"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (self.R.A + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((self.R.A & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def AND_A0(self) -> int:
        """AND A, B"""
        initial = self.R.A
        calc = initial & self.R.B
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def AND_A1(self) -> int:
        """AND A, C"""
        initial = self.R.A
        calc = initial & self.R.C
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def AND_A2(self) -> int:
        """AND A, D"""
        initial = self.R.A
        calc = initial & self.R.D
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def AND_A3(self) -> int:
        """AND A, E"""
        initial = self.R.A
        calc = initial & self.R.E
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def AND_A4(self) -> int:
        """AND A, H"""
        initial = self.R.A
        calc = initial & self.R.H
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def AND_A5(self) -> int:
        """AND A, L"""
        initial = self.R.A
        calc = initial & self.R.L
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def AND_A6(self) -> int:
        """AND A, [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        initial = self.R.A
        calc = initial & mem
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 8

    def AND_A7(self) -> int:
        """AND A, A"""
        initial = self.R.A
        calc = initial & self.R.A
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 4

    def XOR_A8(self) -> int:
        """XOR A, B"""
        calc = self.R.A ^ self.R.B
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def XOR_A9(self) -> int:
        """XOR A, C"""
        calc = self.R.A ^ self.R.C
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def XOR_AA(self) -> int:
        """XOR A, D"""
        calc = self.R.A ^ self.R.D
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def XOR_AB(self) -> int:
        """XOR A, E"""
        calc = self.R.A ^ self.R.E
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def XOR_AC(self) -> int:
        """XOR A, H"""
        calc = self.R.A ^ self.R.H
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def XOR_AD(self) -> int:
        """XOR A, L"""
        calc = self.R.A ^ self.R.L
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def XOR_AE(self) -> int:
        """XOR A, [HL]"""
        calc = self.R.A ^ self.mmu.get_memory(self.R.HL)
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 8

    def XOR_AF(self) -> int:
        """XOR A, A"""
        calc = self.R.A ^ self.R.A
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B0(self) -> int:
        """OR A, B"""
        calc = self.R.A | self.R.B
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B1(self) -> int:
        """OR A, C"""
        calc = self.R.A | self.R.C
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B2(self) -> int:
        """OR A, D"""
        calc = self.R.A | self.R.D
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B3(self) -> int:
        """OR A, E"""
        calc = self.R.A | self.R.E
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B4(self) -> int:
        """OR A, H"""
        calc = self.R.A | self.R.H
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B5(self) -> int:
        """OR A, L"""
        calc = self.R.A | self.R.L
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def OR_B6(self) -> int:
        """OR A, [HL]"""
        calc = self.R.A | self.mmu.get_memory(self.R.HL)
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 8

    def OR_B7(self) -> int:
        """OR A, A"""
        calc = self.R.A | self.R.A
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 4

    def CP_B8(self) -> int:
        """CP A, B"""
        calc = self.R.A - self.R.B
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.B & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def CP_B9(self) -> int:
        """CP A, C"""
        calc = self.R.A - self.R.C
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.C & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def CP_BA(self) -> int:
        """CP A, D"""
        calc = self.R.A - self.R.D
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.D & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def CP_BB(self) -> int:
        """CP A, E"""
        calc = self.R.A - self.R.E
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.E & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def CP_BC(self) -> int:
        """CP A, H"""
        calc = self.R.A - self.R.H
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.H & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def CP_BD(self) -> int:
        """CP A, L"""
        calc = self.R.A - self.R.L
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.L & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def CP_BE(self) -> int:
        """CP A, [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        calc = self.R.A - mem
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (mem & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 8

    def CP_BF(self) -> int:
        """CP A, A"""
        calc = self.R.A - self.R.A
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (self.R.A & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 4

    def RET_C0(self) -> int:
        """RET NZ"""
        if self.R.ZERO == 0:
            self.JP_C3(self.R.POP())
            return 20
        return 8

    def POP_C1(self) -> int:
        """POP BC"""
        self.R.BC = self.R.POP()
        return 12

    def JP_C2(self, address: int) -> int:
        """JP NZ,n16"""
        if self.R.ZERO == 0:
            self.R.PC = address
            return 16
        return 12

    def JP_C3(self, address: int) -> int:
        """JP n16"""
        self.R.PC = address
        return 16

    def CALL_C4(self, address: int) -> int:
        """CALL NZ,n16"""
        if self.R.ZERO == 0:
            self.R.PUSH(self.R.PC)
            self.R.PC = address
            return 24
        return 12

    def PUSH_C5(self) -> int:
        """PUSH BC"""
        self.R.PUSH(self.R.BC)
        return 16

    def ADD_C6(self, value: int) -> int:
        """ADD A, n8"""
        initial = self.R.A
        calc = initial + value
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = ((initial & 0xF) + (value & 0xF) > 0xF) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 8

    def RST_C7(self) -> int:
        """RST $00"""
        self.CALL_CD(0x00)
        return 16

    def RET_C8(self) -> int:
        """RET Z"""
        if self.R.ZERO == 1:
            self.R.PC = self.R.POP()
            return 20
        return 8

    def RET_C9(self) -> int:
        """RET"""
        self.R.PC = self.R.POP()
        return 16

    def JP_CA(self, address: int) -> int:
        """JP Z,n16"""
        if self.R.ZERO == 1:
            self.R.PC = address
            return 16
        return 12

    def RLC_CB00(self) -> int:
        """RLC B"""
        carryBit = self.R.B >> 7
        calc = (self.R.B << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def RLC_CB01(self) -> int:
        """RLC C"""
        carryBit = self.R.C >> 7
        calc = (self.R.C << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def RLC_CB02(self) -> int:
        """RLC D"""
        carryBit = self.R.D >> 7
        calc = (self.R.D << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def RLC_CB03(self) -> int:
        """RLC E"""
        carryBit = self.R.E >> 7
        calc = (self.R.E << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def RLC_CB04(self) -> int:
        """RLC H"""
        carryBit = self.R.H >> 7
        calc = (self.R.H << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def RLC_CB05(self) -> int:
        """RLC L"""
        carryBit = self.R.L >> 7
        calc = (self.R.L << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def RLC_CB06(self) -> int:
        """RLC [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem >> 7
        calc = (mem << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RLC_CB07(self) -> int:
        """RLC A"""
        carryBit = self.R.A >> 7
        calc = (self.R.A << 1) & 0b11111110 | carryBit
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def RRC_CB08(self) -> int:
        """RRC B"""
        carryBit = self.R.B & 1
        calc = (carryBit << 7) | self.R.B >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def RRC_CB09(self) -> int:
        """RRC C"""
        carryBit = self.R.C & 1
        calc = (carryBit << 7) | self.R.C >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def RRC_CB0A(self) -> int:
        """RRC D"""
        carryBit = self.R.D & 1
        calc = (carryBit << 7) | self.R.D >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def RRC_CB0B(self) -> int:
        """RRC E"""
        carryBit = self.R.E & 1
        calc = (carryBit << 7) | self.R.E >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def RRC_CB0C(self) -> int:
        """RRC H"""
        carryBit = self.R.H & 1
        calc = (carryBit << 7) | self.R.H >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def RRC_CB0D(self) -> int:
        """RRC L"""
        carryBit = self.R.L & 1
        calc = (carryBit << 7) | self.R.L >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def RRC_CB0E(self) -> int:
        """RRC [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem & 1
        calc = (carryBit << 7) | mem >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RRC_CB0F(self) -> int:
        """RRC A"""
        carryBit = self.R.A & 1
        calc = (carryBit << 7) | self.R.A >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def RL_CB10(self) -> int:
        """RL B"""
        carryBit = self.R.B >> 7
        calc = (self.R.B << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def RL_CB11(self) -> int:
        """RL C"""
        carryBit = self.R.C >> 7
        calc = (self.R.C << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def RL_CB12(self) -> int:
        """RL D"""
        carryBit = self.R.D >> 7
        calc = (self.R.D << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def RL_CB13(self) -> int:
        """RL E"""
        carryBit = self.R.E >> 7
        calc = (self.R.E << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def RL_CB14(self) -> int:
        """RL H"""
        carryBit = self.R.H >> 7
        calc = (self.R.H << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def RL_CB15(self) -> int:
        """RL L"""
        carryBit = self.R.L >> 7
        calc = (self.R.L << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def RL_CB16(self) -> int:
        """RL [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem >> 7
        calc = (mem << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RL_CB17(self) -> int:
        """RL A"""
        carryBit = self.R.A >> 7
        calc = (self.R.A << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def RR_CB18(self) -> int:
        """RR B"""
        carryBit = self.R.B & 1
        calc = (self.R.CARRY << 7) | self.R.B >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def RR_CB19(self) -> int:
        """RR C"""
        carryBit = self.R.C & 1
        calc = (self.R.CARRY << 7) | self.R.C >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def RR_CB1A(self) -> int:
        """RR D"""
        carryBit = self.R.D & 1
        calc = (self.R.CARRY << 7) | self.R.D >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def RR_CB1B(self) -> int:
        """RR E"""
        carryBit = self.R.E & 1
        calc = (self.R.CARRY << 7) | self.R.E >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def RR_CB1C(self) -> int:
        """RR H"""
        carryBit = self.R.H & 1
        calc = (self.R.CARRY << 7) | self.R.H >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def RR_CB1D(self) -> int:
        """RR L"""
        carryBit = self.R.L & 1
        calc = (self.R.CARRY << 7) | self.R.L >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def RR_CB1E(self) -> int:
        """RR [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem & 1
        calc = (self.R.CARRY << 7) | mem >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RR_CB1F(self) -> int:
        """RR A"""
        carryBit = self.R.A & 1
        calc = (self.R.CARRY << 7) | self.R.A >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def SLA_CB20(self) -> int:
        """SLA B"""
        carryBit = self.R.B >> 7
        calc = (self.R.B << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def SLA_CB21(self) -> int:
        """SLA C"""
        carryBit = self.R.C >> 7
        calc = (self.R.C << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def SLA_CB22(self) -> int:
        """SLA D"""
        carryBit = self.R.D >> 7
        calc = (self.R.D << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def SLA_CB23(self) -> int:
        """SLA E"""
        carryBit = self.R.E >> 7
        calc = (self.R.E << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def SLA_CB24(self) -> int:
        """SLA H"""
        carryBit = self.R.H >> 7
        calc = (self.R.H << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def SLA_CB25(self) -> int:
        """SLA L"""
        carryBit = self.R.L >> 7
        calc = (self.R.L << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def SLA_CB26(self) -> int:
        """SLA [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem >> 7
        calc = (mem << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SLA_CB27(self) -> int:
        """SLA A"""
        carryBit = self.R.A >> 7
        calc = (self.R.A << 1) & 0b11111110
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def SRA_CB28(self) -> int:
        """SRA B"""
        carryBit = self.R.B & 1
        calc = (self.R.B >> 7) << 7 | self.R.B >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def SRA_CB29(self) -> int:
        """SRA C"""
        carryBit = self.R.C & 1
        calc = (self.R.C >> 7) << 7 | self.R.C >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def SRA_CB2A(self) -> int:
        """SRA D"""
        carryBit = self.R.D & 1
        calc = (self.R.D >> 7) << 7 | self.R.D >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def SRA_CB2B(self) -> int:
        """SRA E"""
        carryBit = self.R.E & 1
        calc = (self.R.E >> 7) << 7 | self.R.E >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def SRA_CB2C(self) -> int:
        """SRA H"""
        carryBit = self.R.H & 1
        calc = (self.R.H >> 7) << 7 | self.R.H >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def SRA_CB2D(self) -> int:
        """SRA L"""
        carryBit = self.R.L & 1
        calc = (self.R.L >> 7) << 7 | self.R.L >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def SRA_CB2E(self) -> int:
        """SRA [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem & 1
        calc = (mem >> 7) << 7 | mem >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SRA_CB2F(self) -> int:
        """SRA A"""
        carryBit = self.R.A & 1
        calc = (self.R.A >> 7) << 7 | self.R.A >> 1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def SWAP_CB30(self) -> int:
        """SWAP B"""
        calc = (self.R.B & 0b1111) << 4 | (self.R.B >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.B = calc
        return 8

    def SWAP_CB31(self) -> int:
        """SWAP C"""
        calc = (self.R.C & 0b1111) << 4 | (self.R.C >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.C = calc
        return 8

    def SWAP_CB32(self) -> int:
        """SWAP D"""
        calc = (self.R.D & 0b1111) << 4 | (self.R.D >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.D = calc
        return 8

    def SWAP_CB33(self) -> int:
        """SWAP E"""
        calc = (self.R.E & 0b1111) << 4 | (self.R.E >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.E = calc
        return 8

    def SWAP_CB34(self) -> int:
        """SWAP H"""
        calc = (self.R.H & 0b1111) << 4 | (self.R.H >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.H = calc
        return 8

    def SWAP_CB35(self) -> int:
        """SWAP L"""
        calc = (self.R.L & 0b1111) << 4 | (self.R.L >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.L = calc
        return 8

    def SWAP_CB36(self) -> int:
        """SWAP [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        calc = (mem & 0b1111) << 4 | (mem >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SWAP_CB37(self) -> int:
        """SWAP A"""
        calc = (self.R.A & 0b1111) << 4 | (self.R.A >> 4)
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        self.R.A = calc
        return 8

    def SRL_CB38(self) -> int:
        """SRL B"""
        carryBit = self.R.B & 1
        calc = self.R.B >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.B = calc
        return 8

    def SRL_CB39(self) -> int:
        """SRL C"""
        carryBit = self.R.C & 1
        calc = self.R.C >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.C = calc
        return 8

    def SRL_CB3A(self) -> int:
        """SRL D"""
        carryBit = self.R.D & 1
        calc = self.R.D >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.D = calc
        return 8

    def SRL_CB3B(self) -> int:
        """SRL E"""
        carryBit = self.R.E & 1
        calc = self.R.E >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.E = calc
        return 8

    def SRL_CB3C(self) -> int:
        """SRL H"""
        carryBit = self.R.H & 1
        calc = self.R.H >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.H = calc
        return 8

    def SRL_CB3D(self) -> int:
        """SRL L"""
        carryBit = self.R.L & 1
        calc = self.R.L >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.L = calc
        return 8

    def SRL_CB3E(self) -> int:
        """SRL [HL]"""
        mem = self.mmu.get_memory(self.R.HL)
        carryBit = mem & 1
        calc = mem >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SRL_CB3F(self) -> int:
        """SRL A"""
        carryBit = self.R.A & 1
        calc = self.R.A >> 1 & 0b011111111
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        self.R.A = calc
        return 8

    def BIT_CB40(self) -> int:
        """BIT 0,B"""
        value = 0
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB41(self) -> int:
        """BIT 0,C"""
        value = 0
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB42(self) -> int:
        """BIT 0,D"""
        value = 0
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB43(self) -> int:
        """BIT 0,E"""
        value = 0
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB44(self) -> int:
        """BIT 0,H"""
        value = 0
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB45(self) -> int:
        """BIT 0,L"""
        value = 0
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB46(self) -> int:
        """BIT 0,[HL]"""
        value = 0
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB47(self) -> int:
        """BIT 0,A"""
        value = 0
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB48(self) -> int:
        """BIT 1,B"""
        value = 1
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB49(self) -> int:
        """BIT 1,C"""
        value = 1
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB4A(self) -> int:
        """BIT 1,D"""
        value = 1
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB4B(self) -> int:
        """BIT 1,E"""
        value = 1
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB4C(self) -> int:
        """BIT 1,H"""
        value = 1
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB4D(self) -> int:
        """BIT 1,L"""
        value = 1
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB4E(self) -> int:
        """BIT 1,[HL]"""
        value = 1
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB4F(self) -> int:
        """BIT 1,A"""
        value = 1
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB50(self) -> int:
        """BIT 2,B"""
        value = 2
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB51(self) -> int:
        """BIT 2,C"""
        value = 2
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB52(self) -> int:
        """BIT 2,D"""
        value = 2
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB53(self) -> int:
        """BIT 2,E"""
        value = 2
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB54(self) -> int:
        """BIT 2,H"""
        value = 2
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB55(self) -> int:
        """BIT 2,L"""
        value = 2
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB56(self) -> int:
        """BIT 2,[HL]"""
        value = 2
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB57(self) -> int:
        """BIT 2,A"""
        value = 2
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB58(self) -> int:
        """BIT 3,B"""
        value = 3
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB59(self) -> int:
        """BIT 3,C"""
        value = 3
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB5A(self) -> int:
        """BIT 3,D"""
        value = 3
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB5B(self) -> int:
        """BIT 3,E"""
        value = 3
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB5C(self) -> int:
        """BIT 3,H"""
        value = 3
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB5D(self) -> int:
        """BIT 3,L"""
        value = 3
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB5E(self) -> int:
        """BIT 3,[HL]"""
        value = 3
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB5F(self) -> int:
        """BIT 3,A"""
        value = 3
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB60(self) -> int:
        """BIT 4,B"""
        value = 4
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB61(self) -> int:
        """BIT 4,C"""
        value = 4
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB62(self) -> int:
        """BIT 4,D"""
        value = 4
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB63(self) -> int:
        """BIT 4,E"""
        value = 4
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB64(self) -> int:
        """BIT 4,H"""
        value = 4
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB65(self) -> int:
        """BIT 4,L"""
        value = 4
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB66(self) -> int:
        """BIT 4,[HL]"""
        value = 4
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB67(self) -> int:
        """BIT 4,A"""
        value = 4
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB68(self) -> int:
        """BIT 5,B"""
        value = 5
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB69(self) -> int:
        """BIT 5,C"""
        value = 5
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB6A(self) -> int:
        """BIT 5,D"""
        value = 5
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB6B(self) -> int:
        """BIT 5,E"""
        value = 5
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB6C(self) -> int:
        """BIT 5,H"""
        value = 5
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB6D(self) -> int:
        """BIT 5,L"""
        value = 5
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB6E(self) -> int:
        """BIT 5,[HL]"""
        value = 5
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB6F(self) -> int:
        """BIT 5,A"""
        value = 5
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB70(self) -> int:
        """BIT 6,B"""
        value = 6
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB71(self) -> int:
        """BIT 6,C"""
        value = 6
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB72(self) -> int:
        """BIT 6,D"""
        value = 6
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB73(self) -> int:
        """BIT 6,E"""
        value = 6
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB74(self) -> int:
        """BIT 6,H"""
        value = 6
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB75(self) -> int:
        """BIT 6,L"""
        value = 6
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB76(self) -> int:
        """BIT 6,[HL]"""
        value = 6
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB77(self) -> int:
        """BIT 6,A"""
        value = 6
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB78(self) -> int:
        """BIT 7,B"""
        value = 7
        calc = self.R.B >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB79(self) -> int:
        """BIT 7,C"""
        value = 7
        calc = self.R.C >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB7A(self) -> int:
        """BIT 7,D"""
        value = 7
        calc = self.R.D >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB7B(self) -> int:
        """BIT 7,E"""
        value = 7
        calc = self.R.E >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB7C(self) -> int:
        """BIT 7,H"""
        value = 7
        calc = self.R.H >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB7D(self) -> int:
        """BIT 7,L"""
        value = 7
        calc = self.R.L >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def BIT_CB7E(self) -> int:
        """BIT 7,[HL]"""
        value = 7
        calc = self.mmu.get_memory(self.R.HL) >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 12

    def BIT_CB7F(self) -> int:
        """BIT 7,A"""
        value = 7
        calc = self.R.A >> (value) & 0b1
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        return 8

    def RES_CB80(self) -> int:
        """RES 0,B"""
        value = 0
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CB81(self) -> int:
        """RES 0,C"""
        value = 0
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CB82(self) -> int:
        """RES 0,D"""
        value = 0
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CB83(self) -> int:
        """RES 0,E"""
        value = 0
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CB84(self) -> int:
        """RES 0,H"""
        value = 0
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CB85(self) -> int:
        """RES 0,L"""
        value = 0
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CB86(self) -> int:
        """RES 0,[HL]"""
        value = 0
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CB87(self) -> int:
        """RES 0,A"""
        value = 0
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CB88(self) -> int:
        """RES 1,B"""
        value = 1
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CB89(self) -> int:
        """RES 1,C"""
        value = 1
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CB8A(self) -> int:
        """RES 1,D"""
        value = 1
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CB8B(self) -> int:
        """RES 1,E"""
        value = 1
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CB8C(self) -> int:
        """RES 1,H"""
        value = 1
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CB8D(self) -> int:
        """RES 1,L"""
        value = 1
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CB8E(self) -> int:
        """RES 1,[HL]"""
        value = 1
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CB8F(self) -> int:
        """RES 1,A"""
        value = 1
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CB90(self) -> int:
        """RES 2,B"""
        value = 2
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CB91(self) -> int:
        """RES 2,C"""
        value = 2
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CB92(self) -> int:
        """RES 2,D"""
        value = 2
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CB93(self) -> int:
        """RES 2,E"""
        value = 2
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CB94(self) -> int:
        """RES 2,H"""
        value = 2
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CB95(self) -> int:
        """RES 2,L"""
        value = 2
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CB96(self) -> int:
        """RES 2,[HL]"""
        value = 2
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CB97(self) -> int:
        """RES 2,A"""
        value = 2
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CB98(self) -> int:
        """RES 3,B"""
        value = 3
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CB99(self) -> int:
        """RES 3,C"""
        value = 3
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CB9A(self) -> int:
        """RES 3,D"""
        value = 3
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CB9B(self) -> int:
        """RES 3,E"""
        value = 3
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CB9C(self) -> int:
        """RES 3,H"""
        value = 3
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CB9D(self) -> int:
        """RES 3,L"""
        value = 3
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CB9E(self) -> int:
        """RES 3,[HL]"""
        value = 3
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CB9F(self) -> int:
        """RES 3,A"""
        value = 3
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CBA0(self) -> int:
        """RES 4,B"""
        value = 4
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CBA1(self) -> int:
        """RES 4,C"""
        value = 4
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CBA2(self) -> int:
        """RES 4,D"""
        value = 4
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CBA3(self) -> int:
        """RES 4,E"""
        value = 4
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CBA4(self) -> int:
        """RES 4,H"""
        value = 4
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CBA5(self) -> int:
        """RES 4,L"""
        value = 4
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CBA6(self) -> int:
        """RES 4,[HL]"""
        value = 4
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CBA7(self) -> int:
        """RES 4,A"""
        value = 4
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CBA8(self) -> int:
        """RES 5,B"""
        value = 5
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CBA9(self) -> int:
        """RES 5,C"""
        value = 5
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CBAA(self) -> int:
        """RES 5,D"""
        value = 5
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CBAB(self) -> int:
        """RES 5,E"""
        value = 5
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CBAC(self) -> int:
        """RES 5,H"""
        value = 5
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CBAD(self) -> int:
        """RES 5,L"""
        value = 5
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CBAE(self) -> int:
        """RES 5,[HL]"""
        value = 5
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CBAF(self) -> int:
        """RES 5,A"""
        value = 5
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CBB0(self) -> int:
        """RES 6,B"""
        value = 6
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CBB1(self) -> int:
        """RES 6,C"""
        value = 6
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CBB2(self) -> int:
        """RES 6,D"""
        value = 6
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CBB3(self) -> int:
        """RES 6,E"""
        value = 6
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CBB4(self) -> int:
        """RES 6,H"""
        value = 6
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CBB5(self) -> int:
        """RES 6,L"""
        value = 6
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CBB6(self) -> int:
        """RES 6,[HL]"""
        value = 6
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CBB7(self) -> int:
        """RES 6,A"""
        value = 6
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def RES_CBB8(self) -> int:
        """RES 7,B"""
        value = 7
        higher = self.R.B >> value + 1 << value + 1
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def RES_CBB9(self) -> int:
        """RES 7,C"""
        value = 7
        higher = self.R.C >> value + 1 << value + 1
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def RES_CBBA(self) -> int:
        """RES 7,D"""
        value = 7
        higher = self.R.D >> value + 1 << value + 1
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def RES_CBBB(self) -> int:
        """RES 7,E"""
        value = 7
        higher = self.R.E >> value + 1 << value + 1
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def RES_CBBC(self) -> int:
        """RES 7,H"""
        value = 7
        higher = self.R.H >> value + 1 << value + 1
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def RES_CBBD(self) -> int:
        """RES 7,L"""
        value = 7
        higher = self.R.L >> value + 1 << value + 1
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def RES_CBBE(self) -> int:
        """RES 7,[HL]"""
        value = 7
        mem = self.mmu.get_memory(self.R.HL)
        higher = mem >> value + 1 << value + 1
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def RES_CBBF(self) -> int:
        """RES 7,A"""
        value = 7
        higher = self.R.A >> value + 1 << value + 1
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBC0(self) -> int:
        """SET 0,B"""
        value = 0
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBC1(self) -> int:
        """SET 0,C"""
        value = 0
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBC2(self) -> int:
        """SET 0,D"""
        value = 0
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBC3(self) -> int:
        """SET 0,E"""
        value = 0
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBC4(self) -> int:
        """SET 0,H"""
        value = 0
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBC5(self) -> int:
        """SET 0,L"""
        value = 0
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBC6(self) -> int:
        """SET 0,[HL]"""
        value = 0
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBC7(self) -> int:
        """SET 0,A"""
        value = 0
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBC8(self) -> int:
        """SET 1,B"""
        value = 1
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBC9(self) -> int:
        """SET 1,C"""
        value = 1
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBCA(self) -> int:
        """SET 1,D"""
        value = 1
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBCB(self) -> int:
        """SET 1,E"""
        value = 1
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBCC(self) -> int:
        """SET 1,H"""
        value = 1
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBCD(self) -> int:
        """SET 1,L"""
        value = 1
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBCE(self) -> int:
        """SET 1,[HL]"""
        value = 1
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBCF(self) -> int:
        """SET 1,A"""
        value = 1
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBD0(self) -> int:
        """SET 2,B"""
        value = 2
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBD1(self) -> int:
        """SET 2,C"""
        value = 2
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBD2(self) -> int:
        """SET 2,D"""
        value = 2
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBD3(self) -> int:
        """SET 2,E"""
        value = 2
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBD4(self) -> int:
        """SET 2,H"""
        value = 2
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBD5(self) -> int:
        """SET 2,L"""
        value = 2
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBD6(self) -> int:
        """SET 2,[HL]"""
        value = 2
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBD7(self) -> int:
        """SET 2,A"""
        value = 2
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBD8(self) -> int:
        """SET 3,B"""
        value = 3
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBD9(self) -> int:
        """SET 3,C"""
        value = 3
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBDA(self) -> int:
        """SET 3,D"""
        value = 3
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBDB(self) -> int:
        """SET 3,E"""
        value = 3
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBDC(self) -> int:
        """SET 3,H"""
        value = 3
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBDD(self) -> int:
        """SET 3,L"""
        value = 3
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBDE(self) -> int:
        """SET 3,[HL]"""
        value = 3
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBDF(self) -> int:
        """SET 3,A"""
        value = 3
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBE0(self) -> int:
        """SET 4,B"""
        value = 4
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBE1(self) -> int:
        """SET 4,C"""
        value = 4
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBE2(self) -> int:
        """SET 4,D"""
        value = 4
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBE3(self) -> int:
        """SET 4,E"""
        value = 4
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBE4(self) -> int:
        """SET 4,H"""
        value = 4
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBE5(self) -> int:
        """SET 4,L"""
        value = 4
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBE6(self) -> int:
        """SET 4,[HL]"""
        value = 4
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBE7(self) -> int:
        """SET 4,A"""
        value = 4
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBE8(self) -> int:
        """SET 5,B"""
        value = 5
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBE9(self) -> int:
        """SET 5,C"""
        value = 5
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBEA(self) -> int:
        """SET 5,D"""
        value = 5
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBEB(self) -> int:
        """SET 5,E"""
        value = 5
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBEC(self) -> int:
        """SET 5,H"""
        value = 5
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBED(self) -> int:
        """SET 5,L"""
        value = 5
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBEE(self) -> int:
        """SET 5,[HL]"""
        value = 5
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBEF(self) -> int:
        """SET 5,A"""
        value = 5
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBF0(self) -> int:
        """SET 6,B"""
        value = 6
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBF1(self) -> int:
        """SET 6,C"""
        value = 6
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBF2(self) -> int:
        """SET 6,D"""
        value = 6
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBF3(self) -> int:
        """SET 6,E"""
        value = 6
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBF4(self) -> int:
        """SET 6,H"""
        value = 6
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBF5(self) -> int:
        """SET 6,L"""
        value = 6
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBF6(self) -> int:
        """SET 6,[HL]"""
        value = 6
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBF7(self) -> int:
        """SET 6,A"""
        value = 6
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def SET_CBF8(self) -> int:
        """SET 7,B"""
        value = 7
        higher = ((self.R.B >> value) | 1) << value
        lower = ((self.R.B << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.B = calc
        return 8

    def SET_CBF9(self) -> int:
        """SET 7,C"""
        value = 7
        higher = ((self.R.C >> value) | 1) << value
        lower = ((self.R.C << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.C = calc
        return 8

    def SET_CBFA(self) -> int:
        """SET 7,D"""
        value = 7
        higher = ((self.R.D >> value) | 1) << value
        lower = ((self.R.D << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.D = calc
        return 8

    def SET_CBFB(self) -> int:
        """SET 7,E"""
        value = 7
        higher = ((self.R.E >> value) | 1) << value
        lower = ((self.R.E << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.E = calc
        return 8

    def SET_CBFC(self) -> int:
        """SET 7,H"""
        value = 7
        higher = ((self.R.H >> value) | 1) << value
        lower = ((self.R.H << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.H = calc
        return 8

    def SET_CBFD(self) -> int:
        """SET 7,L"""
        value = 7
        higher = ((self.R.L >> value) | 1) << value
        lower = ((self.R.L << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.L = calc
        return 8

    def SET_CBFE(self) -> int:
        """SET 7,[HL]"""
        value = 7
        mem = self.mmu.get_memory(self.R.HL)
        higher = ((mem >> value) | 1) << value
        lower = ((mem << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.mmu.set_memory(self.R.HL, calc)
        return 16

    def SET_CBFF(self) -> int:
        """SET 7,A"""
        value = 7
        higher = ((self.R.A >> value) | 1) << value
        lower = ((self.R.A << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        self.R.A = calc
        return 8

    def CALL_CC(self, value: int) -> int:
        """CALL Z,n16"""
        if self.R.ZERO == 1:
            self.R.PUSH(self.R.PC)
            self.R.PC = value
            return 24
        return 12

    def CALL_CD(self, address: int) -> int:
        """CALL n16"""
        self.R.PUSH(self.R.PC)
        # NOTE: Must ensure PC is currently the address after CALL
        self.R.PC = address
        return 24

    def ADC_CE(self, value: int) -> int:
        """ADC A, n8"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial + value + carryBit
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            (initial & 0xF) + (value & 0xF) + (carryBit & 0xF) > 0xF
        ) & 1
        self.R.CARRY = (calc > 0xFF) & 1
        return 8

    def RST_CF(self) -> int:
        """RST $08"""
        self.CALL_CD(0x08)
        return 16

    def RET_D0(self) -> int:
        """RET NC"""
        if self.R.CARRY == 0:
            self.R.PC = self.R.POP()
            return 20
        return 8

    def POP_D1(self) -> int:
        """POP DE"""
        self.R.DE = self.R.POP()
        return 12

    def JP_D2(self, address: int) -> int:
        """JP NC,n16"""
        if self.R.CARRY == 0:
            self.R.PC = address
            return 16
        return 12

    def CALL_D4(self, address: int) -> int:
        """CALL NC,n16"""
        if self.R.CARRY == 0:
            self.R.PUSH(self.R.PC)
            self.R.PC = address
            return 24
        return 12

    def PUSH_D5(self) -> int:
        """PUSH DE"""
        self.R.PUSH(self.R.DE)
        return 16

    def SUB_D6(self, value: int) -> int:
        """SUB A, n8"""
        initial = self.R.A
        calc = initial - value
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((initial & 0xF) - (value & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 8

    def RST_D7(self) -> int:
        """RST $10"""
        self.CALL_CD(0x10)
        return 16

    def RET_D8(self) -> int:
        """RET C"""
        if self.R.CARRY == 1:
            self.R.PC = self.R.POP()
            return 20
        return 8

    def RETI_D9(self) -> int:
        """RETI"""
        self.EI_FB()
        self.RET_C9()
        return 16

    def JP_DA(self, address: int) -> int:
        """JP C, n16"""
        if self.R.CARRY == 1:
            self.R.PC = address
            return 16
        return 12

    def CALL_DC(self, address: int) -> int:
        """CALL C,n16"""
        if self.R.CARRY == 1:
            self.R.PUSH(self.R.PC)
            self.R.PC = address
            return 24
        return 12

    def SBC_DE(self, value: int) -> int:
        """SBC A, n8"""
        initial = self.R.A
        carryBit = self.R.CARRY
        calc = initial - (value + carryBit)
        final = calc & 0xFF
        self.R.A = final
        self.R.ZERO = (final == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            (initial & 0xF) - ((value & 0xF) + (carryBit & 0xF)) < 0
        ) & 1
        self.R.CARRY = (calc < 0) & 1
        return 8

    def RST_DF(self) -> int:
        """RST $18"""
        self.CALL_CD(0x18)
        return 16

    def LDH_E0(self, offset: int) -> int:
        """LDH [n8],A"""
        self.mmu.set_memory(0xFF00 + offset, self.R.A)
        return 12

    def POP_E1(self) -> int:
        """POP HL"""
        self.R.HL = self.R.POP()
        return 12

    def LDH_E2(self) -> int:
        """LDH [C], A"""
        self.mmu.set_memory(0xFF00 + self.R.C, self.R.A)
        return 8

    def PUSH_E5(self) -> int:
        """PUSH HL"""
        self.R.PUSH(self.R.HL)
        return 16

    def AND_E6(self, value: int) -> int:
        """AND A, n8"""
        initial = self.R.A
        calc = initial & value
        self.R.A = calc
        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0
        return 8

    def RST_E7(self) -> int:
        """RST $20"""
        self.CALL_CD(0x20)
        return 16

    def ADD_E8(self, value: int) -> int:
        """ADD SP, e8"""
        initial = self.R.SP
        calc = (value ^ 0x80) - 0x80
        final = (initial + calc) & 0xFFFF
        self.R.SP = final

        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            ((initial & 0xF) + (calc & 0xF) > 0xF)
            or ((initial & 0xF) + (calc & 0xF) < 0)
        ) & 1
        self.R.CARRY = ((initial & 0xFF) + (calc & 0xFF) > 0xFF) or (
            (initial & 0xFF) + (calc & 0xFF) < 0
        )
        return 16

    def JP_E9(self) -> int:
        """JP HL"""
        self.R.PC = self.R.HL
        return 4

    def LD_EA(self, address: int) -> int:
        """LD [n16],A"""
        self.mmu.set_memory(address, self.R.A)
        return 16

    def XOR_EE(self, value: int) -> int:
        """XOR A, n8"""
        calc = self.R.A ^ value
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 8

    def RST_EF(self) -> int:
        """RST $28"""
        self.CALL_CD(0x28)
        return 16

    def LDH_F0(self, offset: int) -> int:
        """LDH A, [n8]"""
        self.R.A = self.mmu.get_memory(0xFF00 + offset)
        return 12

    def POP_F1(self) -> int:
        """POP AF"""
        self.R.AF = self.R.POP()
        return 12

    def LDH_F2(self) -> int:
        """LDH A, [C]"""
        self.R.A = self.mmu.get_memory(0xFF00 + self.R.C)
        return 8

    def DI_F3(self) -> int:
        """DI"""
        self.mmu.IME = False
        return 4

    def PUSH_F5(self) -> int:
        """PUSH AF"""
        self.R.PUSH(self.R.AF)
        return 16

    def OR_F6(self, value: int) -> int:
        """OR A, n8"""
        calc = self.R.A | value
        self.R.A = calc

        self.R.ZERO = (calc == 0) & 1
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return 8

    def RST_F7(self) -> int:
        """RST $30"""
        self.CALL_CD(0x30)
        return 16

    def LD_F8(self, value: int) -> int:
        """LD HL, SP + e8"""
        addr = (value ^ 0x80) - 0x80
        calc = self.R.SP + addr
        final = calc & 0xFFFF
        self.R.HL = final

        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            ((self.R.SP & 0xF) + (addr & 0xF) > 0xF)
            or ((self.R.SP & 0xF) + (addr & 0xF) < 0)
        ) & 1
        self.R.CARRY = ((self.R.SP & 0xFF) + (addr & 0xFF) > 0xFF) or (
            (self.R.SP & 0xFF) + (addr & 0xFF) < 0
        )

        return 12

    def LD_F9(self) -> int:
        """LD SP, HL"""
        self.R.SP = self.R.HL
        return 8

    def LD_FA(self, address: int) -> int:
        """LD A, [n16]"""
        self.R.A = self.mmu.get_memory(address)
        return 16

    def EI_FB(self) -> int:
        """EI"""
        self.mmu.IME = True
        return 4

    def CP_FE(self, value: int) -> int:
        """CP A, n8"""
        calc = self.R.A - value
        self.R.ZERO = ((calc & 0xFF) == 0) & 1
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = ((self.R.A & 0xF) - (value & 0xF) < 0) & 1
        self.R.CARRY = (calc < 0) & 1
        return 8

    def RST_FF(self) -> int:
        """RST $38"""
        self.CALL_CD(0x38)
        return 16
