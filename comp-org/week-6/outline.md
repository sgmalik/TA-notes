# Week 6: Arithmetic and Floating Point (Chapter 3, §3.1–§3.5)  

*References: Patterson & Hennessy, ARM Ed., Chapter 3 (§3.1–§3.5)*  

---

## 1. Fixed-Point Representation (§3.1)  
- Represent fractions by fixing binary point.  
- Example: 101.101₂ = 5.625.  
- Limitation: fixed range and precision.  

---

## 2. IEEE 754 Floating-Point Standard (§3.2)  
- Motivation: need to represent very large/small numbers.  
- General form: (–1)^sign × 1.fraction × 2^(exponent – bias).  
- 32-bit single precision: 1 sign, 8 exponent, 23 fraction bits.  
- 64-bit double precision: 1 sign, 11 exponent, 52 fraction bits.  

---

## 3. Floating-Point Arithmetic (§3.3)  
- Addition and subtraction require aligning exponents.  
- Multiplication and division adjust exponents directly.  
- Rounding modes: round-to-nearest-even, truncate, etc.  
- Example: Add 1.5 + 2.25 in binary floating-point.  

---

## 4. Special Values in IEEE 754 (§3.4)  
- Zero (positive and negative).  
- Denormalized numbers (very small magnitudes).  
- Infinity 
- NaN (Not a Number) for undefined results (e.g., 0/0).  

---

## 5. Bitwise Operations (§3.5)  
- AND, OR, XOR, NOT at the bit level.  
- Shifts: logical vs. arithmetic.  
- Application: masking bits, extracting fields.  
- Example: clear lowest 4 bits using AND with 1111…0000.  

---

## 6. Transition to Next Week  
- We now understand both integer and floating-point arithmetic in binary.  
- Next step: return to the CPU datapath to see how these operations are implemented in hardware.  
