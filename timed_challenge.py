# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 17. Service Line Simulation
# Simulate a line where values are added at one end and removed from the other.
# Actions: add("A"), add("B"), serve()
# Output: "A"

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class service_queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def serve(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    
serviceQ = service_queue()

# print(f"Serving: {serviceQ.serve()}")
serviceQ.add(1)
serviceQ.add(2)
serviceQ.add(3)
serviceQ.add(4)
serviceQ.add(5)
print(f"Serving: {serviceQ.serve()}")
print(f"Serving: {serviceQ.serve()}")
print(f"Serving: {serviceQ.serve()}")


# I chose a queue structure for my question. For my problem, I needed to make a line-like structure that served the first person in the 
# queue and then removed them afterwards. A queue follows a first in first out (FIFO) method so it acts on the oldest action in the queue 
# first. This type of data structure is also the one I understand most, so I thought it would be best to complete a skill I know well in
# a timed scenario. Because I was more comfortable working with queues, I thought using it for this assignment would be the best decision
# so I could work at a faster pace and have time to make scenarios. I know how to structure the other data structures, but I find myself
# having to look at more resources or past assignments more in order to complete them. Because of the time limit, I didn't get to test out
# my code as much as I wanted to. I am almost certain it works as it was intended, but I am not sure how well it would hold up against
# bigger, more complex demands. I did have to end up looking at a past assignment to remember where to place everything, but I didn't get 
# the time needed to look at any other resources due to the time limit. Without checking over my work, I could have missed a step or made 
# my code less organized than it should be. 