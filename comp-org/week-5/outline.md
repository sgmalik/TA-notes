# Week 5: Data Representation (Chapter 2, §2.1–§2.4)  

*References: Patterson & Hennessy, ARM Ed., Chapter 2 (§2.1–§2.4)*  

---

## 1. Bits, Bytes, and Words (§2.1)  
- Bit: smallest unit (0 or 1).  
- Byte: 8 bits, standard unit of storage.  
- Word: natural unit of data for a processor (e.g., 32 bits for ARMv7, 64 bits for ARMv8).  
- Example: integer 300 requires 2 bytes.  
- Importance: alignment in memory.  

---

## 2. Unsigned Binary Numbers (§2.2)  
- Binary positional notation, base-2 system.  
- Example: 1101₂ = 13.  
- Maximum values with n-bit unsigned (2ⁿ – 1).  
- Overflow example: 255 + 1 in 8-bit unsigned wraps to 0.  

---

## 3. Signed Binary Numbers (§2.3)  
- Need to represent negative values.  
- Sign-and-magnitude: simplest, but two representations of 0.  
- One’s complement: invert bits for negative, still has +0 and –0.  
- Two’s complement (standard): invert bits, add 1.  
- Example: 4-bit two’s complement — 0110 = +6, 1010 = –6.  
- Advantages: unique zero, same hardware for add/sub.  

---

## 4. Arithmetic in Two’s Complement (§2.3–§2.4)  
- Addition and subtraction in two’s complement.  
- Overflow detection (adding two positives → negative, or two negatives → positive).  
- Example: 0111 (7) + 0001 (1) = 1000 (–8 in 4-bit two’s complement).  

---

## 5. Characters and ASCII (§2.4)  
- Encoding characters in binary.  
- ASCII mapping (e.g., ‘A’ = 65, ‘a’ = 97).  
- Unicode/UTF-8 as modern extensions.  

---

## 6. Transition to Next Week  
- Data representation forms the bridge between hardware circuits and software meaning.  
- Next week → fractions, real numbers, IEEE 754 floating point.  

