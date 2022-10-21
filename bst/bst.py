class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.leftChild != None:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild != None:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def inorder(self):
        if self != None:
            if self.leftChild != None:
                self.leftChild.inorder()
            print(str(self.data), end=" ")
            if self.rightChild != None:
                self.rightChild.inorder()

    def preorder(self):
        if self != None:
            print(str(self.data), end=" ")
            if self.leftChild != None:
                self.leftChild.preorder()
            if self.rightChild != None:
                self.rightChild.preorder()

    def postorder(self):
        if self != None:
            if self.leftChild != None:
                self.leftChild.postorder()
            if self.rightChild != None:
                self.rightChild.postorder()
            print(str(self.data), end=" ")

    def search(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.search(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.search(data)
            else:
                return False

    def delete(self, data, root):
        if self is None:
            return None

        # migra para a sub arvore direta ou esquerda de acordo com o valor do nó
        if data < self.data:
            self.leftChild = self.leftChild.delete(data, root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data, root)
        else:
            # deletar um nó que contem apenas um filho
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data, root)

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data, root)

                temp = self.leftChild
                self = None
                return temp

            # excluir um nó que possui 2 filhos
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data, root)
        return self

    def minValueNode(self, node):
        current = node
        while current.leftChild is not None:
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node
        while current.rightChild is not None:
            current = current.rightChild

        return current


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def preorder(self):
        if self.root is not None:
            print()
            print("Preorder: ")
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print("Inorder: ")
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print("Postorder: ")
            self.root.postorder()

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return False

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data, self.root)


import random

listNodes = []

bstTest = BST()

# gera uma lista aleatoria de numeros
for i in range(10):
    number = random.randint(10, 99)
    if number not in listNodes:
        listNodes.append(number)

print(listNodes)

# insere a lista na arvore
for i in range(len(listNodes)):
    bstTest.insert(listNodes[i])

bstTest.insert(70)

print(bstTest.inorder())
print(bstTest.preorder())
print(bstTest.postorder())

print(bstTest.search(70))

print("Após deletar o nó: ")

bstTest.delete(70)

print(bstTest.inorder())
print(bstTest.preorder())
print(bstTest.postorder())
