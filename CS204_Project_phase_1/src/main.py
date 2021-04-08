from tkinter import*
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import Image,ImageTk

Window=tk.Tk() #creating the first window for file input

Window.geometry("800x450")
Window.configure(bg="Gray6")
Window.title("RISC-V 32 bit Simulator")

path="bg.jpg"
img=ImageTk.PhotoImage(Image.open(path))
frame=tk.Label(Window,image=img)
frame.pack(fill=BOTH,expand=1)

# Command for button "PROCEED" in first window
def done():
    global file_name
    file_name=file_var.get()
    Window.destroy()


Label_1=tk.Label(Window, text="RISC-V 32 bit SIMULATOR", fg="white", bg="gray6")
Label_1.config(font=("Courier",30))
Label_1.place(x=110,y=50)

# Name of file is stored in this variable
file_var=tk.StringVar()

Label_fileName=tk.Label(text=" Enter File Name ",anchor=CENTER)
Label_fileName.config(font=("Times",15),bg="gray15",fg="white")
Label_fileName.place(x=325,y=200)
Entry_fileName=tk.Entry(Window,textvariable=file_var, font=("Calibri",12), width=50)
Entry_fileName.place(x=190,y=230)


bu = ttk.Button(Window, text="PROCEED", width=25, command=done)
bu.place(x=315,y=280)
Window.resizable(False,False)

# First window destroys
Window.mainloop()

# IR- Instruction Register; PC- Program Counter; in_mry- Instruction Memory; dt_mry- Data Memory; reg- Register
# itr,extra1,extra2- temporary data storing data structure
IR = ""
PC = 0
in_mry = {}
dt_mry = {}
reg = {}
itr = {}
ind = 0
clock = 0
extra1 = {}
extra2 = {}
# Presetting Register data
for i in range(0, 32):
    if (i == 2):
        reg[2] = '7FFFFFF0'
    elif (i == 3):
        reg[3] = '10000000'
    else:
        reg[i] = hex(0)[2:].zfill(8)

# Reading input file
file = open(file_name, 'r')
for each in file:
    ln = each.strip().split(' ')
    if (int(ln[0], 16) >= 268435456):
        dt_mry[hex(int(ln[0], 16))[2:].zfill(8)] = hex(int(ln[1], 16))[2:].zfill(8)
    else:
        in_mry[hex(int(ln[0], 16))] = ln[1]

# Defining Fetch function
def FETCH():
    global PC
    global IR
    global clock
    clock += 1
    ex = hex(PC)
    IR = in_mry.get(ex)
    extra1[clock] = ex
    extra2[clock] = IR
    print("\nFETCH: Fetch instruction " + IR + " from address " + ex)

    DECODE()


