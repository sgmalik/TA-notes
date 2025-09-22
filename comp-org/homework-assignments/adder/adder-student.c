// adder.c
// Build:  gcc -std=c11 -Wall -Wextra adder.c -o adder
// Run:    ./adder

#include <stdio.h>
#include <assert.h>

typedef struct { int sum; int carry; } SumCarry;      // for half/full adder
typedef struct { int bits[4]; int carry;} RCAResult; // for ripple-carry adder

// Utilities
int bits_to_bin(const int *bits, int len) {
/*
 * Utility function for converting a list of bits 
 * into a number. Bits should be in ascending order 
 * of powers of two. This function is based on one 
 * of the solutions given in the previous homework.
 */
    int b = 0;
    for (int i = 0; i < len; ++i) {
        b = b * 2 + bits[i];   // same as (b << 1) | bits[i]
    }
    return b;
}

// Helper for printing binary
void print_bin4(int x) {
    for (int i = 3; i >= 0; --i) {
        putchar(((x >> i) & 1) ? '1' : '0');
    }
}

// half_adder, full_adder return `SumCarry struct to mimic returning tuple in python -> Operations relatively the same
SumCarry half_adder(int a, int b) {
  /*
   *This is a *half adder*, which takes two single-bit operands and returns their sum and carry.
   */
    assert(a == 0 || a == 1);
    assert(b == 0 || b == 1);

    SumCarry r;
    r.sum   = (a ^ b);   // XOR
    r.carry = (a & b);   // AND
    return r;
}

SumCarry full_adder(int a, int b, int c_in) {
  /*
   * Here you will implement a *full adder*, constructed from two half adders and an OR gate.
  */
    assert(a == 0 || a == 1);
    assert(b == 0 || b == 1);
    assert(c_in == 0 || c_in == 1);
    
    // COMPLETE THIS FUNCTION, call half_adder TWICE
    
    return r;
}

// ripple_carry_adder returns RCAResult struct with final int in binary plus carry if applicable
RCAResult ripple_carry_adder(unsigned a, unsigned b) {
  /*
   * Here you will implement a 4-bit ripple-carry adder.
   * This takes as arguments two 4-bit (unsigned) binary 
   * numbers. This should return a tuple the first element 
   * of which is the carry out, and the second element of 
   * which is a list of bits in descending powers of two.
  */
    assert(a <= 15); // 4-bit
    assert(b <= 15);

    int a0 = (a >> 0) & 1;
    int a1 = (a >> 1) & 1;
    int a2 = (a >> 2) & 1;
    int a3 = // COMPLETE

    int b0 = (b >> 0) & 1;
    int b1 = // COMPLETE 
    int b2 = // COMPLETE 
    int b3 = // COMPLETE 

    // MAKE 4 CALLS TO full_adder
    SumCarry s0 = // COMPLETE 
    SumCarry s1 = // COMPLETE 
    SumCarry s2 = // COMPLETE 
    SumCarry s3 = // COMPLETE 

    RCAResult r;
    r.bits[0] = s3.sum;  // MSB
    r.bits[1] = s2.sum;
    r.bits[2] = s1.sum;
    r.bits[3] = s0.sum;  // LSB
    r.carry   = s3.carry;

    return r;
}

// DO NOT MODIFY ANY CODE BELOW

// Plus wrapper 
void plus(unsigned a, unsigned b) {
    RCAResult R = ripple_carry_adder(a, b);
    int sum_ = bits_to_bin(R.bits, 4);

    printf("Decimal: %u + %u = %d carry %d.\n", a, b, sum_, R.carry);
    printf("Binary : ");
    print_bin4(a);
    printf(" + ");
    print_bin4(b);
    printf(" = ");
    print_bin4(sum_);
    printf(" carry %d.\n\n", R.carry);
}

// Helper functions for asserting test cases similarly to python, not sure if there is a test framework for C that I should be using
void assertion_sumcarry(SumCarry got, int exp_sum, int exp_carry) {
    assert(got.sum   == exp_sum);
    assert(got.carry == exp_carry);
}

void assertion_RCA(unsigned a, unsigned b, int exp_carry,
                      int e3, int e2, int e1, int e0) {
    RCAResult r = ripple_carry_adder(a, b);
    assert(r.carry   == exp_carry);
    assert(r.bits[0] == e3);
    assert(r.bits[1] == e2);
    assert(r.bits[2] == e1);
    assert(r.bits[3] == e0);
}

int main(void) {
    // Half adder cases
    assertion_sumcarry(half_adder(0,0), 0,0);
    assertion_sumcarry(half_adder(0,1), 1,0);
    assertion_sumcarry(half_adder(1,0), 1,0);
    assertion_sumcarry(half_adder(1,1), 0,1);

    // Full adder cases
    assertion_sumcarry(full_adder(0,0,0), 0,0);
    assertion_sumcarry(full_adder(0,0,1), 1,0);
    assertion_sumcarry(full_adder(0,1,0), 1,0);
    assertion_sumcarry(full_adder(0,1,1), 0,1);
    assertion_sumcarry(full_adder(1,0,0), 1,0);
    assertion_sumcarry(full_adder(1,0,1), 0,1);
    assertion_sumcarry(full_adder(1,1,0), 0,1);
    assertion_sumcarry(full_adder(1,1,1), 1,1);

    // Ripple carry cases
    assertion_RCA(0,  0,  0, 0,0,0,0);  // 0000 + 0000 = 0000
    assertion_RCA(1,  0,  0, 0,0,0,1);  // 0001 + 0000 = 0001
    assertion_RCA(0,  1,  0, 0,0,0,1);  // 0000 + 0001 = 0001
    assertion_RCA(1,  1,  0, 0,0,1,0);  // 0001 + 0001 = 0010
    assertion_RCA(2,  2,  0, 0,1,0,0);  // 0010 + 0010 = 0100
    assertion_RCA(4,  4,  0, 1,0,0,0);  // 0100 + 0100 = 1000
    assertion_RCA(3,  3,  0, 0,1,1,0);  // 0011 + 0011 = 0110
    assertion_RCA(5,  5,  0, 1,0,1,0);  // 0101 + 0101 = 1010
    assertion_RCA(7,  7,  0, 1,1,1,0);  // 0111 + 0111 = 1110
    assertion_RCA(8,  7,  0, 1,1,1,1);  // 1000 + 0111 = 1111
    assertion_RCA(10, 5,  0, 1,1,1,1);  // 1010 + 0101 = 1111
    assertion_RCA(6,  6,  0, 1,1,0,0);  // 0110 + 0110 = 1100
    assertion_RCA(15, 1,  1, 0,0,0,0);  // 1111 + 0001 = 0000, carry 1
    assertion_RCA(14,14,  1, 1,1,0,0);  // 1110 + 1110 = 1100, carry 1
    assertion_RCA(7, 12,  1, 0,0,1,1);  // 0111 + 1100 = 0011, carry 1
    assertion_RCA(9,  9,  1, 0,0,1,0);  // 1001 + 1001 = 0010, carry 1
    assertion_RCA(15,15,  1, 1,1,1,0);  // 1111 + 1111 = 1110, carry 1

    // Plus demo if cases pass
    plus(0, 0);
    plus(1, 1);
    plus(3, 5);
    plus(7, 7);
    plus(10, 10);
    plus(9, 6);
    plus(12, 9);
    plus(15, 15);

    puts("All tests passed.");
    return 0;
}
