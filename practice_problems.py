"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for IDS in product_ids: 
        if IDS in seen:
            return True
        else:
            seen.add(IDS)
    return False

product_ids = [2, 4, 2, 3, 5, 8]
print(has_duplicates(product_ids))


# I decided to use a list for this problem instead of a set because a set automatically removes the duplicates. This function loops through
# each unit in the product ids list and returns a true or false whether there are duplicates or not. In this case, it returns true. The 
# function fits the task because it correctly keeps track of numbers it has already seen and returns if they have been repeated or not.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class TaskQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    
task = TaskQueue()

task.add_task("Laundry")
task.add_task("Vaccuum")
task.add_task("Homework")
print(f"Removed: {task.remove_oldest_task()}")


# I used a queue to complete this problem because it follows a first in, first out (FIFO) method. This makes it easy to find the first
# and oldest task to remove from the queue. It keeps the order organized and successfully adds tasks, keeps their order, and removes
# the oldest task.

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class UniqueTracker:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def get_unique_count(self):
        seen = set()
        current = self.head
        while current:
            seen.add(current.value)
            current = current.next
        return len(seen)

tracker = UniqueTracker()

tracker.add(10)
tracker.add(2)
tracker.add(5)
tracker.add(5)
tracker.add(8)
print(tracker.get_unique_count())


# I used a linked list to finish this problem. The linked list cycled and remembered the numbers that it had already seen and added
# them to a set. The set removes the duplicates on its own, and the 'len' function counted the remaining numbers. 