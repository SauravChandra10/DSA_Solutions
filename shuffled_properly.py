'''
Given an array of 10 numbers, return whether or not the array is shuffled enough.

In this case, if 3 or more numbers appear consecutively (ascending or descending), return false.

Examples
isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4])
output = false
# 1, 2, 3 appear consecutively

isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10])
output = false
# 9, 8, 7, 6 appear consecutively

isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9])
output = true
# No consecutive numbers appear

isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
output = true
# No consecutive numbers appear
Notes
Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).

You will get numbers from 1-10.
'''

def shuffled_properly(arr):
    for i in range(len(arr)-2):
        # check increasing
        if arr[i] < 9 and arr[i+1] == 1+arr[i] and arr[i+2] == arr[i]+2:
            return False 
        
        # check decreasing
        if arr[i] > 2 and arr[i]-1 == arr[i+1] and arr[i]-2 == arr[i+2]:
            return False
    
    return True

# Test cases
test_cases = [
    # From your examples
    ([1, 2, 3, 5, 8, 6, 9, 10, 7, 4], False),  # 1,2,3 appear consecutively
    ([3, 5, 1, 9, 8, 7, 6, 4, 2, 10], False),  # 9,8,7,6 appear consecutively
    ([1, 5, 3, 8, 10, 2, 7, 6, 4, 9], True),   # No consecutive numbers
    ([1, 3, 5, 7, 9, 2, 4, 6, 8, 10], True),   # No consecutive numbers   
    # Additional test cases
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], False),  # All decreasing
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),  # All increasing
    ([5, 6, 7, 1, 2, 3, 8, 9, 10, 4], False),  # Multiple sequences
    ([2, 4, 6, 8, 10, 9, 7, 5, 3, 1], True),   # Alternating up then down
    ([2, 1, 4, 3, 6, 5, 8, 7, 10, 9], True),   # Pairs in decreasing order
    ([3, 4, 1, 7, 8, 9, 2, 5, 6, 10], False),  # 7,8,9 in middle
    ([10, 8, 6, 4, 2, 1, 3, 5, 7, 9], True),   # No consecutive triplets
    ([4, 5, 2, 3, 6, 1, 9, 8, 7, 10], False),  # 9,8,7 at end
]

for i, (arr, expected) in enumerate(test_cases):
    result = shuffled_properly(arr)
    print(f"Test {i+1}: {arr}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"{'PASSED' if result == expected else 'FAILED'}")
    print("-" * 40)