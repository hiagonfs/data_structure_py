#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insere(self, elemento):
        novo_no = Node(elemento)
        novo_no.proximo = self.head
        if self.head != None:
           self.head.anterior = novo_no
        self.head = novo_no

    def insere2(self, elemento):
      novo_no = Node(valor = elemento)
      novo_no.proximo = self.head
      novo_no.anterior = None
      if self.head is not None:
          self.head.anterior = novo_no
      self.head = novo_no

    def insertAfter(self, prev_node, new_data):
      if prev_node is None:
          return
      new_node = Node(data=new_data)
      new_node.next = prev_node.next
      prev_node.next = new_node
      new_node.prev = prev_node
      if new_node.next is not None:
          new_node.next.prev = new_node

    def tamanho(self):
        count = 0
        temp = self.head
        while(temp != None):
            count = count + 1
            temp = temp.proximo
        return count

    def imprimeSequencia(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.valor)
            node = node.proximo
        nodes.append('NULL')
        values = ' -> '.join(str(v) for v in nodes)
        return values
