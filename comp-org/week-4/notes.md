# Week 4: Logic Design  
*References: Patterson & Hennessy, ARM Ed., Appendix A (§A.2–§A.4)*  

---

## Review 

Last week we focused on the **big picture of computer architecture**. We distinguished between **computer architecture**. We examined the **five classic components of a computer system**. We also introduced the **stored-program concept** and the **Von Neumann model**, which together describe how instructions and data coexist in memory and are executed sequentially. This was further examined by tracing the **fetch–decode–execute cycle**, the repetitive process that drives all computation. We discussed **RISC vs. CISC** philosophies and introduced the **CPU performance equation**, which showed that performance depends not only on clock speed but also on instruction count and cycles per instruction. Lastly, we reviewed **boolean logic**, which forms the basis of all decision-making in digital circuits. 

## Topics for This Week

This week, we will dive into the components of the hardware and how these make the architecture work and operate. The hardware introduced last week is made from circuits and at their core, circuits are built off **logic gates** which will be the main point of interest. From here, we will see how these comnbine into **combinational circuits** and **sequential circuits** (more on these later on). This week will bridge the gap: How is the architecture executed in physical hardware.

---

## 1. Logic Gates (§A.2)  

What exactly are **logic gates** and how do they help drive the decision-making process in circuits? **Logic gates** are the physical representation of boolean functions, which as we know, return **true** or **false**. These gates take electronic signals either representing **0 or 1**, with 0 being a low voltage charge and 1 being high. There are two possible options, making this a **binary input** and based on the **logical rule defined in the gate, returns a binary output. There are multiple different types of logic gates:
- **AND**
- **OR**
- **NOT**
- **NAND (NOT-AND)**
- **XOR (Exclusive OR)**
- **XNOR (Exclusive NOR, referred to as the equivalence gate)**
Some of these should be very familiar especially if you've taken some sort of logic course but some of them may be new. For now, we will introduce the 3 most basic gates, **AND**, **OR**, and **NOT**.

*> [!NOTE]
> In the context of logic gates, we will use 0 and 1 for the output with 0 representing False and 1 representing True

### 1.1 Basic Gates  

#### AND Gate

The **AND gate** produces an output of 1 if and only if both of its' inputs are also 1. In boolean algebra this is written as `Y = A · B`. 

#### OR Gate

The **OR gate** produces an output of 1 if **at least** one of its' inputs are 1. In boolean algebra, this is written as `Y = A + B`.

#### NOT Gate

The **NOT gate** is essentially a negation. If the input is 1 then the output is 0. In boolean algebra, this is written as `Y = ¬A`. This is often combined with another gate, more on combinational logic gates later on.

Each of these gates can be represented with a **truth table**, which lists all possible input combinations and their resulting output. Truth tables are the most straightforward way to describe a gate’s behavior mathematically. 

| A | B | AND (A · B) | OR (A + B) | NOT (¬A) |
|---|---|-------------|------------|----------|
| 0 | 0 |      0      |     0      |    1     |
| 0 | 1 |      0      |     1      |    1     |
| 1 | 0 |      0      |     1      |    0     |
| 1 | 1 |      1      |     1      |    0     |

---

### 1.2 Derived Gates  

Beyond the basic gates, digital systems make heavy use of derived gates, which is just a combination of the 3 basic logic gates.

The **XOR (exclusive OR) gate** produces an output of 1 only when its two inputs differ. In Boolean form, it is expressed as `Y = A ⊕ B = A'B + AB'`. If either A or B is true, the output will be 1 but if A and B are true, the output will be 0. This is how XOR differs from a traditional OR.

The **NAND (NOT-AND) gate** and **NOR (NOT-OR) gate** are also essential. NAND produces the opposite of an AND gate, while NOR produces the opposite of an OR gate. What makes these two particularly powerful is that they are **universal gates**: any Boolean function can be built using only NAND gates or only NOR gates. This property has been extremely important in hardware design because fabricating circuits using just one type of gate often simplifies manufacturing.  

Here is a truth table for each of these derived gates:

| A | B | XOR (A ⊕ B) | NAND (¬(A · B)) | NOR (¬(A + B)) |
|---|---|-------------|-----------------|----------------|
| 0 | 0 |      0      |        1        |        1       |
| 0 | 1 |      1      |        1        |        0       |
| 1 | 0 |      1      |        1        |        0       |
| 1 | 1 |      0      |        0        |        0       |

---

## 2. Combinational Logic (§A.3)  

Now that we understand these basic gates, we will expand into combinational circuits. Computers require much more complex circuits and more often than not, there are multiple inputs. A **combinational circuit** is a collection of logic gates executed sequentially, and grouped together. The output depends on the current input, meaning that there is no memory and the circuits output is variable based on conditions. We use these for math, parsing through data, and decoding instruction sets. The derived gates are simplified versions of these combinational gates. 

The combinational circuits that we will discuss this week are **Multiplexers**, **Decoders and Encoders**, and **Adders**.

---

### 2.1 Multiplexers (MUX)  

