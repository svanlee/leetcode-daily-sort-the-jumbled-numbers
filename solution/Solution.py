from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Define a function to map a number to its corresponding value based on the mapping array
        def map_number(num):
            mapped_num = ''
            for digit in str(num):
                mapped_num += str(mapping[int(digit)])
            return int(mapped_num)

        # Sort the numbers based on their mapped values
        return sorted(nums, key=map_number)