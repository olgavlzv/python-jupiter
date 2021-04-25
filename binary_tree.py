import random


class Tree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class BinarySearchTree:
    root = None


    def insert(self, tree, key, value):
        if tree is None:
            return Tree(key, value)
        if tree.key > key:
            tree.left = self.insert(tree.left, key, value)
        elif tree.key < key:
            tree.right = self.insert(tree.right, key, value)
        else:
            tree.value = value
        return tree


    def search(self, tree, key):
        if tree is None or tree.key == key:
            return tree
        if tree.key > key:
            return self.search(tree.left, key)
        return self.search(tree.right, key)


    def __getitem__(self, key):
        tree = self.search(self.root, key)
        if tree is not None:
            return tree.value
        raise KeyError()


    def   
    
    
     __setitem__(self, key, value):
        if self.root is None:
            self.root = self.insert(self.root, key, value)
        else:
            self.insert(self.root, key, value)
    

    def fill_tree(self, iter, min, max):
        for i in range(iter):
            self.insert(self, random.randint(min, max))


tree = BinarySearchTree()

print("Пожалуйста, введите данные для генерации дерева")
n = int(input("Количество элементов: "))
min_limit = int(input("Минимальный элемент: "))
max_limit = int(input("Максимальный элемент: "))

tree.fill_tree(n, min_limit, max_limit)
print("Дерево из " + str(n) + " элементов от " + str(min_limit) + " до " + str(max_limit) + " было создано")
