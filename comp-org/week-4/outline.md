# Week 4: Logic Design (Appendix A)  

*References: Patterson & Hennessy, ARM Ed., Appendix A (§A.2–§A.4)*  

---

## 1. Logic Gates (§A.2)  

### 1.1 Basic Gates  
- AND, OR, NOT with Boolean expressions and truth tables.  
- Examples: ATM PIN check (AND), fire alarm (OR), inverter (NOT).  

---

### 1.2 Derived Gates  
- XOR: output = 1 if inputs differ.  
- NAND and NOR: universal gates.  

---

## 2. Combinational Logic (§A.3)  

### 2.1 Definition  
- Outputs depend only on current inputs (no memory).  

---

### 2.2 Multiplexers (MUX)  
- 2:1 MUX: `Y = S'D0 + SD1`  
- Used in datapath selection.  

---

### 2.3 Decoders and Encoders  
- Decoder: n-bit input → one active output.  
- Encoder: reverse operation.  
- Application: instruction decoding.  

---

### 2.4 Adders  
- Half Adder: Sum = A ⊕ B, Carry = A·B.  
- Full Adder: Sum = A ⊕ B ⊕ Cin, Carry = (A·B) + (Cin·(A⊕B)).  
- Ripple-Carry Adder: chaining full adders.  

**Worked Example:**  
- Add `1011₂` + `0110₂`.  

---

## 3. Sequential Logic (§A.4)  

### 3.1 Why Sequential Logic?  
- Computers need state; combinational circuits can’t remember.  

---

### 3.2 Latches  
- SR Latch: stores 1 bit; invalid if S=R=1.  

---

### 3.3 Flip-Flops  
- D Flip-Flop: captures input on clock edge, holds value until next tick.  

**Diagram (describe):** D and CLK inputs, Q and Q’ outputs.  

---

### 3.4 Registers  
- Multiple flip-flops = register.  
- Stores multi-bit values (e.g., 32-bit ARM register).  

**Example**
- Show a 4-bit register storing `1010₂`.  
- Change input to `1100₂` — ask if output updates immediately. (Answer: no, waits for clock.)  

---

## 4. Transition to CPU Design (Preview)  
- Combinational logic → ALU and datapath.  
- Sequential logic → registers, program counter, state.  
- Together → CPU core.  

**Preview:** Week 5 = data representation (bits, bytes, signed/unsigned numbers, two’s complement).  
