# Homework Assignment: Implementing a Full Adder

---

## Overview  
In this assignment, you will design and implement a **full adder** in code. A full adder is a fundamental building block of digital logic. It takes three single-bit inputs — two operand bits (`A`, `B`) and a carry-in bit (`Cin`) — and produces two outputs: the **sum** and the **carry-out** (`Cout`).  

---

## Background  
A full adder is defined by the following Boolean equations:  

- **Sum:** `A ⊕ B ⊕ Cin`  
- **Carry-out:** `(A · B) + (Cin · (A ⊕ B))`  

Truth table for reference:  

| A | B | Cin | Sum | Cout |  
|---|---|-----|-----|------|  
| 0 | 0 |  0  |  0  |  0   |  
| 0 | 0 |  1  |  1  |  0   |  
| 0 | 1 |  0  |  1  |  0   |  
| 0 | 1 |  1  |  0  |  1   |  
| 1 | 0 |  0  |  1  |  0   |  
| 1 | 0 |  1  |  0  |  1   |  
| 1 | 1 |  0  |  0  |  1   |  
| 1 | 1 |  1  |  1  |  1   |  

---

## Requirements  

1. **Single-bit Full Adder Function**  
   - Write a function that takes three inputs (`A`, `B`, `Cin`) and returns both `Sum` and `Cout`.  
   - Ensure the function works for all possible input combinations (8 total).  

2. **Multi-bit Adder (Extension)**  
   - Use the single-bit full adder to construct an **N-bit ripple-carry adder**.  
   - The program should allow the user to enter two binary numbers of equal length and display the result.  
   - The ripple-carry adder should propagate carries from one stage to the next.  

3. **User Interaction**  
   - The program should prompt the user for inputs in binary form.  
   - The output should clearly display:  
     - The binary sum  
     - Any final carry-out  
     - (Optional) The equivalent decimal result  

4. **Extension (Optional, Bonus Credit):**  
  - Implement error-checking for invalid input.  
  - Display intermediate carry values at each stage of the ripple-carry adder.  
