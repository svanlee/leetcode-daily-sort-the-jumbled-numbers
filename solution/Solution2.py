from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Create a translation table that maps each digit (0-9) to its corresponding value in the mapping list
        trans_rule = str.maketrans({str(i):str(x) for i,x in enumerate(mapping)})

        # Sort the nums list based on the translated values of its elements
        # The lambda function translates each number in nums according to the translation table
        # and converts the result back to an integer, which is then used as the sorting key
        return sorted(nums, key=lambda x: int(str(x).translate(trans_rule)))