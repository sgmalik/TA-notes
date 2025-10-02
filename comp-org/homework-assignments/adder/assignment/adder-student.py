"""
Implementation of a 4-bit ripple-carry adder using full adders
"built" from half adders (with tests and a few conveniences).

EDCI 5004 Computer Organization for Educators
Clayton Cafiero <cbcafier@uvm.edu>
2025-09-21
"""

def bits_to_bin(bits):
    """
    Utility function for converting a list of bits
    into a number. Bits should be in ascending order
    of powers of two. This function is based on one
    of the solutions given in the previous homework.
    """
    b = 0
    for bit in bits:
        b = b * 2 + bit
    return b


def half_adder(a, b):
    """
    This is a *half adder*, which takes two single-bit operands
    and returns their sum and carry.
    """
    assert a in [0, 1]  # ensure arguments are 1-bit
    assert b in [0, 1]
    
    s = (a and not b) or (not a and b)   # XOR
    c = a and b  # AND

    return int(s), int(c)


def full_adder(a, b, c_in):
    """
    Here you will implement a *full adder*, constructed from
    two half adders and an OR gate.
    """
    assert a in [0, 1]  # ensure arguments are 1-bit
    assert b in [0, 1]

    # COMPLETE THIS FUNCTION
    # You should call half_adder() TWICE

    return int(s), int(c)


def ripple_carry_adder(a, b):
    """
    Here you will implement a 4-bit ripple-carry adder.
    This takes as arguments two 4-bit (unsigned) binary
    numbers. This should return a tuple the first element
    of which is the carry out, and the second element of
    which is a list of bits in descending powers of two.
    """ 
    assert 15 >= a >= 0      # ensure arguments are 4-bit
    assert 15 >= b >= 0

    a_0 = (a >> 0) & 1       # isolate individual bits of a
    a_1 = (a >> 1) & 1
    a_2 = (a >> 2) & 1
    a_3 = # COMPLETE THIS
    
    b_0 = (b >> 0) & 1      # isolate individual bits of b
    b_1 = # COMPLETE THIS
    b_2 = # COMPLETE THIS
    b_3 = # COMPLETE THIS

    # MAKE FOUR CALLS TO full_adder() HERE
    s_0, c = # COMPLETE THIS
    s_1, c = # COMPLETE THIS
    s_2, c = # COMPLETE THIS
    s_3, c = # COMPLETE THIS

    # descending powers of two
    return c, [s_3, s_2, s_1, s_0]


def plus(a, b):
    """
    Just a little demo wrapper for the ripple-carry adder.
    You can pass decimal or binary arguments, but they must
    be numeric and not strings.
    """
    carry, bits = ripple_carry_adder(a, b)
    sum_ = bits_to_bin(bits)
    print(f"Decimal: {a} + {b} = {sum_} carry {carry}.")
    print(f"Binary: {a:04b} + {b:04b} = {sum_:04b} carry {carry}.")
    print()      
    

if __name__ == '__main__':

    # DON'T MODIFY ANY OF THE CODE BELOW

    # test against truth table for half adder
    assert half_adder(0, 0) == (0, 0)
    assert half_adder(0, 1) == (1, 0)
    assert half_adder(1, 0) == (1, 0)
    assert half_adder(1, 1) == (0, 1)

    # test against truth table for full adder
    assert full_adder(0, 0, 0) == (0, 0)
    assert full_adder(0, 0, 1) == (1, 0)
    assert full_adder(0, 1, 0) == (1, 0)
    assert full_adder(0, 1, 1) == (0, 1)
    assert full_adder(1, 0, 0) == (1, 0)
    assert full_adder(1, 0, 1) == (0, 1)
    assert full_adder(1, 1, 0) == (0, 1)
    assert full_adder(1, 1, 1) == (1, 1)

    # tests for ripple-carry adder (without carry out / overflow)
    assert ripple_carry_adder(0b0000, 0b0000) == (0, [0, 0, 0, 0])  # 0 + 0 = 0, carry 0
    assert ripple_carry_adder(0b0001, 0b0000) == (0, [0, 0, 0, 1])  # 1 + 0 = 1, carry 0
    assert ripple_carry_adder(0b0000, 0b0001) == (0, [0, 0, 0, 1])  # 0 + 1 = 1, carry 0
    assert ripple_carry_adder(0b0001, 0b0001) == (0, [0, 0, 1, 0])  # 1 + 1 = 2, carry 0
    assert ripple_carry_adder(0b0010, 0b0010) == (0, [0, 1, 0, 0])  # 2 + 2 = 4, carry 0
    assert ripple_carry_adder(0b0100, 0b0100) == (0, [1, 0, 0, 0])  # 4 + 4 = 8, carry 0
    assert ripple_carry_adder(0b0011, 0b0011) == (0, [0, 1, 1, 0])  # 3 + 3 = 6, carry 0
    assert ripple_carry_adder(0b0101, 0b0101) == (0, [1, 0, 1, 0])  # 5 + 5 = 10, carry 0
    assert ripple_carry_adder(0b0111, 0b0111) == (0, [1, 1, 1, 0])  # 7 + 7 = 14, carry 0
    assert ripple_carry_adder(0b1000, 0b0111) == (0, [1, 1, 1, 1])  # 8 + 7 = 15, carry 0
    assert ripple_carry_adder(0b1010, 0b0101) == (0, [1, 1, 1, 1])  # 10 + 5 = 15, carry 0
    assert ripple_carry_adder(0b0110, 0b0110) == (0, [1, 1, 0, 0])  # 6 + 6 = 12, carry 0

    # tests for ripple-carry adder (with carry out / overflow)
    # The carry bit represents the 2^4 (sixteens) bit
    assert ripple_carry_adder(0b1111, 0b0001) == (1, [0, 0, 0, 0])  # 15 + 1 = 0, carry 1
    assert ripple_carry_adder(0b1110, 0b1110) == (1, [1, 1, 0, 0])  # 14 + 14 = 12, carry 1 
    assert ripple_carry_adder(0b0111, 0b1100) == (1, [0, 0, 1, 1])  # 7 + 12 = 3, carry 1
    assert ripple_carry_adder(0b1001, 0b1001) == (1, [0, 0, 1, 0])  # 9 + 9 = 2, carry 1
    assert ripple_carry_adder(0b1111, 0b1111) == (1, [1, 1, 1, 0])  # 15 + 15 = 14, carry 1
    
    # If all tests passed, give a little demo
    plus(0, 0)
    plus(1, 1)
    plus(3, 5)
    plus(7, 7)
    plus(10, 10)
    plus(9, 6)
    plus(12, 9)
    plus(15, 15)
