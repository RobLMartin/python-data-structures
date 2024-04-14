from collections import deque
import time
import threading

class Queue: 
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()
    
  def is_empty(self):
    return len(self.buffer) == 0
    
  def size(self):
    return len(self.buffer)

food_order_queue = Queue()

def place_order(orders):
  for order in orders:
    food_order_queue.enqueue(order)  
    print(food_order_queue.buffer)
    time.sleep(0.5)

def serve_order():
  time.sleep(1)
  while not food_order_queue.is_empty():
    order = food_order_queue.dequeue()
    print("Now serving " + order)
    time.sleep(2)


if __name__ == '__main__':
  orders = ['pizza','samosa','pasta','biryani','burger']
  t1 = threading.Thread(target=place_order, args=(orders,))
  t2 = threading.Thread(target=serve_order)

  t1.start()
  t2.start()

