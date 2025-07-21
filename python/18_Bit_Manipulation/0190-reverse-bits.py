"""

190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Note:

• Note that in some languages, such as Java, there is no unsigned integer type. 
  In this case, both input and output will be given as a signed integer type. 
  They should not affect your implementation, as the integer's internal binary 
  representation is the same, whether it is signed or unsigned.

• In Java, the compiler represents the signed integers using 2's complement 
  notation. Therefore, in Example 2 above, the input represents the signed 
  integer -3 and the output represents the signed integer -1073741825.



Example 1:

Input: n = 43261596
Output: 964176192

Explanation: 

Integer	    Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

The input binary string 00000010100101000001111010011100 represents 
the unsigned integer 43261596, so return 964176192 of which its 
binary representation is 00111001011110000010100101000000.

Example 2:

Input: n = 2147483644
Output: 1073741822

Explanation: 

Integer	    Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

The input binary string 01111111111111111111111111111100 represents 
the unsigned integer 2147483644, so return 1073741822 of which its 
binary representation is 00111111111111111111111111111110.

Example 3:

Input: n = 4294967293
Output: 3221225471

Explanation: 

Integer     Binary
4294967293  11111111111111111111111111111101
3221225471  10111111111111111111111111111111

The input binary string 11111111111111111111111111111101 represents 
the unsigned integer 4294967293, so return 3221225471 of which its 
binary representation is 10111111111111111111111111111111.

"""

# Solution 2: Bit Manipulation [✔️]
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution: # type: ignore
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res


######## ######## ######## ######## ######## ######## ########


# Solution 3: Bit Manipulation (Optimal)
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        return res & 0xFFFFFFFF