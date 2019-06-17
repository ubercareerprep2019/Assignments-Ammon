class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def push_back(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = None

        else:
            if self.tail is None:
                self.tail = Node(data)
                self.head.next_node = self.tail
            else:
                new_node = Node(data)
                self.tail.next_node = new_node
                self.tail = new_node
        self.count += 1

    def insert(self, index, data):
        if index >= 0 and index <= self.size():
            if index is 0:
                new_node = Node(data)
                new_node.next_node = self.head
                self.head = new_node
                self.count += 1
            elif index is self.size():
                self.push_back(data)
            else:
                current_node = self.element_at(index - 1)

                new_node = Node(data)
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                self.count += 1

    def pop_back(self):
        if self.head is None:
            return None
        else:
            return_value = None
            if self.tail is None:
                return_value = self.head
                self.head = None
            else:
                current_node = self.head
                while current_node.next_node is not self.tail:
                    current_node = current_node.next_node
                return_value = self.tail
                current_node.next_node = None
                self.tail = current_node
            self.count -= 1

            return return_value

    def element_at(self, index):
        if index >= 0 and index < self.size():
            current_index = 0
            current_node = self.head
            while current_index < index:
                current_node = current_node.next_node
                current_index += 1
            return current_node
        return None

    def erase(self, index):
        if index >= 0 and index < self.size():
            return_value = None

            if index is self.size() - 1:
                return_value = self.pop_back()
            elif index is 0:
                return_value = self.head
                self.head = return_value.next_node
            else:
                current_node = self.element_at(index - 1)
                return_value = current_node.next_node
                current_node.next_node = return_value.next_node

            self.count -= 1
            return return_value
        return None

    def print_all(self):
        current_index = 0
        current_node = self.head
        while current_index < self.size():
            print(current_node.data)
            current_node = current_node.next_node
            current_index += 1

    def has_cylce(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while slow_pointer and fast_pointer:
            slow_pointer = slow_pointer.next_node

            temp_node = fast_pointer.next_node
            if temp_node:
                fast_pointer = temp_node.next_node
            else:
                fast_pointer = None

            if slow_pointer is fast_pointer:
                return True
        return False

def testPushBackAddsOneNode():
    sLink = SLinkedList()
    sLink.push_back(435)
    return sLink.element_at(0).data is 435

def testPopBackRemovesCorrectNode():
    sLink = SLinkedList()
    sLink.push_back(32)
    return sLink.pop_back().data is 32

def testEraseRemovesCorrectNode():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)
    return sLink.erase(3).data is 9081

def testEraseDoesNothingIfNoNode():
    sLink = SLinkedList()
    return sLink.erase(4) is None

def testElementAtReturnNode():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)

    return sLink.element_at(2).data is 79

def testElementAtReturnsNoNodeIfIndexDoesNotExist():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)

    return sLink.element_at(100) is None

def testSizeReturnsCorrectSize():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)
    sLink.insert(3, 123890)

    return sLink.size() is 6


print(testPushBackAddsOneNode())
print(testPopBackRemovesCorrectNode())
print(testEraseRemovesCorrectNode())
print(testEraseDoesNothingIfNoNode())
print(testElementAtReturnNode())
print(testElementAtReturnsNoNodeIfIndexDoesNotExist())
print(testSizeReturnsCorrectSize())

def testCycleInNonCycleList():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)

    return sLink.has_cylce() is False

print(testCycleInNonCycleList())

def testCycleInListWithCycle():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)
    sLink.tail.next_node = sLink.element_at(2)

    return sLink.has_cylce() is True

print(testCycleInListWithCycle())

def isListPalindrome(s_list):
    temp_list = list()

    current_node = s_list.element_at(0)

    while current_node:
        temp_list.append(current_node.data)
        current_node = current_node.next_node

    current_node = s_list.element_at(0)

    while current_node:
        popped_value = temp_list.pop()
        if current_node.data is not popped_value:
            return False
        current_node = current_node.next_node
    return True

def testPalindromeInNonPalindrome():
    sLink = SLinkedList()
    sLink.push_back(435)
    sLink.push_back(15)
    sLink.push_back(79)
    sLink.push_back(9081)
    sLink.push_back(320)

    return isListPalindrome(sLink) is False

print(testPalindromeInNonPalindrome())

def testPalindromeInPalindrome():
    sLink1 = SLinkedList()
    sLink1.push_back("Q")
    sLink1.push_back("A")
    sLink1.push_back("A")
    sLink1.push_back("Q")

    return isListPalindrome(sLink1) is True

print(testPalindromeInPalindrome())