The first combinational circuit we will discuss are **Multiplexers**, or **MUX** for short. A MUX is essentially like a digital switch that selects an input based on a **control input** and sends this to the output. Here's an analogy: Think of a railroad track where you have 2 seperate tracks combining into one. Only one of these tracks can be attached at the same time. The **control input** is like the lever that switches the track. Based on some condition, the operator pulls the lever and switches the track.

The simplest MUX is the **2-to-1 multiplexer**, which has two data inputs (D0 and D1), one control input (S), and one output (Y). If the control input is 0, the output is equal to D0. If the control input is 1, the output is equal to D1. In Boolean form: `Y = S'D0 + SD1`.  
- The MUX is built from an inverter (to get S'), two AND gates (to combine each data input with the correct select signal), and one OR gate (to combine the results).

>> [!NOTE]
> Multiplexers can operate on both single-bit signals as well as multi-bit buses such as D0 = 1010₂, D1 = 1100₂ making them very useful for real CPU's that use a 32 or 64 bit architecture.

The truth table for a 2-to-1 multiplexer is (Note, the `x` indicates that the input does not affect the output when the select line chooses the other input)

| S | D0 | D1 | Y |
|---|----|----|---|
| 0 |  0 |  x | 0 |
| 0 |  1 |  x | 1 |
| 1 |  x |  0 | 0 |
| 1 |  x |  1 | 1 |

Here is a **4-to-1 multiplexer**, which has 4 data inputs, (D0, D1, D2, and D3), and two select lines, (S1 and S0). Even with the higher dimensionality, the MUX still produces 1 output. Here is the boolean equation: `Y = S1'S0'D0 + S1'S0D1 + S1S0'D2 + S1S0D3`.


The truth table for a 4-to-1 multiplexer is (Note, the `x` indicates that the input does not affect the output when the select line chooses the other input)

- If S1S0 = 00 → Y = D0  
- If S1S0 = 01 → Y = D1  
- If S1S0 = 10 → Y = D2  
- If S1S0 = 11 → Y = D3  

| S1 | S0 | D0 | D1 | D2 | D3 | Y |
|----|----|----|----|----|----|---|
|  0 |  0 |  0 |  x |  x |  x | 0 |
|  0 |  0 |  1 |  x |  x |  x | 1 |
|  0 |  1 |  x |  0 |  x |  x | 0 |
|  0 |  1 |  x |  1 |  x |  x | 1 |
|  1 |  0 |  x |  x |  0 |  x | 0 |
|  1 |  0 |  x |  x |  1 |  x | 1 |
|  1 |  1 |  x |  x |  x |  0 | 0 |
|  1 |  1 |  x |  x |  x |  1 | 1 |

>> [!NOTE]
> An n-to-1 multiplexer requires log₂(n) select lines.

Now, you might be thinking, how is the control input decided? Refering back to our train example, what makes the operator switch the track, what are the conditions? *The control inputs of a MUX are* **signals coming from other parts of the circuit, more often than not from the control unit of the CPU** -> Think back to the **fetch-decode-execute** cycle. The control unit determines what operation needs to happen based on the instruction; Is this addition, is this a branch, etc. These are then turned into control signals which goes into these combinational circuits. Based on these control signals, we select a certain input data.

#### Example

In the CPU, after each instruction the **program counter (PC)** is updated. Depending on the instruction, a different operation occurs. If it is a normal instruction then the next PC should be 4 more than the current PC but if its' a branch instruction, the next PC should be a completely different address representing the branch target. These become the two data inputs:
- If the instruction is not a branch, then the control unit sets `S = 0`, causing the MUX to output `D0 = PC + 4`
- If the instruction is a branch, the control unit sets `S = 0`, causing the MUX to output `D1 = branch target`. This is an example of a *selection circuit*; the select line(s) control **which input** is sent to the output based on some condition.

---

### 2.2 Decoders and Encoders  

Another combinational circuit that we will see frequently are decoders and encoders, with decoders also being selection circuits.

#### Decoder

A **decoder** takes in an n-bit binary input and activates a certain output based on its' value. In total, there are 2ⁿ outputs with *n* being the number of bits. The input essentially tells the circuit which output should be turned on (success, signal of 1 is emmitted) and which outputs should be off (blocked, signal of 0 is emmitted).

For example -> A **2-to-4 decoder** has two inputs, B1 and B0, and four outputs, Y3, Y2, Y1, and Y0. Here is the truth table for reference:

| B1 | B0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
|  0 |  0 |  1 |  0 |  0 |  0 |
|  0 |  1 |  0 |  1 |  0 |  0 |
|  1 |  0 |  0 |  0 |  1 |  0 |
|  1 |  1 |  0 |  0 |  0 |  1 |

Here are the boolean equations for a **2-to-4** decoder: 
- Y0 = B1' · B0' -> `Y0` is active when neither `B1` and `B0` are
- Y1 = B1' · B0  -> `Y1` is active when `B1` is not active and `B0` is
- Y2 = B1 · B0'  -> `Y2` is active when `B1` is active and `B0` is not
- Y3 = B1 · B0 -> `Y3` is active when `B1` and `B0` are both active

> [!NOTE]
> If the input is `10` which is the binary for 2, the corresponding output line 2 becomes active, this can be useful for memory operations as well as interpreting instruction sets.

#### Encoder

An **encoder** does the reverse of a decoder, taking in 2ⁿ input codes, with exactly *1* of them being active, and produces an n-bit binary output that corresponds to this. Encoders and decoders mirror each other.

For example, this would be the truth table for our **4-to-2 encoder**, looks similar to the decoder right:

| Y3 | Y2 | Y1 | Y0 | B1 | B0 |
|----|----|----|----|----|----|
|  1 |  0 |  0 |  0 |  0 |  0 |
|  0 |  1 |  0 |  0 |  0 |  1 |
|  0 |  0 |  1 |  0 |  1 |  0 |
|  0 |  0 |  0 |  1 |  1 |  1 |

Some practical examples of this are a keyboard. Each key is wired to a seperate line where when you press that key, it becomes active and the encoder emits the binary code for that given key. There are multiple different inputs, but you only care about the single key you pressed abd what should happen when you press that *specific key*.

---

### 2.3 Adders  

Arithmetic is at the core of computation, and adders are the simplest circuits that perform it.  

A **half adder** adds two binary inputs, A and B. It produces two outputs: the **sum** (`A ⊕ B`) and the **carry** (`A · B`). For example, adding 1 and 1 produces a sum of 0 with a carry of 1.  

A **full adder** extends this by including a carry-in input, Cin, which allows it to add three binary inputs. The outputs are:  
- Sum = `A ⊕ B ⊕ Cin`  
- Carry = `(A · B) + (Cin · (A ⊕ B))`  

By connecting multiple full adders in sequence, we can create a **ripple-carry adder** capable of adding multi-bit numbers. Each adder passes its carry-out to the next stage as carry-in, which means the carry “ripples” through the circuit. This makes ripple-carry adders conceptually simple but relatively slow for large word sizes, because the carry must propagate through all stages.  

**Worked Example:** Add `1011₂` (11 in decimal) and `0110₂` (6 in decimal) using a ripple-carry adder.  

- Rightmost bit: 1 + 0 = 1 (carry 0).  
- Next bit: 1 + 1 = 0, with carry 1.  
- Next bit: 0 + 1 + 1 (carry) = 0, with carry 1.  
- Leftmost bit: 1 + 0 + 1 (carry) = 0, with carry 1.  

Final result: `0001 0001₂`, or 17 in decimal.  

---

## 3. Sequential Logic (§A.4)  

### 3.1 Why Sequential Logic?  

Combinational circuits are powerful, but they have one limitation: they cannot remember past inputs. Computers, however, require memory to store data, track program execution, and maintain state. To accomplish this, we need **sequential logic circuits**, which use feedback loops to store information across time.  

---

### 3.2 Latches  

The simplest form of sequential logic is the **latch**. A latch can store one bit of information and maintain its output until it is explicitly changed.  

An **SR latch** (Set-Reset latch) is constructed from two cross-coupled NOR gates. It has two inputs, S (set) and R (reset). If S is activated, the latch stores a 1. If R is activated, it stores a 0. If both inputs are inactive, the latch holds its previous state. One problem with this design is that if both inputs are activated simultaneously, the latch enters an invalid or unpredictable state.  

---

### 3.3 Flip-Flops  

To address the limitations of latches, digital systems use **flip-flops**, which are edge-triggered storage elements. A flip-flop changes state only at the transition of a clock signal, typically the rising edge.  

The most common flip-flop is the **D flip-flop**. It has two inputs: D (data) and CLK (clock). On the rising edge of the clock, the value on D is stored and appears on the output Q. Until the next clock edge, the output remains constant, regardless of changes to D. This makes flip-flops predictable and reliable building blocks for sequential circuits.  

Flip-flops allow designers to synchronize circuits with a clock, ensuring that data flows through the system in an orderly fashion.  

---

### 3.4 Registers  

By combining multiple flip-flops, we can create a **register**, which stores a multi-bit value. A 4-bit register, for example, uses four flip-flops, one for each bit. Registers are fundamental components of CPUs, where they store data, instructions, and memory addresses.  

For example, suppose a 4-bit register currently holds the value `1010₂`. If new data `1100₂` is applied to the inputs, the output will not immediately change. Instead, the register will update to `1100₂` only at the next clock edge. This property ensures that all registers in a CPU update simultaneously, keeping the processor synchronized.  

Registers are essential for implementing the program counter, general-purpose registers, and pipeline registers in modern processors.  

---

## 4. Transition to CPU Design (Preview)  

This week’s material introduced the building blocks of digital logic: gates, combinational circuits, and sequential circuits. Combinational circuits enable arithmetic and decision-making, while sequential circuits provide memory and state. Together, these form the foundation of the **datapath** of a CPU.  

In the coming weeks, we will build upon this foundation to explore how these simple components are combined into larger functional units, such as the arithmetic-logic unit (ALU), the control unit, and the memory system. Next week, we will focus on **data representation** — how integers, signed numbers, and floating-point values are encoded in binary — which will prepare us to understand arithmetic in hardware more deeply.  
