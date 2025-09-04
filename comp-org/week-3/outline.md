# Week 3: Basics of Computer Architecture  

*References: Patterson & Hennessy, ARM Ed., Ch. 1 (§1.1–§1.5)*  

---

## 1. Computer Architecture vs. Computer Organization (§1.1)  
**(New material — not in earlier slides)**  

### 1.1 Definitions  
- **Computer Architecture**  
  - Programmer’s view of the machine.  
  - Instruction set, data types, addressing modes.  

- **Computer Organization**  
  - How the architecture is implemented.  
  - Datapath, control signals, pipelines, memory hierarchy.  

**Analogy:**  
- Architecture = house blueprint.  
- Organization = how it is built (materials, layout, plumbing).  

---

## 2. Major Components of a Computer System (§1.3)  
**(Review/Extension: builds on “Inside your computer” slides)**  

- **CPU**: Control unit, datapath, registers.  
- **Memory hierarchy**: Registers → cache → RAM → storage.  
- **I/O devices**: Keyboards, displays, storage, networking.  
- **Buses**: Communication pathways.  

---

## 3. Stored-Program Concept & Von Neumann Model (§1.2)  

- **Stored-Program Concept**: Instructions and data both stored in memory.  
- Invented by John von Neumann (1945, EDVAC report).  
- Enables programs to modify other programs as data.  

- **Von Neumann Architecture**:  
  - Single memory for instructions and data.  
  - Sequential instruction execution.  
  - **Bottleneck**: CPU speed limited by memory bandwidth.  

- **Harvard Architecture (contrast)**: separate instruction and data memory.  

---

## 4. The Fetch–Decode–Execute Cycle (§1.4)  

### 4.1 Cycle Steps  
1. **Fetch** instruction from memory (address in PC).  
2. **Decode**: Determine opcode and operands.  
3. **Execute**: Perform operation in ALU, memory, or I/O.  
4. **Store result** in register or memory.  
5. **Update PC** to next instruction.  

### 4.2 Example Walkthrough  
Instruction (conceptual): `R1 ← R2 + R3`  
- Fetch → Decode → Execute → Store → Update PC.  

---

## 5. RISC vs. CISC (Preview Only) (§1.1)  

- **RISC (Reduced Instruction Set Computer)**  
  - Small, simple instructions.  
  - Fixed length.  
  - Example: ARM.  

- **CISC (Complex Instruction Set Computer)**  
  - Large, complex instruction set.  
  - Variable length.  
  - Example: Intel x86.  

---

## 6. Basic Performance Metrics (§1.5)  

### 6.1 CPU Time Formula  

```

CPU Time = Instruction Count × CPI × Clock Cycle Time

```

- **Instruction Count (IC):** # of instructions executed.  
- **Cycles Per Instruction (CPI):** avg cycles per instruction.  
- **Clock Cycle Time:** 1 ÷ clock frequency.  

### 6.2 Example Comparison  
Processor A: 3 GHz, CPI = 2  
Processor B: 2 GHz, CPI = 1.2  

**Solution:**  
- A: 0.333 ns cycle × 2 = 0.666 ns per instr.  
- B: 0.5 ns cycle × 1.2 = 0.6 ns per instr.  
- **Processor B is faster**, despite lower GHz.  

---

## 7. Transition to Next Week (Preview)  

- **This week:** Architecture concepts, stored program, CPU cycle, performance basics.  
- **Next week (Week 4):** Logic circuits (Appendix A): gates, combinational circuits, sequential logic.  
