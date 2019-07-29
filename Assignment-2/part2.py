# Trees - Ex4
class Node:
	def __init__(self, key=0, value=0, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right
		self.value = value


class BinarySearchTree:
	def __init__(self, root=None):
		self.root = root

	def insert(self, key, value=0):
		self.root = self.__insert_helper(self.root, key, value)

	def __insert_helper(self, node, key, value):
		if not node:
			node = Node(key, value)
		elif key < node.key:
			node.left = self.__insert_helper(node.left, key, value)
		elif key > node.key:
			node.right = self.__insert_helper(node.right, key, value)

		return node

	def find(self, key):
		return self.__find_recursive(self.root, key)

	def __find_recursive(self, node, key):
		if not node:
			return None

		if key == node.key:
			return node
		elif key < node.key:
			return self.__find_recursive(node.left, key)
		else:
			return self.__find_recursive(node.right, key)


# bst = BinarySearchTree()
# bst.insert(4)
# bst.insert(8)
# bst.insert(3)
# # Duplicate values get ignored.
# bst.insert(4)
# bst.insert(5)
# bst.insert(6)
#
# print(bst.find(8).key)
# print(bst.find(9))


# Trees - Ex5
class ListPhoneBook:
	def __init__(self, entry_list=[]):
		self.__entry_list = entry_list
		self.__size = len(entry_list)

	def size(self):
		return self.__size

	def insert(self, name: str, phone_number: int):
		self.__entry_list.append((name, phone_number))
		self.__size += 1

	def find(self, name:str):
		matches = [entry[1] for entry in self.__entry_list if entry[0] == name]
		if matches:
			return matches[0]
		return -1


# list_phone_book = ListPhoneBook()
# list_phone_book.insert("ABC", 1111111111)
# list_phone_book.insert("XYZ", 9999999999)
# list_phone_book.insert("DEF", 2222222222)
#
# print(list_phone_book.find("ABC"))
# print(list_phone_book.find("XYZ"))
# print(list_phone_book.find("PQR"))


class BinarySearchTreePhoneBook:
	def __init__(self):
		self.__bst = BinarySearchTree()
		self.__size = 0

	def size(self):
		return self.__size

	def insert(self, name: str, phone_number: int):
		self.__bst.insert(name, phone_number)
		self.__size += 1

	def find(self, name:str):
		entry = self.__bst.find(name)
		if entry:
			return entry.value
		return -1


# bst_phone_book = BinarySearchTreePhoneBook()
# bst_phone_book.insert("ABC", 1111111111)
# bst_phone_book.insert("XYZ", 9999999999)
# bst_phone_book.insert("DEF", 2222222222)
#
# print(bst_phone_book.find("ABC"))
# print(bst_phone_book.find("XYZ"))
# print(bst_phone_book.find("PQR"))


# Trees - Ex6 (Runtime analysis)
import time


def initialize_data(phone_book):
	with open("data.csv") as csv:
		start = time.time()
		for line in csv:
			[name, phone_number] = line.split(",")
			phone_book.insert(name, phone_number)
		end = time.time()
		print("TIme to insert all entries:- " + str(end - start))


def search_phone_book(phone_book):
	with open("search.txt") as name_file:
		start = time.time()
		for line in name_file:
			[name, _] = line.split("\n")
			if phone_book.find(name) == -1:
				print(name)
				print(ValueError("Value not found."))
				exit()

		end = time.time()
		print("TIme to find all names:- " + str(end - start))


#  BST version
bst_ph_book = BinarySearchTreePhoneBook()
print("BST phone book")
initialize_data(bst_ph_book)
print("BST phone book size: ", str(bst_ph_book.size()))
search_phone_book(bst_ph_book)

print("")
# List version
lst_ph_book = ListPhoneBook()
print("List phone book")
initialize_data(lst_ph_book)
print("List phone book size: " + str(lst_ph_book.size()))
search_phone_book(lst_ph_book)