#!/usr/bin/python
# -*- coding: utf-8 -*-
class Node:

    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:

    def __init__(self):
        self.head = None

    def push(self, item):
        if self.head == None:
            self.head = item
        else:
            novo_no = item
            novo_no.next = self.head
            self.head = novo_no

    def pop(self):
        if self.head == None:
            return None
        else:
            aux = self.head
            self.head = self.head.next
            aux.next = None
            return aux

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head

    def top(self):
        if self.head == None:
            return None
        else:
            return self.head

    def size(self):
        aux = self.front
        tamanho = 0
        while aux != None:
            tamanho += 1
            aux = aux.next
        return tamanho