# Defining Decode function
def DECODE():
    global IR
    global PC
    global clock
    ins = bin(int(IR, 16))[2:].zfill(32)
    # mnemonic
    mnc = ""
    if (ins[25:32] == '0110011'):
        # R-Format
        if (ins[0:7] == '0000000'):
            if (ins[17:20] == '000'):
                mnc = 'ADD'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '001'):
                mnc = 'SLL'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '010'):
                mnc = 'SLT'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '100'):
                mnc = 'XOR'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '101'):
                mnc = 'SRL'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '110'):
                mnc = 'OR'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '111'):
                mnc = 'AND'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
        elif (ins[0:7] == '0100000'):
            if (ins[17:20] == '000'):
                mnc = 'SUB'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '101'):
                mnc = 'SRA'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
        elif (ins[0:7] == '0000001'):
            if (ins[17:20] == '000'):
                mnc = 'MUL'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '100'):
                mnc = 'DIV'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)
            elif (ins[17:20] == '110'):
                mnc = 'REM'
                rd = int(ins[20:25], 2)
                rs1 = int(ins[12:17], 2)
                rs2 = int(ins[7:12], 2)
                x = int(reg.get(rs1), 16)
                y = int(reg.get(rs2), 16)
                print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                      ", Destination register R", rd, sep='')
                print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
                itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " x" + (str(rs2))
                EXECUTE(mnc, ins[20:25], ins[12:17], ins[7:12], x, y)

    elif (ins[25:32] == '0000011' or ins[25:32] == '0010011' or ins[25:32] == '1100111'):
        # I-Format
        if (ins[17:20] == '000' and ins[25:32] == '0010011'):
            mnc = "ADDI"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            im = int(ins[0:12], 2)
            l = len(ins[0:12])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Immediate value is ", im,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " " + (str(im))
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
        elif (ins[17:20] == '110' and ins[25:32] == '0010011'):
            mnc = "ORI"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            imm = int(ins[0:12], 2)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Immediate value is ", imm,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " " + (str(imm))
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
        elif (ins[17:20] == '111' and ins[25:32] == '0010011'):
            mnc = "ANDI"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            imm = int(ins[0:12], 2)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Immediate value is ", imm,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " " + (str(imm))
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
        elif (ins[17:20] == '000' and ins[25:32] == '0000011'):
            mnc = "LB"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            im = int(ins[0:12], 2)
            l = len(ins[0:12])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Offset value is ", im,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " " + (str(im)) + "(x" + (str(rs1)) + ")"
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
        elif (ins[17:20] == '001' and ins[25:32] == '0000011'):
            mnc = "LH"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            im = int(ins[0:12], 2)
            l = len(ins[0:12])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Offset value is ", im,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " " + (str(im)) + "(x" + (str(rs1)) + ")"
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
        elif (ins[17:20] == '010' and ins[25:32] == '0000011'):
            mnc = "LW"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            im = int(ins[0:12], 2)
            l = len(ins[0:12])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Offset value is ", im,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " " + (str(im)) + "(x" + (str(rs1)) + ")"
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
        elif (ins[25:32] == '1100111'):
            mnc = "JALR"
            rd = int(ins[20:25], 2)
            rs1 = int(ins[12:17], 2)
            im = int(ins[0:12], 2)
            l = len(ins[0:12])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Offset value is ", im,
                  ", Destination register R", rd, sep='')
            print("        Read registers R", rs1, " = ", x, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " x" + (str(rs1)) + " " + (str(im))
            EXECUTE(mnc, ins[20:25], ins[12:17], ins[0:12], x, 0)
    elif (ins[25:32] == '0100011'):
        # S-Format
        if (ins[17:20] == '000'):
            mnc = 'SB'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            off = int((ins[0:7] + ins[20:25]), 2)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Offset value is ", off, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs2)) + " " + (str(off)) + "(x" + (str(rs1)) + ")"
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0:7] + ins[20:25], x, 0)
        elif (ins[17:20] == '001'):
            mnc = 'SH'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            off = int((ins[0:7] + ins[20:25]), 2)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Offset value is ", off, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs2)) + " " + (str(off)) + "(x" + (str(rs1)) + ")"
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0:7] + ins[20:25], x, 0)
        elif (ins[17:20] == '010'):
            mnc = 'SW'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            off = int((ins[0:7] + ins[20:25]), 2)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Offset value is ", off, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs2)) + " " + (str(off)) + "(x" + (str(rs1)) + ")"
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0:7] + ins[20:25], x, 0)
    elif (ins[25:32] == '1100011'):
        # SB-Format
        if (ins[17:20] == '000'):
            mnc = 'BEQ'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            im = int((ins[0] + ins[24] + ins[1:7] + ins[20:24]), 2)
            l = len(ins[0] + ins[24] + ins[1:7] + ins[20:24])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Immediate value is ", 2 * im, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs1)) + " x" + (str(rs2)) + " " + (str(2 * im))
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0] + ins[24] + ins[1:7] + ins[20:24], x, y)
        elif (ins[17:20] == '001'):
            mnc = 'BNE'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            im = int((ins[0] + ins[24] + ins[1:7] + ins[20:24]), 2)
            l = len(ins[0] + ins[24] + ins[1:7] + ins[20:24])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Immediate value is ", 2 * im, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs1)) + " x" + (str(rs2)) + " " + (str(2 * im))
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0] + ins[24] + ins[1:7] + ins[20:24], x, y)
        elif (ins[17:20] == '100'):
            mnc = 'BLT'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            im = int((ins[0] + ins[24] + ins[1:7] + ins[20:24]), 2)
            l = len(ins[0] + ins[24] + ins[1:7] + ins[20:24])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Immediate value is ", 2 * im, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs1)) + " x" + (str(rs2)) + " " + (str(2 * im))
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0] + ins[24] + ins[1:7] + ins[20:24], x, y)
        elif (ins[17:20] == '101'):
            mnc = 'BGE'
            rs1 = int(ins[12:17], 2)
            rs2 = int(ins[7:12], 2)
            im = int((ins[0] + ins[24] + ins[1:7] + ins[20:24]), 2)
            l = len(ins[0] + ins[24] + ins[1:7] + ins[20:24])
            if ((im & (1 << (l - 1))) != 0):
                im = im - (1 << l)
            x = int(reg.get(rs1), 16)
            y = int(reg.get(rs2), 16)
            print("DECODE: Operation is ", mnc, ", First operand R", rs1, ", Second operand R", rs2,
                  ", Immediate value is ", 2 * im, sep='')
            print("        Read registers R", rs1, " = ", x, ", R", rs2, " = ", y, sep='')
            itr[clock] = mnc + " x" + (str(rs1)) + " x" + (str(rs2)) + " " + (str(2 * im))
            EXECUTE(mnc, ins[12:17], ins[7:12], ins[0] + ins[24] + ins[1:7] + ins[20:24], x, y)
    elif (ins[25:32] == '0010111' or ins[25:32] == '0110111'):
        # U-Format
        if (ins[25:32] == '0010111'):
            mnc = 'AUIPC'
            rd = int(ins[20:25], 2)
            imm = int(ins[0:20], 2)
            print("DECODE: Immediate value is ", imm, ", Destination register R", rd, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " " + (str(imm))
            EXECUTE(mnc, ins[20:25], ins[0:20], 'none', 0, 0)
        elif (ins[25:32] == '0110111'):
            mnc = 'LUI'
            rd = int(ins[20:25], 2)
            imm = int(ins[0:20], 2)
            print("DECODE: Immediate value is ", imm, ", Destination register R", rd, sep='')
            itr[clock] = mnc + " x" + (str(rd)) + " " + (str(imm))
            EXECUTE(mnc, ins[20:25], ins[0:20], 'none', 0, 0)
    elif (ins[25:32] == '1101111'):
        # UJ-Format
        mnc = 'JAL'
        rd = int(ins[20:25], 2)
        im = int(ins[0] + ins[12:20] + ins[11] + ins[1:11], 2)
        l = len(ins[0] + ins[12:20] + ins[11] + ins[1:11])
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        print("DECODE: Immediate value is ", 2 * im, ", Destination register R", rd, sep='')
        itr[clock] = mnc + " x" + (str(rd)) + " " + (str(2 * im))
        EXECUTE(mnc, ins[20:25], ins[0] + ins[12:20] + ins[11] + ins[1:11], 'none', 0, 0)


def EXECUTE(s1, s2, s3, s4, drs1, drs2):
    global PC
    global ind
    # R-Format
    if (s1 == "ADD"):
        rd = int(s2, 2)
        res = drs1 + drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "AND"):
        rd = int(s2, 2)
        res = drs1 & drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "OR"):
        rd = int(s2, 2)
        res = drs1 | drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "SLL"):
        rd = int(s2, 2)
        tmp = "00000000000000000000000000000000"
        res = bin(drs1)[2:].zfill(32)
        new = res[drs2:32] + tmp[0:drs2]
        print("EXECUTE:", s1, drs1, "by amount", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(int(new, 2))[2:].zfill(8))
    elif (s1 == "SLT"):
        rd = int(s2, 2)
        if (drs1 < drs2):
            res = hex(1)[2:].zfill(8)
            REGISTER_UPDATE(rd, res)
        else:
            res = hex(0)[2:].zfill(8)
            REGISTER_UPDATE(rd, res)
        print("EXECUTE:", s1, "between", drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
    elif (s1 == "SRA"):
        rd = int(s2, 2)
        tmp = "00000000000000000000000000000000"
        tp = "11111111111111111111111111111111"
        res = bin(drs1)[2:].zfill(32)
        if (res[0] == '0'):
            new = tmp[0:drs2] + res[0:(32 - drs2)]
        elif (res[0] == '1'):
            new = tp[0:drs2] + res[0:(32 - drs2)]
        print("EXECUTE:", s1, drs1, "by amount", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(int(new, 2))[2:].zfill(8))
    elif (s1 == "SRL"):
        rd = int(s2, 2)
        tmp = "00000000000000000000000000000000"
        res = bin(drs1)[2:].zfill(32)
        new = tmp[0:drs2] + res[0:(32 - drs2)]
        print("EXECUTE:", s1, drs1, "by amount", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(int(new, 2))[2:].zfill(8))
    elif (s1 == "SUB"):
        rd = int(s2, 2)
        res = drs1 - drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "XOR"):
        rd = int(s2, 2)
        res = drs1 ^ drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "DIV"):
        rd = int(s2, 2)
        res = drs1 / drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "MUL"):
        rd = int(s2, 2)
        res = drs1 * drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "REM"):
        rd = int(s2, 2)
        res = drs1 % drs2
        print("EXECUTE:", s1, drs1, "and", drs2)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))

    # I-Format
    elif (s1 == "ADDI"):
        rd = int(s2, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        res = drs1 + im
        print("EXECUTE:", s1, drs1, "and", im)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "ANDI"):
        rd = int(s2, 2)
        imm = int(s4, 2)
        res = drs1 & imm
        print("EXECUTE:", s1, drs1, "and", imm)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "ORI"):
        rd = int(s2, 2)
        imm = int(s4, 2)
        res = drs1 | imm
        print("EXECUTE:", s1, drs1, "and", imm)
        print("MEMORY: No memory operation")
        print("WRITEBACK: Write ", res, " to R", rd, sep='')
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
    elif (s1 == "LB"):
        rd = int(s2, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        ad = drs1 + im
        if (ad % 4 == 0):
            ad_hex = hex(ad)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad_hex, 'none')
            y = x[6:8]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad_hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "000000" + y)
                print("WRITEBACK: Write ", ("0x000000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "111111" + y)
                print("WRITEBACK: Write ", ("0x111111" + y), " to R", rd, sep='')
        elif (ad % 4 == 1):
            ad_ = ad - 1
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            y = x[4:6]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "000000" + y)
                print("WRITEBACK: Write ", ("0x000000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "111111" + y)
                print("WRITEBACK: Write ", ("0x111111" + y), " to R", rd, sep='')
        elif (ad % 4 == 2):
            ad_ = ad - 2
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            y = x[2:4]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "000000" + y)
                print("WRITEBACK: Write ", ("0x000000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "111111" + y)
                print("WRITEBACK: Write ", ("0x111111" + y), " to R", rd, sep='')
        elif (ad % 4 == 3):
            ad_ = ad - 3
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            y = x[0:2]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "000000" + y)
                print("WRITEBACK: Write ", ("0x000000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "111111" + y)
                print("WRITEBACK: Write ", ("0x111111" + y), " to R", rd, sep='')
    elif (s1 == "LW"):
        rd = int(s2, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        ad = drs1 + im
        if (ad % 4 == 0):
            ad_hex = hex(ad)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad_hex, 'none')
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad_hex, sep='')
            print("WRITEBACK: Write ", x, " to R", rd, sep='')
            REGISTER_UPDATE(rd, x)
        elif (ad % 4 == 1):
            ad_ = ad - 1
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            ad1_ = ad_ + 4
            ad1_hex = hex(ad1_)[2:].zfill(8)
            y = MEMORY_ACCESS('r', ad1_hex, 'none')
            z = y[6:8] + x[0:6]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, "and at address 0x", ad1_hex, sep='')
            print("WRITEBACK: Write ", z, " to R", rd, sep='')
            REGISTER_UPDATE(rd, z)
        elif (ad % 4 == 2):
            ad_ = ad - 2
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            ad1_ = ad_ + 4
            ad1_hex = hex(ad1_)[2:].zfill(8)
            y = MEMORY_ACCESS('r', ad1_hex, 'none')
            z = y[4:8] + x[0:4]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, "and at address 0x", ad1_hex, sep='')
            print("WRITEBACK: Write ", z, " to R", rd, sep='')
            REGISTER_UPDATE(rd, z)
        elif (ad % 4 == 3):
            ad_ = ad - 3
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            ad1_ = ad_ + 4
            ad1_hex = hex(ad1_)[2:].zfill(8)
            y = MEMORY_ACCESS('r', ad1_hex, 'none')
            z = y[2:8] + x[0:2]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, "and at address 0x", ad1_hex, sep='')
            print("WRITEBACK: Write ", z, " to R", rd, sep='')
            REGISTER_UPDATE(rd, z)
    elif (s1 == "LH"):
        rd = int(s2, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        ad = drs1 + im
        if (ad % 4 == 0):
            ad_hex = hex(ad)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad_hex, 'none')
            y = x[4:8]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad_hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "0000" + y)
                print("WRITEBACK: Write ", ("0x0000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "1111" + y)
                print("WRITEBACK: Write ", ("0x1111" + y), " to R", rd, sep='')
        elif (ad % 4 == 1):
            ad_ = ad - 1
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            y = x[2:6]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "0000" + y)
                print("WRITEBACK: Write ", ("0x0000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "1111" + y)
                print("WRITEBACK: Write ", ("0x1111" + y), " to R", rd, sep='')
        elif (ad % 4 == 2):
            ad_ = ad - 2
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            y = x[0:4]
            z = bin(int(y, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "0000" + y)
                print("WRITEBACK: Write ", ("0x0000" + y), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "1111" + y)
                print("WRITEBACK: Write ", ("0x1111" + y), " to R", rd, sep='')
        elif (ad % 4 == 3):
            ad_ = ad - 3
            ad__hex = hex(ad_)[2:].zfill(8)
            x = MEMORY_ACCESS('r', ad__hex, 'none')
            ad1_ = ad_ + 4
            ad1_hex = hex(ad1_)[2:].zfill(8)
            y = MEMORY_ACCESS('r', ad1_hex, 'none')
            w = y[6:8] + x[0:2]
            z = bin(int(w, 16))[2:]
            print("EXECUTE: ", s1, " on R", rd, " from ", drs1, sep='')
            print("MEMORY: Read memory at address 0x", ad__hex, "and at address 0x", ad1_hex, sep='')
            if (z[0] == '0'):
                REGISTER_UPDATE(rd, "0000" + w)
                print("WRITEBACK: Write ", ("0x0000" + w), " to R", rd, sep='')
            elif (z[0] == "1"):
                REGISTER_UPDATE(rd, "1111" + w)
                print("WRITEBACK: Write ", ("0x1111" + w), " to R", rd, sep='')
    elif (s1 == "JALR"):
        rd = int(s2, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        rs1 = int(s3, 2)
        N_PC = PC + 4
        REGISTER_UPDATE(rd, hex(N_PC)[2:].zfill(8))
        res = drs1 + im
        PC = res
        ind = 1
        print("EXECUTE: ", s1, " R", rd, " and R", rs1, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: Write 0x", hex(N_PC)[2:].zfill(8), " to R", rd, sep='')

    # S-Format
    elif (s1 == "SB"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        offset = int(s4, 2)
        stg = reg.get(rs2)[6:8]
        var = drs1 + offset
        print("EXECUTE: ", s1, " on memory from R", rs1, " at address given in R", rs2, sep='')
        if (var % 4 == 0):
            var_hex = hex(var)[2:].zfill(8)
            y = MEMORY_ACCESS('r', var_hex, 'none')
            x = y[0:6] + stg
            MEMORY_ACCESS('w', var_hex, x)
            print("MEMORY: Store byte at 0x", var_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 1):
            v = var - 1
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = y[0:4] + stg + y[6:8]
            MEMORY_ACCESS('w', v_hex, x)
            print("MEMORY: Store byte at 0x", v_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 2):
            v = var - 2
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = y[0:2] + stg + y[4:8]
            MEMORY_ACCESS('w', v_hex, x)
            print("MEMORY: Store byte at 0x", v_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 3):
            v = var - 3
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = stg + y[2:8]
            MEMORY_ACCESS('w', v_hex, x)
            print("MEMORY: Store byte at 0x", v_hex, sep='')
            print("WRITEBACK: NO writeback")
    elif (s1 == "SW"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        offset = int(s4, 2)
        stg = reg.get(rs2)
        var = drs1 + offset
        print("EXECUTE: ", s1, " on memory from R", rs1, " at address given in R", rs2, sep='')
        if (var % 4 == 0):
            var_hex = hex(var)[2:].zfill(8)
            MEMORY_ACCESS('w', var_hex, stg)
            print("MEMORY: Store word at 0x", var_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 1):
            v = var - 1
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = stg[2:8] + y[6:8]
            MEMORY_ACCESS('w', v_hex, x)
            vv = v + 4
            vv_hex = hex(vv)[2:].zfill(8)
            yy = MEMORY_ACCESS('r', vv_hex, 'none')
            xx = yy[0:6] + stg[0:2]
            MEMORY_ACCESS('w', vv_hex, xx)
            print("MEMORY: Store word at 0x", v_hex, " and at 0x", vv_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 2):
            v = var - 2
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = stg[4:8] + y[4:8]
            MEMORY_ACCESS('w', v_hex, x)
            vv = v + 4
            vv_hex = hex(vv)[2:].zfill(8)
            yy = MEMORY_ACCESS('r', vv_hex, 'none')
            xx = yy[0:4] + stg[0:4]
            MEMORY_ACCESS('w', vv_hex, xx)
            print("MEMORY: Store word at 0x", v_hex, " and at 0x", vv_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 3):
            v = var - 3
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = stg[6:8] + y[2:8]
            MEMORY_ACCESS('w', v_hex, x)
            vv = v + 4
            vv_hex = hex(vv)[2:].zfill(8)
            yy = MEMORY_ACCESS('r', vv_hex, 'none')
            xx = yy[0:2] + stg[0:6]
            MEMORY_ACCESS('w', vv_hex, xx)
            print("MEMORY: Store word at 0x", v_hex, " and at 0x", vv_hex, sep='')
            print("WRITEBACK: NO writeback")
    elif (s1 == "SH"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        offset = int(s4, 2)
        stg = reg.get(rs2)
        var = drs1 + offset
        print("EXECUTE: ", s1, " on memory from R", rs1, " at address given in R", rs2, sep='')
        if (var % 4 == 0):
            var_hex = hex(var)[2:].zfill(8)
            y = MEMORY_ACCESS('r', var_hex, 'none')
            x = y[0:4] + stg[4:8]
            MEMORY_ACCESS('w', var_hex, x)
            print("MEMORY: Store halfword at 0x", var_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 1):
            v = var - 1
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = y[0:2] + stg[4:8] + y[6:8]
            MEMORY_ACCESS('w', v_hex, x)
            print("MEMORY: Store halfword at 0x", v_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 2):
            v = var - 2
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = stg[4:8] + y[4:8]
            MEMORY_ACCESS('w', v_hex, x)
            print("MEMORY: Store halfword at 0x", v_hex, sep='')
            print("WRITEBACK: NO writeback")
        elif (var % 4 == 3):
            v = var - 3
            v_hex = hex(v)[2:].zfill(8)
            y = MEMORY_ACCESS('r', v_hex, 'none')
            x = stg[6:8] + y[2:8]
            MEMORY_ACCESS('w', v_hex, x)
            vv = v + 4
            vv_hex = hex(vv)[2:].zfill(8)
            yy = MEMORY_ACCESS('r', vv_hex, 'none')
            xx = yy[0:6] + stg[4:6]
            MEMORY_ACCESS('w', vv_hex, xx)
            print("MEMORY: Store halfword at 0x", v_hex, " and at 0x", vv_hex, sep='')
            print("WRITEBACK: NO writeback")

    # SB-Format
    elif (s1 == "BEQ"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        print("EXECUTE: Compare R", rs1, " and R", rs2, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: No writeback")
        if (drs1 == drs2):
            PC = PC + (2 * im)
            ind = 1
    elif (s1 == "BNE"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        print("EXECUTE: Compare R", rs1, " and R", rs2, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: No writeback")
        if (drs1 != drs2):
            PC = PC + (2 * im)
            ind = 1
    elif (s1 == "BGE"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        print("EXECUTE: Compare R", rs1, " and R", rs2, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: No writeback")
        if (drs1 >= drs2):
            PC = PC + (2 * im)
            ind = 1
    elif (s1 == "BLT"):
        rs1 = int(s2, 2)
        rs2 = int(s3, 2)
        im = int(s4, 2)
        l = len(s4)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        print("EXECUTE: Compare R", rs1, " and R", rs2, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: No writeback")
        if (drs1 < drs2):
            PC = PC + (2 * im)
            ind = 1

    # U-Format
    elif (s1 == "AUIPC"):
        rd = int(s2, 2)
        s = s3 + "000000000000"
        im = int(s, 2)
        l = len(s)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        res = PC + im
        REGISTER_UPDATE(rd, hex(res)[2:].zfill(8))
        print("EXECUTE: ", s1, " to R", rd, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: Write ", hex(res)[2:].zfill(8), " to R", rd, sep='')
    elif (s1 == "LUI"):
        rd = int(s2, 2)
        s = s3 + "000000000000"
        imm = int(s, 2)
        REGISTER_UPDATE(rd, hex(imm)[2:].zfill(8))
        print("EXECUTE: ", s1, " to R", rd, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: Write ", hex(imm)[2:].zfill(8), " to R", rd, sep='')

    # UJ-Format
    elif (s1 == "JAL"):
        rd = int(s2, 2)
        N_PC = PC + 4
        im = int(s3, 2)
        l = len(s3)
        if ((im & (1 << (l - 1))) != 0):
            im = im - (1 << l)
        PC = 2 * im + PC
        REGISTER_UPDATE(rd, hex(N_PC)[2:].zfill(8))
        print("EXECUTE: ", s1, " R", rd, sep='')
        print("MEMORY: No memory  operation")
        print("WRITEBACK: Write ", hex(N_PC)[2:].zfill(8), " to R", rd, sep='')
        ind = 1

# Defining memory access function
def MEMORY_ACCESS(r_w, src_des, value):
    if (r_w == 'r'):
        return dt_mry.get(src_des)
    elif (r_w == 'w'):
        dt_mry[src_des] = value

# Defining Register update function
def REGISTER_UPDATE(rd, value):
    reg[rd] = value
    reg[0] = '00000000'


print("\nNumber of clock cycles:", clock)

# Writing data from data memory to .mc file
f = open('data.mc', 'w')
for i in dt_mry:
    string = "0x" + i + " " + "0x" + dt_mry[i] + "\n"
    f.write(string)
f.close()


# starting of Second Window

# Defining functions for buttons
def popup():
    tk.messagebox.showinfo("POP-UP","Execution Finished")


def run(tree1,tree2,tree3):
    global PC, ind
    while(hex(PC) in in_mry.keys()):
        FETCH()
        if (ind == 0):
            PC = PC + 4
        else:
            ind = 0
    Update_register(tree1)
    Update_memory(tree2)
    Update_instruction(tree3)
    popup()

def nxt(tree1,tree2,tree3):
    global PC,ind
    FETCH()
    if (ind == 0):
        PC = PC + 4
    else:
        ind = 0
    Update_register(tree1)
    Update_memory(tree2)
    Update_instruction(tree3)


def Update_register(tree):
    for row in tree.get_children():
        tree.delete(row)
    for i in range(32):
        tree.insert(parent='', index='end', iid=i, text=i + 1, values=("x" + str(i), "0x" + str(reg.get(i))))


def Update_memory(tree):
    i=0
    for row in tree.get_children():
        tree.delete(row)
    for item in dt_mry:
        tree2.insert(parent='', index='end', iid=i, text=i+1, value=("0x"+str(item),"0x"+str(dt_mry.get(item))))
        i+=1

def Update_instruction(tree):
    for row in tree.get_children():
        tree.delete(row)
    for i in range(0,len(itr)):
        tree.insert(parent='', index='end', iid=i, text=i + 1, value=(str(extra1.get(i+1)), str(extra2.get(i+1)), str(itr.get(i+1))))


Window2 = tk.Tk()
Window2.title("RISC-V SIMULATOR")
Window2.geometry("1200x600")
Window2.config(bg="Gray6")


frame1=Frame(Window2)
frame1.pack(side=LEFT,fill=BOTH,expand=1)
frame1.config(bg="goldenrod1")
frame2=Frame(Window2,padx=20,pady=10,width=600,height=600)
frame2.pack(side=LEFT,fill=BOTH,expand=1)
frame2.config(bg="gray25")
frame3=Frame(Window2,padx=20,pady=10,width=400,height=600)
frame3.pack(side=RIGHT)
frame3.config(bg="goldenrod1")
sub_frame_1=Frame(frame3,padx=10,pady=10)
sub_frame_1.pack(side=TOP,anchor=NW)
sub_frame_1.config(bg="gray25")
sub_frame_2=Frame(frame3,padx=10,pady=10)
sub_frame_2.pack(anchor=NW)
sub_frame_2.config(bg="gray25")


canvas_inst=Canvas(frame2)
sbv_instr=ttk.Scrollbar(frame2,orient=VERTICAL,command=canvas_inst.yview)
sbv_instr.pack(side=RIGHT,fill=Y)
canvas_inst.pack(fill=BOTH,expand=1)
sbh_instr=ttk.Scrollbar(frame2,orient=HORIZONTAL,command=canvas_inst.xview)
sbh_instr.pack(fill=X)
canvas_inst.config(xscrollcommand=sbh_instr.set,yscrollcommand=sbh_instr.set)
canvas_inst.bind('<Configure>', lambda e: canvas_inst.configure(scrollregion=canvas_inst.bbox("all")))

canvas_reg=Canvas(sub_frame_1)
sbv_regtrs=ttk.Scrollbar(sub_frame_1,orient=VERTICAL,command=canvas_reg.yview)
sbv_regtrs.pack(side=RIGHT,fill=Y)
canvas_reg.pack(fill=BOTH,expand=1)
sbh_reg=ttk.Scrollbar(sub_frame_1,orient=HORIZONTAL,command=canvas_reg.xview)
sbh_reg.pack(fill="x")
canvas_reg.config(xscrollcommand=sbh_reg.set,yscrollcommand=sbh_reg)
canvas_reg.bind('<Configure>', lambda e: canvas_reg.configure(scrollregion=canvas_reg.bbox("all")))

canvas_mem=Canvas(sub_frame_2)
sbv_mmr=ttk.Scrollbar(sub_frame_2,orient=VERTICAL,command=canvas_mem.yview)
sbv_mmr.pack(side=RIGHT,fill=Y)

sbh_mem=ttk.Scrollbar(sub_frame_2,orient=HORIZONTAL,command=canvas_mem.xview)
sbh_mem.pack(side=BOTTOM,fill="x")
canvas_mem.pack(fill=BOTH,expand=1)
canvas_mem.config(yscrollcommand=sbh_mem.set,xscrollcommand=sbh_mem.set)
canvas_mem.bind('<Configure>', lambda e: canvas_mem.configure(scrollregion=canvas_mem.bbox("all")))


second_frame_inst=Frame(canvas_inst)
second_frame_reg=Frame(canvas_reg)
second_frame_mem=Frame(canvas_mem)

canvas_inst.create_window((0,0), window=second_frame_inst, anchor="nw")
canvas_reg.create_window((0,0), window=second_frame_reg, anchor="nw")
canvas_mem.create_window((0,0), window=second_frame_mem, anchor="nw")


# Creating treeview for storing register entries
tree1=ttk.Treeview(second_frame_reg,height=len(reg))
tree1.pack()
tree1['columns']=("Register Number","Register Value")
tree1.column("#0",width=40,minwidth=20)
tree1.column("Register Number",width=150,anchor=CENTER)
tree1.column("Register Value",width=200,anchor=CENTER)
tree1.heading("#0",text="S.No",anchor=CENTER)
tree1.heading("Register Number",text="Register Number",anchor=CENTER)
tree1.heading("Register Value",text="Register Value",anchor=CENTER)


# Creating Treeview for storing data memory entries
tree2=ttk.Treeview(second_frame_mem,height="12")
tree2.pack()
tree2['columns']=("Memory Address","Data Stored")
tree2.column("#0",width=40,minwidth=20)
tree2.column("Memory Address",width=150,anchor=CENTER)
tree2.column("Data Stored",width=200,anchor=CENTER)

tree2.heading("#0",text="S.No",anchor=CENTER)
tree2.heading("Memory Address",text="Memory Address",anchor=CENTER)
tree2.heading("Data Stored",text="Data Stored",anchor=CENTER)


# Creating Treeview for storing instruction,PC,
tree3=ttk.Treeview(second_frame_inst,height="38")
tree3.pack(fill="x",padx=9)
tree3['column']=("PC","Machine Code","Basic Code")
tree3.column("#0",width=50)
tree3.column("PC",width=100,anchor=CENTER)
tree3.column("Machine Code",width=150,anchor=CENTER)
tree3.column("Basic Code",width=150,anchor=CENTER)

tree3.heading("#0",text="S.No",)
tree3.heading("PC",text="PC")
tree3.heading("Machine Code",text="Machine Code")
tree3.heading("Basic Code",text="Basic Code")


btn_step=ttk.Button(frame1, text="STEP",command=lambda:nxt(tree1,tree2,tree3))
btn_step.pack(side=LEFT,padx=20)

btn_run=ttk.Button(frame1, text="RUN",command=lambda:run(tree1,tree2,tree3))
btn_run.pack(side=LEFT,padx=20)


Window2.mainloop()







