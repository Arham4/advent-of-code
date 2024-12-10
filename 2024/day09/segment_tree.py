from typing import Optional

_FREE = 1
_OCCUPIED = 0


class SegmentTree:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2

        self.max_free = 0
        self.prefix_free = 0
        self.suffix_free = 0
        self.total_free = 0
        
        if self.start != self.end:
            self.left = SegmentTree(start, self.mid)
            self.right = SegmentTree(self.mid + 1, end)
        else:
            self.left = None
            self.right = None

            
    def _calculate_max_free(self):
        if self.start == self.end:
            return
            
        self.prefix_free = self.left.prefix_free
        if self.left.total_free == self.left.end - self.left.start + 1:
            self.prefix_free += self.right.prefix_free
            
        self.suffix_free = self.right.suffix_free
        if self.right.total_free == self.right.end - self.right.start + 1:
            self.suffix_free += self.left.suffix_free
            
        self.max_free = max(
            self.left.max_free,
            self.right.max_free,
            self.left.suffix_free + self.right.prefix_free
        )
        
        self.total_free = self.left.total_free + self.right.total_free

            
    def _update(self, index: int, value: int):
        if self.start == self.end:
            self.max_free = value
            self.prefix_free = value
            self.suffix_free = value
            self.total_free = value
            return
            
        if index <= self.mid:
            self.left._update(index, value)
        else:
            self.right._update(index, value)
            
        self._calculate_max_free()

        
    def free(self, index: int):
        self._update(index, _FREE)

        
    def occupy(self, index: int):
        self._update(index, _OCCUPIED)

        
    def find_for_size(self, required_size: int) -> Optional[int]:
        # print(self.start, self.end, self.max_free, required_size, self.prefix_free, self.suffix_free, self.total_free)

        if self.max_free < required_size:
            return None
            
        if self.start == self.end:
            return self.start if self.max_free >= required_size else None
            
        if self.left.max_free >= required_size:
            return self.left.find_for_size(required_size)
            
        if self.left.suffix_free + self.right.prefix_free >= required_size:
            return self.mid - self.left.suffix_free + 1
            
        if self.right.max_free >= required_size:
            return self.right.find_for_size(required_size)
            
        return None