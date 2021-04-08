================================================
README
Functional Simulator for RISC V 32-bit ISA
================================================

INTRODUCTION:
--------------------
We made a Function Simulator for RISC V 32-bit ISA. 
It works only for the below instructions:-
1. Support for Pseudo instructions is not compulsory.
2. Limit to RISC-V 32bit ISA, specifically, below 31 instructions:

R format - add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
I format - addi, andi, ori, lb, lh, lw, jalr
S format - sb, sw, sh
SB format - beq, bne, bge, blt
U format - auipc, lui
UJ format - jal

Directory Structure:
--------------------
CS204-Project
    |
    |- doc
        |- Design Document.pdf
    |- src
        |- main.py
        |- bg.jpg
        |- data.mc(created to store data memory after execution)
    |- test
        |- fibo.mc
        |- factorial.mc
        |- bubble_sort.mc
    

REQUIREMENTS:-
You have to install a python compiler and PIL library in your system.
I have attached below a link for this.
https://pypi.org/project/Pillow/2.2.1/ (PIL)
https://www.toolsqa.com/python/install-python/ (Python)


How to execute
--------------
First, make sure the above mentioned software is installed in your system.
1)You have to run "main.py" in the python compiler.
2)A window will appear. You have to type the file name like fibo.mc, factorial.mc.
3)Press the "PROCEED" button
4)A new window will appear that will have sections to show Register details(number and data),Data Memory, a section having basic code with their respective PC and machine
  code.It has two buttons, STEP and RUN. You can check your RISC-V code stepwise by pressing STEP. On the other hand, the RUN button will execute your entire  
  RISC-V instructions in one time.
