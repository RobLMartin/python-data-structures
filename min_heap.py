class MinHeap:
  def __init__(self):
    self.heap = []

  def insert(self, element):
    self.heap.append(element)
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, index):
    parent_index = (index - 1) // 2
    if index > 0 and self.heap[index] < self.heap[parent_index]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self._heapify_up(parent_index)

  def pop_min(self):
    if len(self.heap) == 0:
      raise IndexError("pop from empty heap")

    min_item = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._heapify_down(0)
    return min_item

  def _heapify_down(self, index):
    smallest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
      smallest = left_index
    if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
      smallest = right_index

    if smallest != index:
      self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
      self._heapify_down(smallest)


if __name__ == "__main__":
  min_heap = MinHeap()
  min_heap.insert(1)
  min_heap.insert(3)
  min_heap.insert(8)
  min_heap.insert(5)
  min_heap.insert(9)
  min_heap.insert(14)
  min_heap.insert(11)
  min_heap.insert(10)
  min_heap.insert(21)
  print(min_heap.heap)
  # print("Removed min:", min_heap.pop_min())
  # print("New heap:", min_heap.heap)