class MaxHeap:
  def __init__(self):
    self.heap = []

  def insert(self, element):
    self.heap.append(element)
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, index):
    parent_index = (index - 1) // 2
    if index > 0 and self.heap[index] > self.heap[parent_index]: 
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self._heapify_up(parent_index)

  def pop_max(self):  
    if len(self.heap) == 0:
      raise IndexError("pop from empty heap")

    max_item = self.heap[0]
    self.heap[0] = self.heap.pop() if len(self.heap) > 1 else 0
    self._heapify_down(0)
    return max_item

  def _heapify_down(self, index):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
      largest = left_index
    if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
      largest = right_index

    if largest != index:
      self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
      self._heapify_down(largest)


if __name__ == "__main__":
  max_heap = MaxHeap()
  max_heap.insert(1)
  max_heap.insert(3)
  max_heap.insert(8)
  max_heap.insert(5)
  max_heap.insert(9)
  max_heap.insert(14)
  max_heap.insert(11)
  max_heap.insert(10)
  max_heap.insert(21)
  print(max_heap.heap)
  # print("Removed max:", max_heap.pop_max())
  # print("New heap:", max_heap.heap)