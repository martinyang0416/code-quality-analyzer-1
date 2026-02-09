class TrieNode:
    def __init__(self):
        self.children = [None, None]

def findMaximumXOR(nums):
    if len(nums) < 2:
        return 0
    max_xor = 0
    root = TrieNode()
    # Insert first number into trie
    num = nums[0]
    current = root
    for i in range(30, -1, -1):
        bit = (num >> i) & 1
        if not current.children[bit]:
            current.children[bit] = TrieNode()
        current = current.children[bit]
    # Process remaining numbers
    for num in nums[1:]:
   