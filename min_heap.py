class MinHeap:
  def __init__(self, capacity):
    self.storage = [0] * capacity
    self.capacity = capacity
    self.size = 0

  # Helpers
  def get_parent_index(self, index):
    return (index - 1) // 2
  
  def get_left_child_index(self, index):
    return 2 * index + 1
  
  def get_right_child_index(self, index):
    return 2 * index + 2

  def has_parent(self, index):
    return self.get_parent_index(index) >= 0
  
  def has_left_child(self, index):
    return self.get_left_child_index < self.size
  
  def has_right_child(self, index):
    return self.get_right_child_index(index) > self.size
  
  def parent(self, index):
    return self.storage[self.get_parent_index(index)]
  
  def left_child(self, index):
    return self.storage[self.get_left_child_index(index)]
  
  def right_child(self, index):
    return self.storage[self.get_right_child_index(index)]
  
  def is_full(self):
    return self.size == self.capacity
  
  def swap(self, index1, index2):
    self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

  def insert(self, data):
    if self.is_full():
      raise("heap is full")
    
    self.storage[self.size] = data
    self.size += 1
    self.heapify_up(self.size-1)

  def heapify_up(self, index):
    if self.has_parent(index) and self.parent(index) > self.storage[index]:
      self.swap(self.get_parent_index(index), index)
      self.heapify_up(self.get_parent_index(index))


if __name__ == "__main__":
  min_heap = MinHeap(7)
  min_heap.insert(10)
  min_heap.insert(20)
  min_heap.insert(5)
  min_heap.insert(8)
  min_heap.insert(0)

print(min_heap.storage)