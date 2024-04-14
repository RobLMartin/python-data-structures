class MinHeap:
  def __init__(self):
    self.heap = []

  def insert(self, element):
    self.heap.append(element)
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, index):
    parent_index = (index - 1) // 2
    if index > 0 and self.heap[index] <self.heap[parent_index]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self._heapify_up(parent_index)

if __name__ == "__main__":
  min_heap = MinHeap()
  min_heap.insert(5)
  min_heap.insert(3)
  min_heap.insert(8)
  min_heap.insert(1)
  print(min_heap.heap)