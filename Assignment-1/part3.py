# Ammon S Mugimu
# Uber Career Prep 2019
# Assignment-1

# Question 1: Stacks
class Stack:
    def __init__(self):
        self.list = []

    def push(self, integer):
        if type(integer) == int:
            if self.isEmpty():
                self.list.append((integer, integer))
            else:
                min_val = self.list[-1][1]
                if integer < min_val:
                    self.list.append((integer, integer))
                else:
                    self.list.append((integer, min_val))
        else:
            raise Exception("Input should be an integer.")

    def pop(self):
        if not self.isEmpty():
            top_item = self.list.pop(-1)
            return top_item[0]
        else:
            raise Exception("The Stack is empty.")

    def top(self):
        if not self.isEmpty():
            top_item = self.list[-1]
            return top_item[0]
        else:
            print("The Stack is empty and has no 'top'.")
            return None

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def min(self):
        if self.isEmpty():
            print("INVALID: The stack is empty")
            return None
        top_item = self.list[-1]
        return top_item[1]


# Test for more pops than pushes to the stack.
# 4 pushes and 5 pops
# myStack = Stack()
#
# myStack.push(32)
# myStack.push(512)
# myStack.push(-12)
# myStack.push(0)
#
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()


# Question 2: Queues.

class Queue:
    def __init__(self):
        self.inputStack = Stack()
        self.outputStack = Stack()
        self.rear_value_in_output_stack = None

    def enqueue(self, integer):
        self.inputStack.push(integer)

    def dequeue(self):
        if self.outputStack.isEmpty():
            self.refill_output_stack()
        return self.outputStack.pop()

    def front(self):
        if self.outputStack.isEmpty():
            self.refill_output_stack()
        return self.outputStack.top()

    def rear(self):
        if self.inputStack.isEmpty():
            if not self.outputStack.isEmpty():
                return self.rear_value_in_output_stack
            else:
                print("INVALID: The Queue is empty.")
                return None

    def refill_output_stack(self):
        rear_value_counter = 0
        while not self.inputStack.isEmpty():
            current_value = self.inputStack.pop()
            if rear_value_counter < 1:
                self.rear_value_in_output_stack = current_value
                rear_value_counter += 1

            self.outputStack.push(current_value)

    def min(self):
        if self.inputStack.isEmpty() and self.outputStack.isEmpty():
            print("INVALID: The Queue is empty")
            return None
        elif self.outputStack.isEmpty() and not self.inputStack.isEmpty():
            return self.inputStack.min()
        elif self.inputStack.isEmpty() and not self.outputStack.isEmpty():
            return self.outputStack.min()
        else:
            input_stack_min = self.inputStack.min()
            output_stack_min = self.outputStack.min()
            return min(input_stack_min, output_stack_min)

# This tests the O(n) shift of all items in inputStack to outputStack
# that happens when the outputStack Stack is empty.

myQueue = Queue()


myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(1)
myQueue.enqueue(4)
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.front())
#
# Testing myQueue.min().
#
# Empty queue.
# print(myQueue.min())

# Test case with values in both stacks.
myQueue.enqueue(12)
myQueue.enqueue(89)
myQueue.front()
myQueue.enqueue(32)
myQueue.enqueue(54)
print(myQueue.min())
