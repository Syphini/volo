import json
import helpers
from mmu import MMU
from registers import Registers


class Opcodes:
    def __init__(self, mmu: MMU, registers: Registers):
        self.mmu = mmu
        self.R = registers

        with open("GB/opcodes.json") as f:
            self.opinfo = json.loads(f.read())

    def execute(self, opcode, value):
        match opcode:
            case 0x00:
                self.NOP_00()
            case 0x01:
                self.LD_01(value)
            case 0x02:
                self.LD_02()
            case 0x03:
                self.INC_03()
            case 0x04:
                self.INC_04()
            case 0x05:
                self.DEC_05()
            case 0x06:
                self.LD_06(value)
            case 0x07:
                self.RLCA_07()
            case 0x09:
                self.ADD_09()
            case 0x0A:
                self.LD_0A()
            case 0x0B:
                self.DEC_0B()
            case 0x0C:
                self.INC_0C()
            case 0x0D:
                self.DEC_0D()
            case 0x0E:
                self.LD_0E(value)
            case 0x0F:
                self.RRCA_0F()
            case 0x11:
                self.LD_11(value)
            case 0x12:
                self.LD_12()
            case 0x13:
                self.INC_13()
            case 0x14:
                self.INC_14()
            case 0x15:
                self.DEC_15()
            case 0x16:
                self.LD_16(value)
            case 0x17:
                self.RLA_17()
            case 0x18:
                self.JR_18(value)
            case 0x19:
                self.ADD_19()
            case 0x1A:
                self.LD_1A()
            case 0x1B:
                self.DEC_1B()
            case 0x1C:
                self.INC_1C()
            case 0x1D:
                self.DEC_1D()
            case 0x1E:
                self.LD_1E(value)
            case 0x1F:
                self.RRA_1F(value)
            case 0x20:
                self.JR_20(value)
            case 0x21:
                self.LD_21(value)
            case 0x22:
                self.LD_22()
            case 0x23:
                self.INC_23()
            case 0x24:
                self.INC_24()
            case 0x25:
                self.DEC_25()
            case 0x26:
                self.LD_26(value)
            case 0x28:
                self.JR_28(value)
            case 0x29:
                self.ADD_29()
            case 0x2A:
                self.LD_2A()
            case 0x2B:
                self.DEC_2B()
            case 0x2C:
                self.INC_2C()
            case 0x2D:
                self.DEC_2D()
            case 0x2E:
                self.LD_2E(value)
            case 0x2F:
                self.CPL_2F()
            case 0x30:
                self.JR_30(value)
            case 0x31:
                self.LD_31(value)
            case 0x32:
                self.LD_32()
            case 0x33:
                self.INC_33()
            case 0x34:
                self.INC_34()
            case 0x35:
                self.DEC_35()
            case 0x36:
                self.LD_36(value)
            case 0x37:
                self.SCF_37()
            case 0x38:
                self.JR_38(value)
            case 0x39:
                self.ADD_39()
            case 0x3A:
                self.LD_3A()
            case 0x3B:
                self.DEC_3B()
            case 0x3C:
                self.INC_3C()
            case 0x3D:
                self.DEC_3D()
            case 0x3E:
                self.LD_3E(value)
            case 0x3F:
                self.CCF_3F()
            case 0x40:
                self.LD_40()
            case 0x41:
                self.LD_41()
            case 0x42:
                self.LD_42()
            case 0x43:
                self.LD_43()
            case 0x44:
                self.LD_44()
            case 0x45:
                self.LD_45()
            case 0x46:
                self.LD_46()
            case 0x47:
                self.LD_47()
            case 0x48:
                self.LD_48()
            case 0x49:
                self.LD_49()
            case 0x4A:
                self.LD_4A()
            case 0x4B:
                self.LD_4B()
            case 0x4C:
                self.LD_4C()
            case 0x4D:
                self.LD_4D()
            case 0x4E:
                self.LD_4E()
            case 0x4F:
                self.LD_4F()
            case 0x50:
                self.LD_50()
            case 0x51:
                self.LD_51()
            case 0x52:
                self.LD_52()
            case 0x53:
                self.LD_53()
            case 0x54:
                self.LD_54()
            case 0x55:
                self.LD_55()
            case 0x56:
                self.LD_56()
            case 0x57:
                self.LD_57()
            case 0x58:
                self.LD_58()
            case 0x59:
                self.LD_59()
            case 0x5A:
                self.LD_5A()
            case 0x5B:
                self.LD_5B()
            case 0x5C:
                self.LD_5C()
            case 0x5D:
                self.LD_5D()
            case 0x5E:
                self.LD_5E()
            case 0x5F:
                self.LD_5F()
            case 0x60:
                self.LD_60()
            case 0x61:
                self.LD_61()
            case 0x62:
                self.LD_62()
            case 0x63:
                self.LD_63()
            case 0x64:
                self.LD_64()
            case 0x65:
                self.LD_65()
            case 0x66:
                self.LD_66()
            case 0x67:
                self.LD_67()
            case 0x68:
                self.LD_68()
            case 0x69:
                self.LD_69()
            case 0x6A:
                self.LD_6A()
            case 0x6B:
                self.LD_6B()
            case 0x6C:
                self.LD_6C()
            case 0x6D:
                self.LD_6D()
            case 0x6E:
                self.LD_6E()
            case 0x6F:
                self.LD_6F()
            case 0x70:
                self.LD_70()
            case 0x71:
                self.LD_71()
            case 0x72:
                self.LD_72()
            case 0x73:
                self.LD_73()
            case 0x74:
                self.LD_74()
            case 0x75:
                self.LD_75()
            case 0x76:
                self.HALT_76()
            case 0x77:
                self.LD_77()
            case 0x78:
                self.LD_78()
            case 0x79:
                self.LD_79()
            case 0x7A:
                self.LD_7A()
            case 0x7B:
                self.LD_7B()
            case 0x7C:
                self.LD_7C()
            case 0x7D:
                self.LD_7D()
            case 0x7E:
                self.LD_7E()
            case 0x7F:
                self.LD_7F()
            case 0x80:
                self.ADD_80()
            case 0x81:
                self.ADD_81()
            case 0x82:
                self.ADD_82()
            case 0x83:
                self.ADD_83()
            case 0x84:
                self.ADD_84()
            case 0x85:
                self.ADD_85()
            case 0x86:
                self.ADD_86()
            case 0x87:
                self.ADD_87()
            case 0x88:
                self.ADC_88()
            case 0x89:
                self.ADC_89()
            case 0x8A:
                self.ADC_8A()
            case 0x8B:
                self.ADC_8B()
            case 0x8C:
                self.ADC_8C()
            case 0x8D:
                self.ADC_8D()
            case 0x8E:
                self.ADC_8E()
            case 0x8F:
                self.ADC_8F()
            case 0x90:
                self.SUB_90()
            case 0x91:
                self.SUB_91()
            case 0x92:
                self.SUB_92()
            case 0x93:
                self.SUB_93()
            case 0x94:
                self.SUB_94()
            case 0x95:
                self.SUB_95()
            case 0x96:
                self.SUB_96()
            case 0x97:
                self.SUB_97()
            case 0x98:
                self.SBC_98()
            case 0x99:
                self.SBC_99()
            case 0x9A:
                self.SBC_9A()
            case 0x9B:
                self.SBC_9B()
            case 0x9C:
                self.SBC_9C()
            case 0x9D:
                self.SBC_9D()
            case 0x9E:
                self.SBC_9E()
            case 0x9F:
                self.SBC_9F()
            case 0xA0:
                self.AND_A0()
            case 0xA1:
                self.AND_A1()
            case 0xA2:
                self.AND_A2()
            case 0xA3:
                self.AND_A3()
            case 0xA4:
                self.AND_A4()
            case 0xA5:
                self.AND_A5()
            case 0xA6:
                self.AND_A6()
            case 0xA7:
                self.AND_A7()
            case 0xA8:
                self.XOR_A8()
            case 0xA9:
                self.XOR_A9()
            case 0xAA:
                self.XOR_AA()
            case 0xAB:
                self.XOR_AB()
            case 0xAC:
                self.XOR_AC()
            case 0xAD:
                self.XOR_AD()
            case 0xAE:
                self.XOR_AE()
            case 0xAF:
                self.XOR_AF()
            case 0xB0:
                self.OR_B0()
            case 0xB1:
                self.OR_B1()
            case 0xB2:
                self.OR_B2()
            case 0xB3:
                self.OR_B3()
            case 0xB4:
                self.OR_B4()
            case 0xB5:
                self.OR_B5()
            case 0xB6:
                self.OR_B6()
            case 0xB7:
                self.OR_B7()
            case 0xB8:
                self.CP_B8()
            case 0xB9:
                self.CP_B9()
            case 0xBA:
                self.CP_BA()
            case 0xBB:
                self.CP_BB()
            case 0xBC:
                self.CP_BC()
            case 0xBD:
                self.CP_BD()
            case 0xBE:
                self.CP_BE()
            case 0xBF:
                self.CP_BF()
            case 0xC0:
                self.RET_C0()
            case 0xC1:
                self.POP_C1()
            case 0xC2:
                self.JP_C2(value)
            case 0xC3:
                self.JP_C3(value)
            case 0xC4:
                self.CALL_C4(value)
            case 0xC5:
                self.PUSH_C5()
            case 0xC6:
                self.ADD_C6(value)
            case 0xC8:
                self.RET_C8()
            case 0xC9:
                self.RET_C9()
            case 0xCA:
                self.JP_CA(value)
            case 0xCC:
                self.CALL_CC(value)
            case 0xCD:
                self.CALL_CD(value)
            case 0xD0:
                self.RET_D0()
            case 0xD1:
                self.POP_D1()
            case 0xD4:
                self.CALL_D4(value)
            case 0xD5:
                self.PUSH_D5()
            case 0xD6:
                self.SUB_D6(value)
            case 0xD8:
                self.RET_D8()
            case 0xD9:
                self.RETI_D9()
            case 0xDC:
                self.CALL_DC(value)
            case 0xE0:
                self.LDH_E0(value)
            case 0xE1:
                self.POP_E1()
            case 0xE2:
                self.LDH_E2()
            case 0xE5:
                self.PUSH_E5()
            case 0xE6:
                self.AND_E6(value)
            case 0xE9:
                self.JP_E9()
            case 0xEA:
                self.LD_EA(value)
            case 0xF0:
                self.LDH_F0(value)
            case 0xF1:
                self.POP_F1()
            case 0xF2:
                self.LDH_F2()
            case 0xF3:
                self.DI_F3()
            case 0xF5:
                self.PUSH_F5()
            case 0xF6:
                self.OR_F6(value)
            case 0xFA:
                self.LD_FA(value)
            case 0xFB:
                self.EI_FB()
            case 0xFE:
                self.CP_FE(value)
            case _:
                raise Exception(f"Unknown Instruction: {helpers.int_to_hex(opcode)}")

    def execute_cb(self, opcode):
        match opcode:
            case 0x00:
                self.RLC_CB00()
            case 0x01:
                self.RLC_CB01()
            case 0x02:
                self.RLC_CB02()
            case 0x03:
                self.RLC_CB03()
            case 0x04:
                self.RLC_CB04()
            case 0x05:
                self.RLC_CB05()
            case 0x06:
                self.RLC_CB06()
            case 0x07:
                self.RLC_CB07()
            case 0x08:
                self.RLC_CB08()
            case 0x09:
                self.RRC_CB09()
            case 0x0A:
                self.RRC_CB0A()
            case 0x0B:
                self.RRC_CB0B()
            case 0x0C:
                self.RRC_CB0C()
            case 0x0D:
                self.RRC_CB0D()
            case 0x0E:
                self.RRC_CB0E()
            case 0x0F:
                self.RRC_CB0F()
            case 0x10:
                self.RL_CB10()
            case 0x11:
                self.RL_CB11()
            case 0x12:
                self.RL_CB12()
            case 0x13:
                self.RL_CB13()
            case 0x14:
                self.RL_CB14()
            case 0x15:
                self.RL_CB15()
            case 0x16:
                self.RL_CB16()
            case 0x17:
                self.RL_CB17()
            case 0x18:
                self.RR_CB18()
            case 0x19:
                self.RR_CB19()
            case 0x1A:
                self.RR_CB1A()
            case 0x1B:
                self.RR_CB1B()
            case 0x1C:
                self.RR_CB1C()
            case 0x1D:
                self.RR_CB1D()
            case 0x1E:
                self.RR_CB1E()
            case 0x1F:
                self.RR_CB1F()
            case 0x20:
                self.SLA_CB20()
            case 0x21:
                self.SLA_CB21()
            case 0x22:
                self.SLA_CB22()
            case 0x23:
                self.SLA_CB23()
            case 0x24:
                self.SLA_CB24()
            case 0x25:
                self.SLA_CB25()
            case 0x26:
                self.SLA_CB26()
            case 0x27:
                self.SLA_CB27()
            case 0x28:
                self.SRA_CB28()
            case 0x29:
                self.SRA_CB29()
            case 0x2A:
                self.SRA_CB2A()
            case 0x2B:
                self.SRA_CB2B()
            case 0x2C:
                self.SRA_CB2C()
            case 0x2D:
                self.SRA_CB2D()
            case 0x2E:
                self.SRA_CB2E()
            case 0x2F:
                self.SRA_CB2F()
            case 0x30:
                self.SWAP_CB30()
            case 0x31:
                self.SWAP_CB31()
            case 0x32:
                self.SWAP_CB32()
            case 0x33:
                self.SWAP_CB33()
            case 0x34:
                self.SWAP_CB34()
            case 0x35:
                self.SWAP_CB35()
            case 0x36:
                self.SWAP_CB36()
            case 0x37:
                self.SWAP_CB37()
            case 0x38:
                self.SRL_CB38()
            case 0x39:
                self.SRL_CB39()
            case 0x3A:
                self.SRL_CB3A()
            case 0x3B:
                self.SRL_CB3B()
            case 0x3C:
                self.SRL_CB3C()
            case 0x3D:
                self.SRL_CB3D()
            case 0x3E:
                self.SRL_CB3E()
            case 0x3F:
                self.SRL_CB3F()
            case 0x40:
                self.BIT_CB40()
            case 0x41:
                self.BIT_CB41()
            case 0x42:
                self.BIT_CB42()
            case 0x43:
                self.BIT_CB43()
            case 0x44:
                self.BIT_CB44()
            case 0x45:
                self.BIT_CB45()
            case 0x46:
                self.BIT_CB46()
            case 0x47:
                self.BIT_CB47()
            case 0x48:
                self.BIT_CB48()
            case 0x49:
                self.BIT_CB49()
            case 0x4A:
                self.BIT_CB4A()
            case 0x4B:
                self.BIT_CB4B()
            case 0x4C:
                self.BIT_CB4C()
            case 0x4D:
                self.BIT_CB4D()
            case 0x4E:
                self.BIT_CB4E()
            case 0x4F:
                self.BIT_CB4F()
            case 0x50:
                self.BIT_CB50()
            case 0x51:
                self.BIT_CB51()
            case 0x52:
                self.BIT_CB52()
            case 0x53:
                self.BIT_CB53()
            case 0x54:
                self.BIT_CB54()
            case 0x55:
                self.BIT_CB55()
            case 0x56:
                self.BIT_CB56()
            case 0x57:
                self.BIT_CB57()
            case 0x58:
                self.BIT_CB58()
            case 0x59:
                self.BIT_CB59()
            case 0x5A:
                self.BIT_CB5A()
            case 0x5B:
                self.BIT_CB5B()
            case 0x5C:
                self.BIT_CB5C()
            case 0x5D:
                self.BIT_CB5D()
            case 0x5E:
                self.BIT_CB5E()
            case 0x5F:
                self.BIT_CB5F()
            case 0x60:
                self.BIT_CB60()
            case 0x61:
                self.BIT_CB61()
            case 0x62:
                self.BIT_CB62()
            case 0x63:
                self.BIT_CB63()
            case 0x64:
                self.BIT_CB64()
            case 0x65:
                self.BIT_CB65()
            case 0x66:
                self.BIT_CB66()
            case 0x67:
                self.BIT_CB67()
            case 0x68:
                self.BIT_CB68()
            case 0x69:
                self.BIT_CB69()
            case 0x6A:
                self.BIT_CB6A()
            case 0x6B:
                self.BIT_CB6B()
            case 0x6C:
                self.BIT_CB6C()
            case 0x6D:
                self.BIT_CB6D()
            case 0x6E:
                self.BIT_CB6E()
            case 0x6F:
                self.BIT_CB6F()
            case 0x70:
                self.BIT_CB70()
            case 0x71:
                self.BIT_CB71()
            case 0x72:
                self.BIT_CB72()
            case 0x73:
                self.BIT_CB73()
            case 0x74:
                self.BIT_CB74()
            case 0x75:
                self.BIT_CB75()
            case 0x76:
                self.BIT_CB76()
            case 0x77:
                self.BIT_CB77()
            case 0x78:
                self.BIT_CB78()
            case 0x79:
                self.BIT_CB79()
            case 0x7A:
                self.BIT_CB7A()
            case 0x7B:
                self.BIT_CB7B()
            case 0x7C:
                self.BIT_CB7C()
            case 0x7D:
                self.BIT_CB7D()
            case 0x7E:
                self.BIT_CB7E()
            case 0x7F:
                self.BIT_CB7F()
            case 0x80:
                self.RES_CB80()
            case 0x81:
                self.RES_CB81()
            case 0x82:
                self.RES_CB82()
            case 0x83:
                self.RES_CB83()
            case 0x84:
                self.RES_CB84()
            case 0x85:
                self.RES_CB85()
            case 0x86:
                self.RES_CB86()
            case 0x87:
                self.RES_CB87()
            case 0x88:
                self.RES_CB88()
            case 0x89:
                self.RES_CB89()
            case 0x8A:
                self.RES_CB8A()
            case 0x8B:
                self.RES_CB8B()
            case 0x8C:
                self.RES_CB8C()
            case 0x8D:
                self.RES_CB8D()
            case 0x8E:
                self.RES_CB8E()
            case 0x8F:
                self.RES_CB8F()
            case 0x90:
                self.RES_CB90()
            case 0x91:
                self.RES_CB91()
            case 0x92:
                self.RES_CB92()
            case 0x93:
                self.RES_CB93()
            case 0x94:
                self.RES_CB94()
            case 0x95:
                self.RES_CB95()
            case 0x96:
                self.RES_CB96()
            case 0x97:
                self.RES_CB97()
            case 0x98:
                self.RES_CB98()
            case 0x99:
                self.RES_CB99()
            case 0x9A:
                self.RES_CB9A()
            case 0x9B:
                self.RES_CB9B()
            case 0x9C:
                self.RES_CB9C()
            case 0x9D:
                self.RES_CB9D()
            case 0x9E:
                self.RES_CB9E()
            case 0x9F:
                self.RES_CB9F()
            case 0xA0:
                self.RES_CBA0()
            case 0xA1:
                self.RES_CBA1()
            case 0xA2:
                self.RES_CBA2()
            case 0xA3:
                self.RES_CBA3()
            case 0xA4:
                self.RES_CBA4()
            case 0xA5:
                self.RES_CBA5()
            case 0xA6:
                self.RES_CBA6()
            case 0xA7:
                self.RES_CBA7()
            case 0xA8:
                self.RES_CBA8()
            case 0xA9:
                self.RES_CBA9()
            case 0xAA:
                self.RES_CBAA()
            case 0xAB:
                self.RES_CBAB()
            case 0xAC:
                self.RES_CBAC()
            case 0xAD:
                self.RES_CBAD()
            case 0xAE:
                self.RES_CBAE()
            case 0xAF:
                self.RES_CBAF()
            case 0xB0:
                self.RES_CBB0()
            case 0xB1:
                self.RES_CBB1()
            case 0xB2:
                self.RES_CBB2()
            case 0xB3:
                self.RES_CBB3()
            case 0xB4:
                self.RES_CBB4()
            case 0xB5:
                self.RES_CBB5()
            case 0xB6:
                self.RES_CBB6()
            case 0xB7:
                self.RES_CBB7()
            case 0xB8:
                self.RES_CBB8()
            case 0xB9:
                self.RES_CBB9()
            case 0xBA:
                self.RES_CBBA()
            case 0xBB:
                self.RES_CBBB()
            case 0xBC:
                self.RES_CBBC()
            case 0xBD:
                self.RES_CBBD()
            case 0xBE:
                self.RES_CBBE()
            case 0xBF:
                self.RES_CBBF()
            case 0xC0:
                self.SET_CBC0()
            case 0xC1:
                self.SET_CBC1()
            case 0xC2:
                self.SET_CBC2()
            case 0xC3:
                self.SET_CBC3()
            case 0xC4:
                self.SET_CBC4()
            case 0xC5:
                self.SET_CBC5()
            case 0xC6:
                self.SET_CBC6()
            case 0xC7:
                self.SET_CBC7()
            case 0xC8:
                self.SET_CBC8()
            case 0xC9:
                self.SET_CBC9()
            case 0xCA:
                self.SET_CBCA()
            case 0xCB:
                self.SET_CBCB()
            case 0xCC:
                self.SET_CBCC()
            case 0xCD:
                self.SET_CBCD()
            case 0xCE:
                self.SET_CBCE()
            case 0xCF:
                self.SET_CBCF()
            case 0xD0:
                self.SET_CBD0()
            case 0xD1:
                self.SET_CBD1()
            case 0xD2:
                self.SET_CBD2()
            case 0xD3:
                self.SET_CBD3()
            case 0xD4:
                self.SET_CBD4()
            case 0xD5:
                self.SET_CBD5()
            case 0xD6:
                self.SET_CBD6()
            case 0xD7:
                self.SET_CBD7()
            case 0xD8:
                self.SET_CBD8()
            case 0xD9:
                self.SET_CBD9()
            case 0xDA:
                self.SET_CBDA()
            case 0xDB:
                self.SET_CBDB()
            case 0xDC:
                self.SET_CBDC()
            case 0xDD:
                self.SET_CBDD()
            case 0xDE:
                self.SET_CBDE()
            case 0xDF:
                self.SET_CBDF()
            case 0xE0:
                self.SET_CBE0()
            case 0xE1:
                self.SET_CBE1()
            case 0xE2:
                self.SET_CBE2()
            case 0xE3:
                self.SET_CBE3()
            case 0xE4:
                self.SET_CBE4()
            case 0xE5:
                self.SET_CBE5()
            case 0xE6:
                self.SET_CBE6()
            case 0xE7:
                self.SET_CBE7()
            case 0xE8:
                self.SET_CBE8()
            case 0xE9:
                self.SET_CBE9()
            case 0xEA:
                self.SET_CBEA()
            case 0xEB:
                self.SET_CBEB()
            case 0xEC:
                self.SET_CBEC()
            case 0xED:
                self.SET_CBED()
            case 0xEE:
                self.SET_CBEE()
            case 0xEF:
                self.SET_CBEF()
            case 0xF0:
                self.SET_CBF0()
            case 0xF1:
                self.SET_CBF1()
            case 0xF2:
                self.SET_CBF2()
            case 0xF3:
                self.SET_CBF3()
            case 0xF4:
                self.SET_CBF4()
            case 0xF5:
                self.SET_CBF5()
            case 0xF6:
                self.SET_CBF6()
            case 0xF7:
                self.SET_CBF7()
            case 0xF8:
                self.SET_CBF8()
            case 0xF9:
                self.SET_CBF9()
            case 0xFA:
                self.SET_CBFA()
            case 0xFB:
                self.SET_CBFB()
            case 0xFC:
                self.SET_CBFC()
            case 0xFD:
                self.SET_CBFD()
            case 0xFE:
                self.SET_CBFE()
            case 0xFF:
                self.SET_CBFF()
            case _:
                raise Exception(f"Unknown Instruction: {helpers.int_to_hex(opcode)}")

    def NOP_00(self):
        """NOP"""
        pass

    def LD_01(self, value: int):
        """LD BC,n16"""
        self.R.BC = value

    def LD_02(self):
        """LD [BC],A"""
        self.mmu.set_memory(self.R.BC, self.R.A)

    def INC_03(self):
        """INC BC"""
        self.R.BC += 1

    def INC_R8(self, register):
        initial = register
        calc = initial + 1
        final = calc % 256
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = (0,)
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(initial) > helpers.getLowerNibble(calc) else 0
        )
        self.R.INCREMENT_PC(1)
        return final

    def INC_04(self):
        """INC B"""
        self.R.B = self.INC_R8(self.R.B)

    def DEC_R8(self, register):
        initial = register
        calc = initial - 1
        final = calc % 256
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = (1,)
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(calc) > helpers.getLowerNibble(initial) else 0
        )
        return final

    def DEC_05(self):
        """DEC B"""
        self.R.B = self.DEC_R8(self.R.B)

    def LD_06(self, value):
        """LD B,n8"""
        self.R.B = value

    def RLCA_07(self):
        initial = self.R.A
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110 | carryBit
        self.R.A = calc
        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit

    def ADD_09(self):
        """ADD HL,BC"""
        calc = self.R.HL + self.R.BC
        self.R.HL = calc % 65536
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1 if calc > 2047 else 0
        self.R.CARRY = 1 if calc > 65535 else 0

    def LD_0A(self):
        """LD A,[BC]"""
        self.R.A = self.mmu.get_memory(self.R.BC)

    def DEC_0B(self):
        """DEC BC"""
        self.R.BC -= 1

    def INC_0C(self):
        """INC C"""
        self.R.C = self.INC_R8(self.R.C)

    def DEC_0D(self):
        """DEC C"""
        self.R.C = self.DEC_R8(self.R.C)

    def LD_0E(self, value):
        """LD C,n8"""
        self.R.C = value

    def RRCA_0F(self):
        initial = self.R.A
        carryBit = initial & 0b1
        calc = (carryBit << 7) | initial >> 1
        self.R.A = calc
        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit

    def LD_11(self, value: int):
        """LD DE,n16"""
        self.R.DE = value

    def LD_12(self):
        """LD [DE],A"""
        self.mmu.set_memory(self.R.DE, self.R.A)

    def INC_13(self):
        """INC DE"""
        self.R.DE += 1

    def INC_14(self):
        """INC D"""
        self.R.D = self.INC_R8(self.R.D)

    def DEC_15(self):
        """DEC D"""
        self.R.D = self.DEC_R8(self.R.D)

    def LD_16(self, value):
        """LD D,n8"""
        self.R.D = value

    def RLA_17(self):
        initial = self.R.A
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110 | self.R.CARRY
        self.R.A = calc
        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit

    def JR_18(self, value):
        """JR e8"""
        if (value & (1 << 7)) != 0:
            addr = -(128 - (value - (1 << 7)))
            self.R.INCREMENT_PC(addr)
            return
        self.R.INCREMENT_PC(value)

    def ADD_19(self):
        """ADD HL,DE"""
        calc = self.R.HL + self.R.DE
        self.R.HL = calc % 65536
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1 if calc > 2047 else 0
        self.R.CARRY = 1 if calc > 65535 else 0

    def LD_1A(self):
        """LD A,[DE]"""
        self.R.A = self.mmu.get_memory(self.R.DE)

    def DEC_1B(self):
        """DEC DE"""
        self.R.DE -= 1

    def INC_1C(self):
        """INC E"""
        self.R.E = self.INC_R8(self.R.E)

    def DEC_1D(self):
        """DEC E"""
        self.R.E = self.DEC_R8(self.R.E)

    def LD_1E(self, value):
        """LD E,n8"""
        self.R.E = value

    def RRA_1F(self, register):
        initial = register
        carryBit = initial & 0b1
        calc = (self.R.CARRY << 7) | initial >> 1
        self.R.ZERO = 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def JR_20(self, value):
        """JR NZ,e8"""
        if self.R.ZERO == 0:
            self.JR_18(value)

    def LD_21(self, value: int):
        """LD HL,n16"""
        self.R.HL = value

    def LD_22(self):
        """LD [HLI],A"""
        self.mmu.set_memory(self.R.HL, self.R.A)
        self.R.HL += 1

    def INC_23(self):
        """INC HL"""
        self.R.HL += 1

    def INC_24(self):
        """INC H"""
        self.R.H = self.INC_R8(self.R.H)

    def DEC_25(self):
        """DEC H"""
        self.R.H = self.DEC_R8(self.R.H)

    def LD_26(self, value):
        """LD H,n8"""
        self.R.H = value

    def JR_28(self, value):
        """JR Z,e8"""
        if self.R.ZERO == 1:
            self.JR_18(value)

    def ADD_29(self):
        """ADD HL,HL"""
        calc = self.R.HL + self.R.HL
        self.R.HL = calc % 65536
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1 if calc > 2047 else 0
        self.R.CARRY = 1 if calc > 65535 else 0

    def LD_2A(self):
        """LD A,[HLI]"""
        self.R.A = self.mmu.get_memory(self.R.HL)
        self.R.HL += 1

    def DEC_2B(self):
        """DEC HL"""
        self.R.HL -= 1

    def INC_2C(self):
        """INC L"""
        self.R.L = self.INC_R8(self.R.L)

    def DEC_2D(self):
        """DEC L"""
        self.R.L = self.DEC_R8(self.R.L)

    def LD_2E(self, value):
        """LD L,n8"""
        self.R.L = value

    def CPL_2F(self):
        """CPL"""
        self.R.A = self.R.A ^ 0xFF
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = 1

    def JR_30(self, value):
        """JR NC,e8"""
        if self.R.CARRY == 0:
            self.JR_18(value)

    def LD_31(self, value: int):
        """LD SP,n16"""
        self.R.SP = value

    def LD_32(self):
        """LD [HLD],A"""
        self.mmu.set_memory(self.R.HL, self.R.A)
        self.R.HL -= 1

    def INC_33(self):
        """INC SP"""
        self.R.SP += 1

    def INC_34(self):
        """INC [HL]"""
        self.mmu.set_memory(self.R.HL, self.mmu.get_memory(self.R.HL) + 1)

    def DEC_35(self):
        """DEC [HL]"""
        self.mmu.set_memory(self.R.HL, self.mmu.get_memory(self.R.HL) - 1)

    def LD_36(self, value):
        """LD [HL],n8"""
        self.mmu.set_memory(self.R.HL, value)

    def SCF_37(self):
        """SCF"""
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 1

    def JR_38(self, value):
        """JR C,e8"""
        if self.R.CARRY == 1:
            self.JR_18(value)

    def ADD_39(self):
        """ADD HL,SP"""
        calc = self.R.HL + self.R.SP
        self.R.HL = calc % 65536
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1 if calc > 2047 else 0
        self.R.CARRY = 1 if calc > 65535 else 0

    def LD_3A(self):
        """LD A,[HLD]"""
        self.R.A = self.mmu.get_memory(self.R.HL)
        self.R.HL -= 1

    def DEC_3B(self):
        """DEC SP"""
        self.R.SP -= 1

    def INC_3C(self):
        """INC A"""
        self.R.A = self.INC_R8(self.R.A)

    def DEC_3D(self):
        """DEC A"""
        self.R.A = self.DEC_R8(self.R.A)

    def LD_3E(self, value):
        """LD A,n8"""
        self.R.A = value

    def CCF_3F(self):
        """CCF"""
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 1 if self.R.CARRY == 0 else 0

    def LD_40(self):
        """LD B,B"""
        self.R.B = self.R.B

    def LD_41(self):
        """LD B,C"""
        self.R.B = self.R.C

    def LD_42(self):
        """LD B,D"""
        self.R.B = self.R.D

    def LD_43(self):
        """LD B,E"""
        self.R.B = self.R.E

    def LD_44(self):
        """LD B,H"""
        self.R.B = self.R.H

    def LD_45(self):
        """LD B,L"""
        self.R.B = self.R.L

    def LD_46(self):
        """LD B,[HL]"""
        self.R.B = self.mmu.get_memory(self.R.HL)

    def LD_47(self):
        """LD B,A"""
        self.R.B = self.R.A

    def LD_48(self):
        """LD C,B"""
        self.R.C = self.R.B

    def LD_49(self):
        """LD C,C"""
        self.R.C = self.R.C

    def LD_4A(self):
        """LD C,D"""
        self.R.C = self.R.D

    def LD_4B(self):
        """LD C,E"""
        self.R.C = self.R.E

    def LD_4C(self):
        """LD C,H"""
        self.R.C = self.R.H

    def LD_4D(self):
        """LD C,L"""
        self.R.C = self.R.L

    def LD_4E(self):
        """LD C,[HL]"""
        self.R.C = self.mmu.get_memory(self.R.HL)

    def LD_4F(self):
        """LD C,A"""
        self.R.C = self.R.A

    def LD_50(self):
        """LD D,B"""
        self.R.D = self.R.B

    def LD_51(self):
        """LD D,C"""
        self.R.D = self.R.C

    def LD_52(self):
        """LD D,D"""
        self.R.D = self.R.D

    def LD_53(self):
        """LD D,E"""
        self.R.D = self.R.E

    def LD_54(self):
        """LD D,H"""
        self.R.D = self.R.H

    def LD_55(self):
        """LD D,L"""
        self.R.D = self.R.L

    def LD_56(self):
        """LD D,[HL]"""
        self.R.D = self.mmu.get_memory(self.R.HL)

    def LD_57(self):
        """LD D,A"""
        self.R.D = self.R.A

    def LD_58(self):
        """LD E,B"""
        self.R.E = self.R.B

    def LD_59(self):
        """LD E,C"""
        self.R.E = self.R.C

    def LD_5A(self):
        """LD E,D"""
        self.R.E = self.R.D

    def LD_5B(self):
        """LD E,E"""
        self.R.E = self.R.E

    def LD_5C(self):
        """LD E,H"""
        self.R.E = self.R.H

    def LD_5D(self):
        """LD E,L"""
        self.R.E = self.R.L

    def LD_5E(self):
        """LD E,[HL]"""
        self.R.E = self.mmu.get_memory(self.R.HL)

    def LD_5F(self):
        """LD E,A"""
        self.R.E = self.R.A

    def LD_60(self):
        """LD H,B"""
        self.R.H = self.R.B

    def LD_61(self):
        """LD H,C"""
        self.R.H = self.R.C

    def LD_62(self):
        """LD H,D"""
        self.R.H = self.R.D

    def LD_63(self):
        """LD H,E"""
        self.R.H = self.R.E

    def LD_64(self):
        """LD H,H"""
        self.R.H = self.R.H

    def LD_65(self):
        """LD H,L"""
        self.R.H = self.R.L

    def LD_66(self):
        """LD H,[HL]"""
        self.R.H = self.mmu.get_memory(self.R.HL)

    def LD_67(self):
        """LD H,A"""
        self.R.H = self.R.A

    def LD_68(self):
        """LD L,B"""
        self.R.L = self.R.B

    def LD_69(self):
        """LD L,C"""
        self.R.L = self.R.C

    def LD_6A(self):
        """LD L,D"""
        self.R.L = self.R.D

    def LD_6B(self):
        """LD L,E"""
        self.R.L = self.R.E

    def LD_6C(self):
        """LD L,H"""
        self.R.L = self.R.H

    def LD_6D(self):
        """LD L,L"""
        self.R.L = self.R.L

    def LD_6E(self):
        """LD L,[HL]"""
        self.R.L = self.mmu.get_memory(self.R.HL)

    def LD_6F(self):
        """LD L,A"""
        self.R.L = self.R.A

    def LD_70(self):
        """LD [HL],B"""
        self.mmu.set_memory(self.R.HL, self.R.B)

    def LD_71(self):
        """LD [HL],C"""
        self.mmu.set_memory(self.R.HL, self.R.C)

    def LD_72(self):
        """LD [HL],D"""
        self.mmu.set_memory(self.R.HL, self.R.D)

    def LD_73(self):
        """LD [HL],E"""
        self.mmu.set_memory(self.R.HL, self.R.E)

    def LD_74(self):
        """LD [HL],H"""
        self.mmu.set_memory(self.R.HL, self.R.H)

    def LD_75(self):
        """LD [HL],L"""
        self.mmu.set_memory(self.R.HL, self.R.L)

    def HALT_76(self):
        """HALT"""
        raise Exception("HALT")

    def LD_77(self):
        """LD [HL],A"""
        self.mmu.set_memory(self.R.HL, self.R.A)

    def LD_78(self):
        """LD A,B"""
        self.R.A = self.R.B

    def LD_79(self):
        """LD A,C"""
        self.R.A = self.R.C

    def LD_7A(self):
        """LD A,D"""
        self.R.A = self.R.D

    def LD_7B(self):
        """LD A,E"""
        self.R.A = self.R.E

    def LD_7C(self):
        """LD A,H"""
        self.R.A = self.R.H

    def LD_7D(self):
        """LD A,L"""
        self.R.A = self.R.L

    def LD_7E(self):
        """LD A,[HL]"""
        self.R.A = self.mmu.get_memory(self.R.HL)

    def LD_7F(self):
        """LD A,A"""
        self.R.A = self.R.A

    def ADD_A_N8(self, value):
        initial = self.R.A
        calc = initial + value
        final = calc % 256
        self.R.A = final
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(initial) > helpers.getLowerNibble(value) else 0
        )
        self.R.CARRY = 1 if calc > 255 else 0

    def ADD_80(self):
        """ADD A,B"""
        self.ADD_A_N8(self.R.B)

    def ADD_81(self):
        """ADD A,C"""
        self.ADD_A_N8(self.R.C)

    def ADD_82(self):
        """ADD A,D"""
        self.ADD_A_N8(self.R.D)

    def ADD_83(self):
        """ADD A,E"""
        self.ADD_A_N8(self.R.E)

    def ADD_84(self):
        """ADD A,H"""
        self.ADD_A_N8(self.R.H)

    def ADD_85(self):
        """ADD A,L"""
        self.ADD_A_N8(self.R.L)

    def ADD_86(self):
        """ADD A,[HL]"""
        self.ADD_A_N8(self.mmu.get_memory(self.R.HL))

    def ADD_87(self):
        """ADD A,A"""
        self.ADD_A_N8(self.R.A)

    def ADC_A_N8(self, value):
        initial = self.R.A
        value = value + self.R.CARRY
        calc = initial + value
        final = calc % 256
        self.R.A = final
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(initial) > helpers.getLowerNibble(value) else 0
        )
        self.R.CARRY = 1 if calc > 255 else 0

    def ADC_88(self):
        """ADC A,B"""
        self.ADC_A_N8(self.R.B)

    def ADC_89(self):
        """ADC A,C"""
        self.ADC_A_N8(self.R.C)

    def ADC_8A(self):
        """ADC A,D"""
        self.ADC_A_N8(self.R.D)

    def ADC_8B(self):
        """ADC A,E"""
        self.ADC_A_N8(self.R.E)

    def ADC_8C(self):
        """ADC A,H"""
        self.ADC_A_N8(self.R.H)

    def ADC_8D(self):
        """ADC A,L"""
        self.ADC_A_N8(self.R.L)

    def ADC_8E(self):
        """ADC A,[HL]"""
        self.ADC_A_N8(self.mmu.get_memory(self.R.HL))

    def ADC_8F(self):
        """ADC A,A"""
        self.ADC_A_N8(self.R.A)

    def SUB_A_N8(self, value):
        initial = self.R.A
        calc = initial - value
        final = calc % 256
        self.R.A = final
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(value) > helpers.getLowerNibble(initial) else 0
        )
        self.R.CARRY = 1 if calc < 0 else 0

    def SUB_90(self):
        """SUB A,B"""
        self.SUB_A_N8(self.R.B)

    def SUB_91(self):
        """SUB A,C"""
        self.SUB_A_N8(self.R.C)

    def SUB_92(self):
        """SUB A,D"""
        self.SUB_A_N8(self.R.D)

    def SUB_93(self):
        """SUB A,E"""
        self.SUB_A_N8(self.R.E)

    def SUB_94(self):
        """SUB A,H"""
        self.SUB_A_N8(self.R.H)

    def SUB_95(self):
        """SUB A,L"""
        self.SUB_A_N8(self.R.L)

    def SUB_96(self):
        """SUB A,[HL]"""
        self.SUB_A_N8(self.mmu.get_memory(self.R.HL))

    def SUB_97(self):
        """SUB A,A"""
        self.SUB_A_N8(self.R.A)

    def SBC_A_N8(self, value):
        initial = self.R.A
        value = value + self.R.CARRY
        calc = initial - value
        final = calc % 256
        self.R.A = final
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(value) > helpers.getLowerNibble(initial) else 0
        )
        self.R.CARRY = 1 if calc < 0 else 0

    def SBC_98(self):
        """SBC A,B"""
        self.SBC_A_N8(self.R.B)

    def SBC_99(self):
        """SBC A,C"""
        self.SBC_A_N8(self.R.C)

    def SBC_9A(self):
        """SBC A,D"""
        self.SBC_A_N8(self.R.D)

    def SBC_9B(self):
        """SBC A,E"""
        self.SBC_A_N8(self.R.E)

    def SBC_9C(self):
        """SBC A,H"""
        self.SBC_A_N8(self.R.H)

    def SBC_9D(self):
        """SBC A,L"""
        self.SBC_A_N8(self.R.L)

    def SBC_9E(self):
        """SBC A,[HL]"""
        self.SBC_A_N8(self.mmu.get_memory(self.R.HL))

    def SBC_9F(self):
        """SBC A,A"""
        self.SBC_A_N8(self.R.A)

    def AND_A_N8(self, value):
        initial = self.R.A
        calc = initial & value
        self.R.A = calc
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1
        self.R.CARRY = 0

    def AND_A0(self):
        """AND A,B"""
        self.AND_A_N8(self.R.B)

    def AND_A1(self):
        """AND A,C"""
        self.AND_A_N8(self.R.C)

    def AND_A2(self):
        """AND A,D"""
        self.AND_A_N8(self.R.D)

    def AND_A3(self):
        """AND A,E"""
        self.AND_A_N8(self.R.E)

    def AND_A4(self):
        """AND A,H"""
        self.AND_A_N8(self.R.H)

    def AND_A5(self):
        """AND A,L"""
        self.AND_A_N8(self.R.L)

    def AND_A6(self):
        """AND A,[HL]"""
        self.AND_A_N8(self.mmu.get_memory(self.R.HL))

    def AND_A7(self):
        """AND A,A"""
        self.AND_A_N8(self.R.A)

    def XOR_A_N8(self, value):
        initial = self.R.A
        calc = initial ^ value
        self.R.A = calc
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0

    def XOR_A8(self):
        """XOR A,B"""
        self.XOR_A_N8(self.R.B)

    def XOR_A9(self):
        """XOR A,C"""
        self.XOR_A_N8(self.R.C)

    def XOR_AA(self):
        """XOR A,D"""
        self.XOR_A_N8(self.R.D)

    def XOR_AB(self):
        """XOR A,E"""
        self.XOR_A_N8(self.R.E)

    def XOR_AC(self):
        """XOR A,H"""
        self.XOR_A_N8(self.R.H)

    def XOR_AD(self):
        """XOR A,L"""
        self.XOR_A_N8(self.R.L)

    def XOR_AE(self):
        """XOR A,[HL]"""
        self.XOR_A_N8(self.mmu.get_memory(self.R.HL))

    def XOR_AF(self):
        """XOR A,A"""
        self.XOR_A_N8(self.R.A)

    def OR_A_N8(self, value):
        initial = self.R.A
        calc = initial | value
        self.R.A = calc
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0

    def OR_B0(self):
        """OR A,B"""
        self.OR_A_N8(self.R.B)

    def OR_B1(self):
        """OR A,C"""
        self.OR_A_N8(self.R.C)

    def OR_B2(self):
        """OR A,D"""
        self.OR_A_N8(self.R.D)

    def OR_B3(self):
        """OR A,E"""
        self.OR_A_N8(self.R.E)

    def OR_B4(self):
        """OR A,H"""
        self.OR_A_N8(self.R.H)

    def OR_B5(self):
        """OR A,L"""
        self.OR_A_N8(self.R.L)

    def OR_B6(self):
        """OR A,[HL]"""
        self.OR_A_N8(self.mmu.get_memory(self.R.HL))

    def OR_B7(self):
        """OR A,A"""
        self.OR_A_N8(self.R.A)

    def CP_A_N8(self, value):
        initial = self.R.A
        calc = initial - value
        final = calc % 256
        self.R.ZERO = 1 if final == 0 else 0
        self.R.SUBTRACTION = 1
        self.R.HALFCARRY = (
            1 if helpers.getLowerNibble(value) > helpers.getLowerNibble(initial) else 0
        )
        self.R.CARRY = 1 if calc < 0 else 0

    def CP_B8(self):
        """CP A,B"""
        self.CP_A_N8(self.R.B)

    def CP_B9(self):
        """CP A,C"""
        self.CP_A_N8(self.R.C)

    def CP_BA(self):
        """CP A,D"""
        self.CP_A_N8(self.R.D)

    def CP_BB(self):
        """CP A,E"""
        self.CP_A_N8(self.R.E)

    def CP_BC(self):
        """CP A,H"""
        self.CP_A_N8(self.R.H)

    def CP_BD(self):
        """CP A,L"""
        self.CP_A_N8(self.R.L)

    def CP_BE(self):
        """CP A,[HL]"""
        self.CP_A_N8(self.mmu.get_memory(self.R.HL))

    def CP_BF(self):
        """CP A,A"""
        self.CP_A_N8(self.R.A)

    def RET_C0(self):
        """RET NZ"""
        if self.R.ZERO == 0:
            self.JP_C3(self.R.POP())

    def POP_C1(self):
        """POP BC"""
        self.R.BC = self.R.POP()

    def JP_C2(self, value):
        """JP NZ,n16"""
        if self.R.ZERO == 0:
            self.R.PC = value

    def JP_C3(self, value):
        """JP n16"""
        self.R.PC = value

    def CALL_C4(self, value):
        """CALL NZ,n16"""
        if self.R.ZERO == 0:
            self.R.PUSH(self.R.PC)
            self.JP_C3(value)

    def PUSH_C5(self):
        """PUSH BC"""
        self.R.PUSH(self.R.BC)

    def ADD_C6(self, value):
        """ADD A,n8"""
        self.ADD_A_N8(value)

    def RET_C8(self):
        """RET Z"""
        if self.R.ZERO == 1:
            self.JP_C3(self.R.POP())

    def RET_C9(self):
        """RET"""
        self.JP_C3(self.R.POP())

    def JP_CA(self, value):
        """JP Z,n16"""
        if self.R.ZERO == 1:
            self.R.PC = value

    def RLC_R8(self, value):
        initial = value
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110 | carryBit
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def RLC_CB00(self):
        """RLC B"""
        self.R.B = self.RLC_R8(self.R.B)

    def RLC_CB01(self):
        """RLC C"""
        self.R.C = self.RLC_R8(self.R.C)

    def RLC_CB02(self):
        """RLC D"""
        self.R.D = self.RLC_R8(self.R.D)

    def RLC_CB03(self):
        """RLC E"""
        self.R.E = self.RLC_R8(self.R.E)

    def RLC_CB04(self):
        """RLC H"""
        self.R.H = self.RLC_R8(self.R.H)

    def RLC_CB05(self):
        """RLC L"""
        self.R.L = self.RLC_R8(self.R.L)

    def RLC_CB06(self):
        """RLC [HL]"""
        self.mmu.set_memory(self.R.HL, self.RLC_R8(self.mmu.get_memory(self.R.HL)))

    def RLC_CB07(self):
        """RLC A"""
        self.R.A = self.RLC_R8(self.R.A)

    def RRC_R8(self, register):
        initial = register
        carryBit = initial & 0b1
        calc = (carryBit << 7) | initial >> 1
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def RRC_CB08(self):
        """RRC B"""
        self.R.B = self.RRC_R8(self.R.B)

    def RRC_CB09(self):
        """RRC C"""
        self.R.C = self.RRC_R8(self.R.C)

    def RRC_CB0A(self):
        """RRC D"""
        self.R.D = self.RRC_R8(self.R.D)

    def RRC_CB0B(self):
        """RRC E"""
        self.R.E = self.RRC_R8(self.R.E)

    def RRC_CB0C(self):
        """RRC H"""
        self.R.H = self.RRC_R8(self.R.H)

    def RRC_CB0D(self):
        """RRC L"""
        self.R.L = self.RRC_R8(self.R.L)

    def RRC_CB0E(self):
        """RRC [HL]"""
        self.mmu.set_memory(self.R.HL, self.RRC_R8(self.mmu.get_memory(self.R.HL)))

    def RRC_CB0F(self):
        """RRC A"""
        self.R.A = self.RRC_R8(self.R.A)

    def RL_R8(self, register):
        initial = register
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110 | self.R.CARRY
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def RL_CB10(self):
        """RL B"""
        self.R.B = self.RL_R8(self.R.B)

    def RL_CB11(self):
        """RL C"""
        self.R.C = self.RL_R8(self.R.C)

    def RL_CB12(self):
        """RL D"""
        self.R.D = self.RL_R8(self.R.D)

    def RL_CB13(self):
        """RL E"""
        self.R.E = self.RL_R8(self.R.E)

    def RL_CB14(self):
        """RL H"""
        self.R.H = self.RL_R8(self.R.H)

    def RL_CB15(self):
        """RL L"""
        self.R.L = self.RL_R8(self.R.L)

    def RL_CB16(self):
        """RL [HL]"""
        self.mmu.set_memory(self.R.HL, self.RL_R8(self.mmu.get_memory(self.R.HL)))

    def RL_CB17(self):
        """RL A"""
        self.R.A = self.RL_R8(self.R.A)

    def RR_R8(self, register):
        initial = register
        carryBit = initial & 0b1
        calc = (self.R.CARRY << 7) | initial >> 1
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def RR_CB18(self):
        """RR B"""
        self.R.B = self.RR_R8(self.R.B)

    def RR_CB19(self):
        """RR C"""
        self.R.C = self.RR_R8(self.R.C)

    def RR_CB1A(self):
        """RR D"""
        self.R.D = self.RR_R8(self.R.D)

    def RR_CB1B(self):
        """RR E"""
        self.R.E = self.RR_R8(self.R.E)

    def RR_CB1C(self):
        """RR H"""
        self.R.H = self.RR_R8(self.R.H)

    def RR_CB1D(self):
        """RR L"""
        self.R.L = self.RR_R8(self.R.L)

    def RR_CB1E(self):
        """RR [HL]"""
        self.mmu.set_memory(self.R.HL, self.RR_R8(self.mmu.get_memory(self.R.HL)))

    def RR_CB1F(self):
        """RR A"""
        self.R.A = self.RR_R8(self.R.A)

    def SLA_R8(self, register):
        initial = register
        carryBit = initial >> 7
        calc = (initial << 1) & 0b11111110
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def SLA_CB20(self):
        """SLA B"""
        self.R.B = self.SLA_R8(self.R.B)

    def SLA_CB21(self):
        """SLA C"""
        self.R.C = self.SLA_R8(self.R.C)

    def SLA_CB22(self):
        """SLA D"""
        self.R.D = self.SLA_R8(self.R.D)

    def SLA_CB23(self):
        """SLA E"""
        self.R.E = self.SLA_R8(self.R.E)

    def SLA_CB24(self):
        """SLA H"""
        self.R.H = self.SLA_R8(self.R.H)

    def SLA_CB25(self):
        """SLA L"""
        self.R.L = self.SLA_R8(self.R.L)

    def SLA_CB26(self):
        """SLA [HL]"""
        self.mmu.set_memory(self.R.HL, self.SLA_R8(self.mmu.get_memory(self.R.HL)))

    def SLA_CB27(self):
        """SLA A"""
        self.R.A = self.SLA_R8(self.R.A)

    def SRA_R8(self, register):
        initial = register
        carryBit = initial & 0b1
        calc = (initial >> 7) << 7 | initial >> 1
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def SRA_CB28(self):
        """SRA B"""
        self.R.B = self.SRA_R8(self.R.B)

    def SRA_CB29(self):
        """SRA C"""
        self.R.C = self.SRA_R8(self.R.C)

    def SRA_CB2A(self):
        """SRA D"""
        self.R.D = self.SRA_R8(self.R.D)

    def SRA_CB2B(self):
        """SRA E"""
        self.R.E = self.SRA_R8(self.R.E)

    def SRA_CB2C(self):
        """SRA H"""
        self.R.H = self.SRA_R8(self.R.H)

    def SRA_CB2D(self):
        """SRA L"""
        self.R.L = self.SRA_R8(self.R.L)

    def SRA_CB2E(self):
        """SRA [HL]"""
        self.mmu.set_memory(self.R.HL, self.SRA_R8(self.mmu.get_memory(self.R.HL)))

    def SRA_CB2F(self):
        """SRA A"""
        self.R.A = self.SRA_R8(self.R.A)

    def SWAP_R8(self, register):
        initial = register
        calc = (initial & 0b1111) << 4 | (initial >> 4)
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = 0
        return calc

    def SWAP_CB30(self):
        """SWAP B"""
        self.R.B = self.SWAP_R8(self.R.B)

    def SWAP_CB31(self):
        """SWAP C"""
        self.R.C = self.SWAP_R8(self.R.C)

    def SWAP_CB32(self):
        """SWAP D"""
        self.R.D = self.SWAP_R8(self.R.D)

    def SWAP_CB33(self):
        """SWAP E"""
        self.R.E = self.SWAP_R8(self.R.E)

    def SWAP_CB34(self):
        """SWAP H"""
        self.R.H = self.SWAP_R8(self.R.H)

    def SWAP_CB35(self):
        """SWAP L"""
        self.R.L = self.SWAP_R8(self.R.L)

    def SWAP_CB36(self):
        """SWAP [HL]"""
        self.mmu.set_memory(self.R.HL, self.SWAP_R8(self.mmu.get_memory(self.R.HL)))

    def SWAP_CB37(self):
        """SWAP A"""
        self.R.A = self.SWAP_R8(self.R.A)

    def SRL_R8(self, register):
        initial = register
        carryBit = initial & 0b1
        calc = initial >> 1 & 0b011111111
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 0
        self.R.CARRY = carryBit
        return calc

    def SRL_CB38(self):
        """SRL B"""
        self.R.B = self.SRL_R8(self.R.B)

    def SRL_CB39(self):
        """SRL C"""
        self.R.C = self.SRL_R8(self.R.C)

    def SRL_CB3A(self):
        """SRL D"""
        self.R.D = self.SRL_R8(self.R.D)

    def SRL_CB3B(self):
        """SRL E"""
        self.R.E = self.SRL_R8(self.R.E)

    def SRL_CB3C(self):
        """SRL H"""
        self.R.H = self.SRL_R8(self.R.H)

    def SRL_CB3D(self):
        """SRL L"""
        self.R.L = self.SRL_R8(self.R.L)

    def SRL_CB3E(self):
        """SRL [HL]"""
        self.mmu.set_memory(self.R.HL, self.SRL_R8(self.mmu.get_memory(self.R.HL)))

    def SRL_CB3F(self):
        """SRL A"""
        self.R.A = self.SRL_R8(self.R.A)

    def BIT_U3R8(self, register, value):
        initial = register
        calc = initial >> (value) & 0b1
        self.R.ZERO = 1 if calc == 0 else 0
        self.R.SUBTRACTION = 0
        self.R.HALFCARRY = 1

    def BIT_CB40(self):
        """BIT 0,B"""
        self.BIT_U3R8(self.R.B, 0)

    def BIT_CB41(self):
        """BIT 0,C"""
        self.BIT_U3R8(self.R.C, 0)

    def BIT_CB42(self):
        """BIT 0,D"""
        self.BIT_U3R8(self.R.D, 0)

    def BIT_CB43(self):
        """BIT 0,E"""
        self.BIT_U3R8(self.R.E, 0)

    def BIT_CB44(self):
        """BIT 0,H"""
        self.BIT_U3R8(self.R.H, 0)

    def BIT_CB45(self):
        """BIT 0,L"""
        self.BIT_U3R8(self.R.L, 0)

    def BIT_CB46(self):
        """BIT 0,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 0)

    def BIT_CB47(self):
        """BIT 0,A"""
        self.BIT_U3R8(self.R.A, 0)

    def BIT_CB48(self):
        """BIT 1,B"""
        self.BIT_U3R8(self.R.B, 1)

    def BIT_CB49(self):
        """BIT 1,C"""
        self.BIT_U3R8(self.R.C, 1)

    def BIT_CB4A(self):
        """BIT 1,D"""
        self.BIT_U3R8(self.R.D, 1)

    def BIT_CB4B(self):
        """BIT 1,E"""
        self.BIT_U3R8(self.R.E, 1)

    def BIT_CB4C(self):
        """BIT 1,H"""
        self.BIT_U3R8(self.R.H, 1)

    def BIT_CB4D(self):
        """BIT 1,L"""
        self.BIT_U3R8(self.R.L, 1)

    def BIT_CB4E(self):
        """BIT 1,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 1)

    def BIT_CB4F(self):
        """BIT 1,A"""
        self.BIT_U3R8(self.R.A, 1)

    def BIT_CB50(self):
        """BIT 2,B"""
        self.BIT_U3R8(self.R.B, 2)

    def BIT_CB51(self):
        """BIT 2,C"""
        self.BIT_U3R8(self.R.C, 2)

    def BIT_CB52(self):
        """BIT 2,D"""
        self.BIT_U3R8(self.R.D, 2)

    def BIT_CB53(self):
        """BIT 2,E"""
        self.BIT_U3R8(self.R.E, 2)

    def BIT_CB54(self):
        """BIT 2,H"""
        self.BIT_U3R8(self.R.H, 2)

    def BIT_CB55(self):
        """BIT 2,L"""
        self.BIT_U3R8(self.R.L, 2)

    def BIT_CB56(self):
        """BIT 2,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 2)

    def BIT_CB57(self):
        """BIT 2,A"""
        self.BIT_U3R8(self.R.A, 2)

    def BIT_CB58(self):
        """BIT 3,B"""
        self.BIT_U3R8(self.R.B, 3)

    def BIT_CB59(self):
        """BIT 3,C"""
        self.BIT_U3R8(self.R.C, 3)

    def BIT_CB5A(self):
        """BIT 3,D"""
        self.BIT_U3R8(self.R.D, 3)

    def BIT_CB5B(self):
        """BIT 3,E"""
        self.BIT_U3R8(self.R.E, 3)

    def BIT_CB5C(self):
        """BIT 3,H"""
        self.BIT_U3R8(self.R.H, 3)

    def BIT_CB5D(self):
        """BIT 3,L"""
        self.BIT_U3R8(self.R.L, 3)

    def BIT_CB5E(self):
        """BIT 3,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 3)

    def BIT_CB5F(self):
        """BIT 3,A"""
        self.BIT_U3R8(self.R.A, 3)

    def BIT_CB60(self):
        """BIT 4,B"""
        self.BIT_U3R8(self.R.B, 4)

    def BIT_CB61(self):
        """BIT 4,C"""
        self.BIT_U3R8(self.R.C, 4)

    def BIT_CB62(self):
        """BIT 4,D"""
        self.BIT_U3R8(self.R.D, 4)

    def BIT_CB63(self):
        """BIT 4,E"""
        self.BIT_U3R8(self.R.E, 4)

    def BIT_CB64(self):
        """BIT 4,H"""
        self.BIT_U3R8(self.R.H, 4)

    def BIT_CB65(self):
        """BIT 4,L"""
        self.BIT_U3R8(self.R.L, 4)

    def BIT_CB66(self):
        """BIT 4,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 4)

    def BIT_CB67(self):
        """BIT 4,A"""
        self.BIT_U3R8(self.R.A, 4)

    def BIT_CB68(self):
        """BIT 5,B"""
        self.BIT_U3R8(self.R.B, 5)

    def BIT_CB69(self):
        """BIT 5,C"""
        self.BIT_U3R8(self.R.C, 5)

    def BIT_CB6A(self):
        """BIT 5,D"""
        self.BIT_U3R8(self.R.D, 5)

    def BIT_CB6B(self):
        """BIT 5,E"""
        self.BIT_U3R8(self.R.E, 5)

    def BIT_CB6C(self):
        """BIT 5,H"""
        self.BIT_U3R8(self.R.H, 5)

    def BIT_CB6D(self):
        """BIT 5,L"""
        self.BIT_U3R8(self.R.L, 5)

    def BIT_CB6E(self):
        """BIT 5,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 5)

    def BIT_CB6F(self):
        """BIT 5,A"""
        self.BIT_U3R8(self.R.A, 5)

    def BIT_CB70(self):
        """BIT 6,B"""
        self.BIT_U3R8(self.R.B, 6)

    def BIT_CB71(self):
        """BIT 6,C"""
        self.BIT_U3R8(self.R.C, 6)

    def BIT_CB72(self):
        """BIT 6,D"""
        self.BIT_U3R8(self.R.D, 6)

    def BIT_CB73(self):
        """BIT 6,E"""
        self.BIT_U3R8(self.R.E, 6)

    def BIT_CB74(self):
        """BIT 6,H"""
        self.BIT_U3R8(self.R.H, 6)

    def BIT_CB75(self):
        """BIT 6,L"""
        self.BIT_U3R8(self.R.L, 6)

    def BIT_CB76(self):
        """BIT 6,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 6)

    def BIT_CB77(self):
        """BIT 6,A"""
        self.BIT_U3R8(self.R.A, 6)

    def BIT_CB78(self):
        """BIT 7,B"""
        self.BIT_U3R8(self.R.B, 7)

    def BIT_CB79(self):
        """BIT 7,C"""
        self.BIT_U3R8(self.R.C, 7)

    def BIT_CB7A(self):
        """BIT 7,D"""
        self.BIT_U3R8(self.R.D, 7)

    def BIT_CB7B(self):
        """BIT 7,E"""
        self.BIT_U3R8(self.R.E, 7)

    def BIT_CB7C(self):
        """BIT 7,H"""
        self.BIT_U3R8(self.R.H, 7)

    def BIT_CB7D(self):
        """BIT 7,L"""
        self.BIT_U3R8(self.R.L, 7)

    def BIT_CB7E(self):
        """BIT 7,[HL]"""
        self.BIT_U3R8(self.mmu.get_memory(self.R.HL), 7)

    def BIT_CB7F(self):
        """BIT 7,A"""
        self.BIT_U3R8(self.R.A, 7)

    def RES_U3R8(self, register, value):
        initial = register
        higher = initial >> value + 1 << value + 1
        lower = ((initial << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        return calc

    def RES_CB80(self):
        """RES 0,B"""
        self.R.B = self.RES_U3R8(self.R.B, 0)

    def RES_CB81(self):
        """RES 0,C"""
        self.R.C = self.RES_U3R8(self.R.C, 0)

    def RES_CB82(self):
        """RES 0,D"""
        self.R.D = self.RES_U3R8(self.R.D, 0)

    def RES_CB83(self):
        """RES 0,E"""
        self.R.E = self.RES_U3R8(self.R.E, 0)

    def RES_CB84(self):
        """RES 0,H"""
        self.R.H = self.RES_U3R8(self.R.H, 0)

    def RES_CB85(self):
        """RES 0,L"""
        self.R.L = self.RES_U3R8(self.R.L, 0)

    def RES_CB86(self):
        """RES 0,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 0))

    def RES_CB87(self):
        """RES 0,A"""
        self.R.A = self.RES_U3R8(self.R.A, 0)

    def RES_CB88(self):
        """RES 1,B"""
        self.R.B = self.RES_U3R8(self.R.B, 1)

    def RES_CB89(self):
        """RES 1,C"""
        self.R.C = self.RES_U3R8(self.R.C, 1)

    def RES_CB8A(self):
        """RES 1,D"""
        self.R.D = self.RES_U3R8(self.R.D, 1)

    def RES_CB8B(self):
        """RES 1,E"""
        self.R.E = self.RES_U3R8(self.R.E, 1)

    def RES_CB8C(self):
        """RES 1,H"""
        self.R.H = self.RES_U3R8(self.R.H, 1)

    def RES_CB8D(self):
        """RES 1,L"""
        self.R.L = self.RES_U3R8(self.R.L, 1)

    def RES_CB8E(self):
        """RES 1,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 1))

    def RES_CB8F(self):
        """RES 1,A"""
        self.R.A = self.RES_U3R8(self.R.A, 1)

    def RES_CB90(self):
        """RES 2,B"""
        self.R.B = self.RES_U3R8(self.R.B, 2)

    def RES_CB91(self):
        """RES 2,C"""
        self.R.C = self.RES_U3R8(self.R.C, 2)

    def RES_CB92(self):
        """RES 2,D"""
        self.R.D = self.RES_U3R8(self.R.D, 2)

    def RES_CB93(self):
        """RES 2,E"""
        self.R.E = self.RES_U3R8(self.R.E, 2)

    def RES_CB94(self):
        """RES 2,H"""
        self.R.H = self.RES_U3R8(self.R.H, 2)

    def RES_CB95(self):
        """RES 2,L"""
        self.R.L = self.RES_U3R8(self.R.L, 2)

    def RES_CB96(self):
        """RES 2,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 2))

    def RES_CB97(self):
        """RES 2,A"""
        self.R.A = self.RES_U3R8(self.R.A, 2)

    def RES_CB98(self):
        """RES 3,B"""
        self.R.B = self.RES_U3R8(self.R.B, 3)

    def RES_CB99(self):
        """RES 3,C"""
        self.R.C = self.RES_U3R8(self.R.C, 3)

    def RES_CB9A(self):
        """RES 3,D"""
        self.R.D = self.RES_U3R8(self.R.D, 3)

    def RES_CB9B(self):
        """RES 3,E"""
        self.R.E = self.RES_U3R8(self.R.E, 3)

    def RES_CB9C(self):
        """RES 3,H"""
        self.R.H = self.RES_U3R8(self.R.H, 3)

    def RES_CB9D(self):
        """RES 3,L"""
        self.R.L = self.RES_U3R8(self.R.L, 3)

    def RES_CB9E(self):
        """RES 3,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 3))

    def RES_CB9F(self):
        """RES 3,A"""
        self.R.A = self.RES_U3R8(self.R.A, 3)

    def RES_CBA0(self):
        """RES 4,B"""
        self.R.B = self.RES_U3R8(self.R.B, 4)

    def RES_CBA1(self):
        """RES 4,C"""
        self.R.C = self.RES_U3R8(self.R.C, 4)

    def RES_CBA2(self):
        """RES 4,D"""
        self.R.D = self.RES_U3R8(self.R.D, 4)

    def RES_CBA3(self):
        """RES 4,E"""
        self.R.E = self.RES_U3R8(self.R.E, 4)

    def RES_CBA4(self):
        """RES 4,H"""
        self.R.H = self.RES_U3R8(self.R.H, 4)

    def RES_CBA5(self):
        """RES 4,L"""
        self.R.L = self.RES_U3R8(self.R.L, 4)

    def RES_CBA6(self):
        """RES 4,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 4))

    def RES_CBA7(self):
        """RES 4,A"""
        self.R.A = self.RES_U3R8(self.R.A, 4)

    def RES_CBA8(self):
        """RES 5,B"""
        self.R.B = self.RES_U3R8(self.R.B, 5)

    def RES_CBA9(self):
        """RES 5,C"""
        self.R.C = self.RES_U3R8(self.R.C, 5)

    def RES_CBAA(self):
        """RES 5,D"""
        self.R.D = self.RES_U3R8(self.R.D, 5)

    def RES_CBAB(self):
        """RES 5,E"""
        self.R.E = self.RES_U3R8(self.R.E, 5)

    def RES_CBAC(self):
        """RES 5,H"""
        self.R.H = self.RES_U3R8(self.R.H, 5)

    def RES_CBAD(self):
        """RES 5,L"""
        self.R.L = self.RES_U3R8(self.R.L, 5)

    def RES_CBAE(self):
        """RES 5,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 5))

    def RES_CBAF(self):
        """RES 5,A"""
        self.R.A = self.RES_U3R8(self.R.A, 5)

    def RES_CBB0(self):
        """RES 6,B"""
        self.R.B = self.RES_U3R8(self.R.B, 6)

    def RES_CBB1(self):
        """RES 6,C"""
        self.R.C = self.RES_U3R8(self.R.C, 6)

    def RES_CBB2(self):
        """RES 6,D"""
        self.R.D = self.RES_U3R8(self.R.D, 6)

    def RES_CBB3(self):
        """RES 6,E"""
        self.R.E = self.RES_U3R8(self.R.E, 6)

    def RES_CBB4(self):
        """RES 6,H"""
        self.R.H = self.RES_U3R8(self.R.H, 6)

    def RES_CBB5(self):
        """RES 6,L"""
        self.R.L = self.RES_U3R8(self.R.L, 6)

    def RES_CBB6(self):
        """RES 6,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 6))

    def RES_CBB7(self):
        """RES 6,A"""
        self.R.A = self.RES_U3R8(self.R.A, 6)

    def RES_CBB8(self):
        """RES 7,B"""
        self.R.B = self.RES_U3R8(self.R.B, 7)

    def RES_CBB9(self):
        """RES 7,C"""
        self.R.C = self.RES_U3R8(self.R.C, 7)

    def RES_CBBA(self):
        """RES 7,D"""
        self.R.D = self.RES_U3R8(self.R.D, 7)

    def RES_CBBB(self):
        """RES 7,E"""
        self.R.E = self.RES_U3R8(self.R.E, 7)

    def RES_CBBC(self):
        """RES 7,H"""
        self.R.H = self.RES_U3R8(self.R.H, 7)

    def RES_CBBD(self):
        """RES 7,L"""
        self.R.L = self.RES_U3R8(self.R.L, 7)

    def RES_CBBE(self):
        """RES 7,[HL]"""
        self.mmu.set_memory(self.R.HL, self.RES_U3R8(self.mmu.get_memory(self.R.HL), 7))

    def RES_CBBF(self):
        """RES 7,A"""
        self.R.A = self.RES_U3R8(self.R.A, 7)

    def SET_U3R8(self, register, value):
        initial = register
        higher = ((initial >> value) | 1) << value
        lower = ((initial << 8 - value) & 0xFF) >> 8 - value
        calc = higher | lower
        return calc

    def SET_CBC0(self):
        """SET 0,B"""
        self.R.B = self.SET_U3R8(self.R.B, 0)

    def SET_CBC1(self):
        """SET 0,C"""
        self.R.C = self.SET_U3R8(self.R.C, 0)

    def SET_CBC2(self):
        """SET 0,D"""
        self.R.D = self.SET_U3R8(self.R.D, 0)

    def SET_CBC3(self):
        """SET 0,E"""
        self.R.E = self.SET_U3R8(self.R.E, 0)

    def SET_CBC4(self):
        """SET 0,H"""
        self.R.H = self.SET_U3R8(self.R.H, 0)

    def SET_CBC5(self):
        """SET 0,L"""
        self.R.L = self.SET_U3R8(self.R.L, 0)

    def SET_CBC6(self):
        """SET 0,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 0))

    def SET_CBC7(self):
        """SET 0,A"""
        self.R.A = self.SET_U3R8(self.R.A, 0)

    def SET_CBC8(self):
        """SET 1,B"""
        self.R.B = self.SET_U3R8(self.R.B, 1)

    def SET_CBC9(self):
        """SET 1,C"""
        self.R.C = self.SET_U3R8(self.R.C, 1)

    def SET_CBCA(self):
        """SET 1,D"""
        self.R.D = self.SET_U3R8(self.R.D, 1)

    def SET_CBCB(self):
        """SET 1,E"""
        self.R.E = self.SET_U3R8(self.R.E, 1)

    def SET_CBCC(self):
        """SET 1,H"""
        self.R.H = self.SET_U3R8(self.R.H, 1)

    def SET_CBCD(self):
        """SET 1,L"""
        self.R.L = self.SET_U3R8(self.R.L, 1)

    def SET_CBCE(self):
        """SET 1,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 1))

    def SET_CBCF(self):
        """SET 1,A"""
        self.R.A = self.SET_U3R8(self.R.A, 1)

    def SET_CBD0(self):
        """SET 2,B"""
        self.R.B = self.SET_U3R8(self.R.B, 2)

    def SET_CBD1(self):
        """SET 2,C"""
        self.R.C = self.SET_U3R8(self.R.C, 2)

    def SET_CBD2(self):
        """SET 2,D"""
        self.R.D = self.SET_U3R8(self.R.D, 2)

    def SET_CBD3(self):
        """SET 2,E"""
        self.R.E = self.SET_U3R8(self.R.E, 2)

    def SET_CBD4(self):
        """SET 2,H"""
        self.R.H = self.SET_U3R8(self.R.H, 2)

    def SET_CBD5(self):
        """SET 2,L"""
        self.R.L = self.SET_U3R8(self.R.L, 2)

    def SET_CBD6(self):
        """SET 2,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 2))

    def SET_CBD7(self):
        """SET 2,A"""
        self.R.A = self.SET_U3R8(self.R.A, 2)

    def SET_CBD8(self):
        """SET 3,B"""
        self.R.B = self.SET_U3R8(self.R.B, 3)

    def SET_CBD9(self):
        """SET 3,C"""
        self.R.C = self.SET_U3R8(self.R.C, 3)

    def SET_CBDA(self):
        """SET 3,D"""
        self.R.D = self.SET_U3R8(self.R.D, 3)

    def SET_CBDB(self):
        """SET 3,E"""
        self.R.E = self.SET_U3R8(self.R.E, 3)

    def SET_CBDC(self):
        """SET 3,H"""
        self.R.H = self.SET_U3R8(self.R.H, 3)

    def SET_CBDD(self):
        """SET 3,L"""
        self.R.L = self.SET_U3R8(self.R.L, 3)

    def SET_CBDE(self):
        """SET 3,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 3))

    def SET_CBDF(self):
        """SET 3,A"""
        self.R.A = self.SET_U3R8(self.R.A, 3)

    def SET_CBE0(self):
        """SET 4,B"""
        self.R.B = self.SET_U3R8(self.R.B, 4)

    def SET_CBE1(self):
        """SET 4,C"""
        self.R.C = self.SET_U3R8(self.R.C, 4)

    def SET_CBE2(self):
        """SET 4,D"""
        self.R.D = self.SET_U3R8(self.R.D, 4)

    def SET_CBE3(self):
        """SET 4,E"""
        self.R.E = self.SET_U3R8(self.R.E, 4)

    def SET_CBE4(self):
        """SET 4,H"""
        self.R.H = self.SET_U3R8(self.R.H, 4)

    def SET_CBE5(self):
        """SET 4,L"""
        self.R.L = self.SET_U3R8(self.R.L, 4)

    def SET_CBE6(self):
        """SET 4,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 4))

    def SET_CBE7(self):
        """SET 4,A"""
        self.R.A = self.SET_U3R8(self.R.A, 4)

    def SET_CBE8(self):
        """SET 5,B"""
        self.R.B = self.SET_U3R8(self.R.B, 5)

    def SET_CBE9(self):
        """SET 5,C"""
        self.R.C = self.SET_U3R8(self.R.C, 5)

    def SET_CBEA(self):
        """SET 5,D"""
        self.R.D = self.SET_U3R8(self.R.D, 5)

    def SET_CBEB(self):
        """SET 5,E"""
        self.R.E = self.SET_U3R8(self.R.E, 5)

    def SET_CBEC(self):
        """SET 5,H"""
        self.R.H = self.SET_U3R8(self.R.H, 5)

    def SET_CBED(self):
        """SET 5,L"""
        self.R.L = self.SET_U3R8(self.R.L, 5)

    def SET_CBEE(self):
        """SET 5,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 5))

    def SET_CBEF(self):
        """SET 5,A"""
        self.R.A = self.SET_U3R8(self.R.A, 5)

    def SET_CBF0(self):
        """SET 6,B"""
        self.R.B = self.SET_U3R8(self.R.B, 6)

    def SET_CBF1(self):
        """SET 6,C"""
        self.R.C = self.SET_U3R8(self.R.C, 6)

    def SET_CBF2(self):
        """SET 6,D"""
        self.R.D = self.SET_U3R8(self.R.D, 6)

    def SET_CBF3(self):
        """SET 6,E"""
        self.R.E = self.SET_U3R8(self.R.E, 6)

    def SET_CBF4(self):
        """SET 6,H"""
        self.R.H = self.SET_U3R8(self.R.H, 6)

    def SET_CBF5(self):
        """SET 6,L"""
        self.R.L = self.SET_U3R8(self.R.L, 6)

    def SET_CBF6(self):
        """SET 6,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 6))

    def SET_CBF7(self):
        """SET 6,A"""
        self.R.A = self.SET_U3R8(self.R.A, 6)

    def SET_CBF8(self):
        """SET 7,B"""
        self.R.B = self.SET_U3R8(self.R.B, 7)

    def SET_CBF9(self):
        """SET 7,C"""
        self.R.C = self.SET_U3R8(self.R.C, 7)

    def SET_CBFA(self):
        """SET 7,D"""
        self.R.D = self.SET_U3R8(self.R.D, 7)

    def SET_CBFB(self):
        """SET 7,E"""
        self.R.E = self.SET_U3R8(self.R.E, 7)

    def SET_CBFC(self):
        """SET 7,H"""
        self.R.H = self.SET_U3R8(self.R.H, 7)

    def SET_CBFD(self):
        """SET 7,L"""
        self.R.L = self.SET_U3R8(self.R.L, 7)

    def SET_CBFE(self):
        """SET 7,[HL]"""
        self.mmu.set_memory(self.R.HL, self.SET_U3R8(self.mmu.get_memory(self.R.HL), 7))

    def SET_CBFF(self):
        """SET 7,A"""
        self.R.A = self.SET_U3R8(self.R.A, 7)

    def CALL_CC(self, value):
        """CALL Z,n16"""
        if self.R.ZERO == 1:
            self.R.PUSH(self.R.PC)
            self.JP_C3(value)

    def CALL_CD(self, value):
        """CALL n16"""
        self.R.PUSH(self.R.PC)
        # NOTE: Must ensure PC is currently the address after CALL
        self.JP_C3(value)

    def ADC_CE(self, value):
        """ADC A,n8"""
        self.ADC_A_N8(value)

    def RET_D0(self):
        """RET NC"""
        if self.R.CARRY == 0:
            self.JP_C3(self.R.POP())

    def POP_D1(self):
        """POP DE"""
        self.R.DE = self.R.POP()

    def JP_D2(self, value):
        """JP NC,n16"""
        if self.R.CARRY == 0:
            self.R.PC = value

    def CALL_D4(self, value):
        """CALL NC,n16"""
        if self.R.CARRY == 0:
            self.R.PUSH(self.R.PC)
            self.JP_C3(value)

    def PUSH_D5(self):
        """PUSH DE"""
        self.R.PUSH(self.R.DE)

    def SUB_D6(self, value):
        """SUB A,n8"""
        self.SUB_A_N8(value)

    def RET_D8(self):
        """RET C"""
        if self.R.CARRY == 1:
            self.JP_C3(self.R.POP())

    def RETI_D9(self):
        """RETI"""
        self.EI_FB()
        self.RET_C9()

    def JP_DA(self, value):
        """JP C,n16"""
        if self.R.CARRY == 1:
            self.R.PC = value

    def CALL_DC(self, value):
        """CALL C,n16"""
        if self.R.CARRY == 1:
            self.R.PUSH(self.R.PC)
            self.JP_C3(value)

    def SBC_DE(self, value):
        """SBC A,n8"""
        self.SBC_A_N8(value)

    def LDH_E0(self, value):
        """LDH [n8],A"""
        self.mmu.set_memory(0xFF00 + value, self.R.A)

    def POP_E1(self):
        """POP HL"""
        self.R.HL = self.R.POP()

    def LDH_E2(self):
        """LDH [C],A"""
        self.mmu.set_memory(0xFF00 + self.R.C, self.R.A)

    def PUSH_E5(self):
        """PUSH HL"""
        self.R.PUSH(self.R.HL)

    def AND_E6(self, value):
        """AND A,n8"""
        self.AND_A_N8(value)

    def JP_E9(self):
        """JP HL"""
        self.R.PC = self.R.HL

    def LD_EA(self, value: int):
        """LD [n16],A"""
        self.mmu.set_memory(value, self.R.A)

    def XOR_EE(self, value):
        """XOR A,n8"""
        self.XOR_A_N8(value)

    def LDH_F0(self, value):
        """LDH A,[n8]"""
        self.R.A = self.mmu.get_memory(0xFF00 + value)

    def POP_F1(self):
        """POP AF"""
        self.R.AF = self.R.POP()

    def LDH_F2(self):
        """LDH A,[C]"""
        self.R.A = self.mmu.get_memory(0xFF00 + self.R.C)

    def DI_F3(self):
        """DI"""
        global IME
        IME = False

    def PUSH_F5(self):
        """PUSH AF"""
        self.R.PUSH(self.R.AF)

    def OR_F6(self, value):
        """OR A,n8"""
        self.OR_A_N8(value)

    def LD_FA(self, value):
        """LD A,[n16]"""
        self.R.A = self.mmu.get_memory(value)

    def EI_FB(self):
        """EI"""
        global IME
        IME = True

    def CP_FE(self, value):
        """CP A,n8"""
        self.CP_A_N8(value)
