#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Fila:

    def __init__(self):
        self.front = None 
        self.rear = None

    def enqueue(self, item):
        aux = Node(item)
        if self.rear == None:
            self.front = aux 
            self.rear = aux
            return
        self.rear.next = aux
        self.rear = aux

    def dequeue(self):
        if self.isEmpty():
            return
        aux = self.front
        self.front = aux.next
        if(self.front == None):
            self.rear = None

    def isEmpty(self):
        return self.front == None 

    def size(self):
        aux = self.front
        tamanho = 0
        while aux != None:
          tamanho += 1
          aux = aux.next
        return tamanho

    def front(self):
        return self.front

    def rear(self):
        return self.rear 
