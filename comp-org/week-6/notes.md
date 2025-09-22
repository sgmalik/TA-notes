# Week 6: Arithmetic and Floating Point  
*References: Patterson & Hennessy, ARM Ed., Chapter 3 (§3.1–§3.5)*  

---

## Review  

Last week, we focused on **data representation for integers and characters**. We saw how unsigned binary counts naturally from 0 upward, how two’s complement extends this system to include negative numbers, and how characters are encoded with ASCII and Unicode.  

This week, we build on those ideas. Real-world computing requires handling **fractions, extremely large values, and very small values**. Scientific and engineering programs cannot survive on integers alone — they rely on floating-point arithmetic. In addition, we study **bitwise operations**, which treat numbers as raw bit patterns rather than as quantities. These are essential for low-level programming, systems design, and hardware control.  

---

## 1. Bitwise Operations (§3.5)  

Arithmetic interprets a binary pattern as a number. Bitwise operations ignore numeric meaning and instead work directly on the individual bits of the pattern. Each bit of the output depends only on the corresponding input bits.  

- **AND (`&`)**: Produces `1` only if both inputs are `1`.  
  - Example: `1101₂ & 1011₂ = 1001₂`  
- **OR (`|`)**: Produces `1` if either input is `1`.  
  - Example: `1101₂ | 1011₂ = 1111₂`  
- **XOR (`⊕`)**: Produces `1` if the inputs differ.  
  - Example: `1101₂ ⊕ 1011₂ = 0110₂`  
- **NOT (`~`)**: Inverts all bits.  
  - Example: `~1101₂ = 0010₂` (in 4-bit representation).  

**Shift operations:**  
- **Logical left shift:** Shifts bits left, filling with zeros on the right. Equivalent to multiplying by powers of 2.  
  - Example: `00010101₂ << 2 = 01010100₂` (21 shifted left 2 = 84).  
- **Logical right shift:** Shifts bits right, filling with zeros on the left. Equivalent to dividing by powers of 2.  
  - Example: `10010000₂ >> 3 = 00010010₂` (144 shifted right 3 = 18).  
- **Arithmetic right shift:** Preserves the sign bit (the leftmost bit in two’s complement) while shifting right.  
  - Example: `11101000₂ (–24)` arithmetic right shift by 2 = `11111010₂ (–6)`.  

**Applications:**  
- **Masking bits:** Using AND with a mask isolates certain bits.  
  - Example: `10111101₂ & 00001111₂ = 00001101₂` extracts the lower 4 bits.  
- **Clearing bits:** Mask with AND and zeros.  
  - Example: `10111101₂ & 11110000₂ = 10110000₂` clears the lower 4 bits.  
- **Setting bits:** Mask with OR and ones.  
  - Example: `10010000₂ | 00001111₂ = 10011111₂`.  
- **Toggling bits:** XOR with ones flips certain bits.  

Bitwise operations are essential for device control, networking protocols, cryptography, and performance-critical software.  

---

## 2. Fixed-Point Representation (§3.1)  

Integers cannot express fractions. The simplest way to store fractional values is **fixed-point representation**, where the binary point (like a decimal point in base 10) is placed at a predetermined position.  

**Example:**  
`101.101₂ = 4 + 0 + 1 + 0.5 + 0 + 0.125 = 5.625₁₀`  

In this case:  
- Bits to the left of the binary point represent powers of 2 (`2² = 4`, `2¹ = 2`, `2⁰ = 1`).  
- Bits to the right represent fractions (`2⁻¹ = 0.5`, `2⁻² = 0.25`, `2⁻³ = 0.125`).  

**Advantages:**  
- Simple to implement in hardware.  
- Useful in embedded systems or digital signal processing (DSP).  

**Limitations:**  
- Precision and range are both fixed.  
- Example: With 8 bits and 4 fractional bits:  
  - Largest representable value = `1111.1111₂ = 15.9375`.  
  - Smallest increment = `0.0001₂ = 1/16 = 0.0625`.  
- Cannot dynamically adjust to represent both very large and very small numbers.  

Fixed-point works when the range of expected values is known in advance, but it is not general-purpose enough for modern computing.  

---

## 3. IEEE 754 Floating-Point Standard (§3.2)  

To handle a vast range of values with limited bits, computers use **floating-point numbers**, modeled after scientific notation.  

General form:  
`(–1)^sign × 1.fraction × 2^(exponent – bias)`  

### 32-bit single precision  
- 1 sign bit  
- 8 exponent bits (bias = 127)  
- 23 fraction bits (also called mantissa)  

### 64-bit double precision  
- 1 sign bit  
- 11 exponent bits (bias = 1023)  
- 52 fraction bits  

**Example: Represent 6.5 in single precision**  
- Step 1: Convert to binary → `110.1₂`  
- Step 2: Normalize → `1.101₂ × 2^2`  
- Step 3: Sign = 0 (positive)  
- Step 4: Exponent = 2 + 127 = 129 = `10000001₂`  
- Step 5: Fraction = `.101` → `101000...` (padded to 23 bits)  

Final representation:  
`0 10000001 10100000000000000000000`  

Floating-point allows the same 32-bit pattern to represent values as small as ~`10^–38` and as large as ~`10^38`.  

---

## 4. Floating-Point Arithmetic (§3.3)  

Floating-point arithmetic is more complex than integer arithmetic because of normalization and rounding.  

### Addition and subtraction  
1. Align exponents (shift the smaller number).  
2. Add or subtract the fractions.  
3. Normalize the result (shift until it is in `1.x` form).  
4. Round if necessary.  

**Example: 1.5 + 2.25**  
- `1.5 = 1.1₂ × 2^0`  
- `2.25 = 1.001₂ × 2^1`  
- Align → `1.5 = 0.11₂ × 2^1`  
- Add → `0.11₂ + 1.001₂ = 1.111₂`  
- Normalize → `1.111₂ × 2^1 = 3.75₁₀`  

### Multiplication and division  
- Multiply/divide fractions.  
- Add/subtract exponents.  
- Normalize result.  

### Rounding modes  
Since fraction bits are limited, results must be rounded. IEEE 754 defines four modes:  
- Round to nearest, ties to even (default)  
- Round toward 0  
- Round toward +∞  
- Round toward –∞  

Rounding ensures predictable and consistent results across platforms.  

---

## 5. Special Values in IEEE 754 (§3.4)  

Floating-point has special bit patterns to handle cases outside normal arithmetic.  

- **Zero:** Exponent = 0, fraction = 0. There are +0 and –0, but they behave the same in most operations.  
- **Denormalized numbers:** Exponent = 0, fraction ≠ 0. These represent values very close to zero, filling the gap between zero and the smallest normalized number.  
- **Infinity:** Exponent = all 1s, fraction = 0. Results from overflow or division by zero. Can be +∞ or –∞.  
- **NaN (Not a Number):** Exponent = all 1s, fraction ≠ 0. Used for invalid operations such as `0/0`, `∞ – ∞`, or the square root of a negative number.  

These rules make floating-point arithmetic robust and allow programs to continue even when encountering unusual values.  

---

## 6. Transition to Next Week  

This week, we expanded our understanding of binary arithmetic to include **bitwise manipulation, fractions, and floating-point numbers**. We examined how the IEEE 754 standard represents real numbers, how arithmetic is performed, and how special cases like infinity and NaN are handled.  

Next week, we move back into **CPU architecture**, specifically the **datapath**. We will connect the circuits we studied in Weeks 3–4 with the arithmetic operations we studied in Weeks 5–6. This is where hardware and data representation come together to execute programs.  
