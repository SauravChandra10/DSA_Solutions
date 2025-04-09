# Problem link: https://leetcode.com/problems/long-pressed-name/description/
# Solution: Two pointers
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0

        while i<len(name) and j<len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1

            elif i>0 and name[i-1] == typed[j]:
                j += 1

            else:
                break

        while j<len(typed) and name[-1] == typed[j]:
            j += 1

        return True if i == len(name) and j == len(typed) else False