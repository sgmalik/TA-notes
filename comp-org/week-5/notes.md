# Week 5: Data Representation  
*References: Patterson & Hennessy, ARM Ed., Chapter 2 (§2.1–§2.4)*  

---

## Review  

Last week, we studied the **building blocks of digital logic**: gates, combinational circuits like multiplexers, decoders, and adders, and sequential circuits like latches, flip-flops, and registers. These circuits gave us the hardware foundation for performing arithmetic and controlling the flow of data inside a CPU.  

This week, we shift focus to **what those circuits actually operate on**: the data itself. The binary signals that flow through logic gates are not random 0s and 1s. They represent integers, negative values, characters, and eventually floating-point numbers. Understanding how data is encoded in binary is essential for bridging the gap between high-level programming concepts and the physical machine.  

---

## 1. Bits, Bytes, and Words (§2.1)  

The most fundamental unit of information in computing is the **bit**. A bit can hold a value of `0` or `1`, corresponding physically to a low or high voltage.  

- **Byte:** A collection of 8 bits. The byte is the smallest *addressable unit* of memory in nearly all modern architectures. Even if a program needs only a single bit, memory hardware typically allocates at least a full byte.  

- **Word:** The “natural” unit of data for a processor. A word corresponds to the width of the CPU registers and datapath.  
  - In a 32-bit architecture like ARMv7, a word is 32 bits (4 bytes).  
  - In a 64-bit architecture like ARMv8, a word is 64 bits (8 bytes).  

**Example:**  
The decimal number `300₁₀` is equal to `100101100₂`. This requires 9 bits to store. Since memory addresses bytes, and each byte holds 8 bits, we need 2 full bytes to store this number.  

**Memory alignment:**  
Processors often require data to be stored at addresses that are multiples of the word size. For example, a 4-byte word should be placed at an address divisible by 4. If not, the processor may take longer to fetch the data or may even raise an exception. This ensures efficient memory access.  

---

## 2. Unsigned Binary Numbers (§2.2)  

Binary numbers use **positional notation** just like decimal numbers, but with base 2 instead of base 10. Each position in a binary number represents a power of 2.  

For an n-bit number:  
`Value = (bn-1 × 2^(n-1)) + (bn-2 × 2^(n-2)) + … + (b1 × 2^1) + (b0 × 2^0)`  

**Example:**  
`1101₂ = (1×8) + (1×4) + (0×2) + (1×1) = 13₁₀`  

**Range of values:**  
- An n-bit unsigned integer can represent values from `0 → 2ⁿ – 1`.  
- Examples:  
  - 8-bit unsigned: `0 → 255`  
  - 16-bit unsigned: `0 → 65,535`  
  - 32-bit unsigned: `0 → 4,294,967,295`  

**Overflow:**  
Binary arithmetic is limited by the fixed width of registers. When the result of an operation is too large to fit in the allotted bits, the value “wraps around.”  

**Example (8-bit):**  
`11111111₂ (255) + 1 = 00000000₂ (0)`  

Here the result is 0 because the 9th bit is discarded.  

---

## 3. Signed Binary Numbers (§2.3)  

Unsigned binary cannot represent negative values. Several methods have been used historically to extend binary numbers to represent signed integers.  

### 3.1 Sign-and-Magnitude  
- Leftmost bit = sign (`0` = positive, `1` = negative).  
- Remaining bits = magnitude.  
- Example (4-bit): `1001₂ = –9`.  
- Problem: Two representations of zero (`0000 = +0`, `1000 = –0`).  

### 3.2 One’s Complement  
- Negative numbers are formed by flipping all the bits of the positive number.  
- Example (4-bit): `+5 = 0101`, `–5 = 1010`.  
- Problem: Still has two zeros (`0000 = +0`, `1111 = –0`).  

### 3.3 Two’s Complement (standard today)  
- Negative numbers are formed by flipping all bits of the positive value and adding `1`.  
- Example (4-bit):  
  - `+6 = 0110`  
  - `–6 = invert(0110) = 1001 + 1 = 1010`  
- Range: `–2ⁿ⁻¹ → 2ⁿ⁻¹ – 1`  
  - 4-bit: `–8 → +7`  
  - 32-bit: `–2,147,483,648 → 2,147,483,647`  

**Why two’s complement?**  
- Only one zero (solves the redundancy issue).  
- Addition and subtraction use the *same hardware* for positive and negative numbers.  
- Carry out from the leftmost bit is ignored, simplifying circuits.  

---

## 4. Arithmetic in Two’s Complement (§2.3–§2.4)  

Two’s complement arithmetic follows the same rules as binary addition, with interpretation depending on whether the number is signed or unsigned.  

**Example (4-bit addition with overflow):**  
`0111 (7) + 0001 (1) = 1000 (–8)`  

Here, the result is –8 because the 4-bit signed range is `–8 → +7`. This demonstrates **overflow**.  

**Overflow detection rule:**  
- Overflow occurs if two positive numbers produce a negative, or two negative numbers produce a positive.  
- If the operands have different signs, overflow cannot occur.  

**Subtraction in two’s complement:**  
Subtraction can be performed by adding the two’s complement of the subtrahend.  
Example: `5 – 3 = 5 + (–3)`  

---

## 5. Characters and ASCII (§2.4)  

Computers also represent non-numeric data such as text. This is achieved by mapping characters to integers.  

- **ASCII (American Standard Code for Information Interchange):**  
  - A 7-bit standard that encodes 128 characters, including letters, digits, punctuation, and control codes.  
  - Examples:  
    - `'A' = 65`  
    - `'a' = 97`  
    - `newline = 10`  

- **Extended ASCII:** Uses 8 bits to allow 256 characters, adding support for accented letters and symbols.  

- **Unicode and UTF-8:** Modern computing requires representing characters from all human languages, as well as emojis and symbols. Unicode defines a much larger set of characters, and UTF
