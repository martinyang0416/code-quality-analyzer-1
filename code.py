import sys

def main():
    sys.setrecursionlimit(1 << 25)
    target = ['b', 'e', 's', 's', 'i', 'e']
    m = len(target)
    
    class SegmentTreeNode:
        __slots__ = ['left', 'right', 'start', 'end', 'data']
        def __init__(self, l, r):
            self.left = None
            self.right = None
            self.start = l
            self.end = r
            self.data = [0]*(m+1)
    
    def build(l, r):
        node = SegmentTreeNode(l, r)
        if l == r:
            c = s[l]
 