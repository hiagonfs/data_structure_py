#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insere_inicio(self, elemento):
        elemento.proximo = self.head
        self.head = elemento

    def insere_final(self, elemento):
        novo_no = elemento
        if self.head is None:
            self.head = novo_no
            return
        temp = self.head
        while temp.proximo != None:
            temp = temp.proximo
        temp.proximo = novo_no

    def inserePorPosicao(self, elemento, posicao):
        pass


    def remove2(self, valor):
      current = self.head
      previous = None
      found = False
      while not found:
          if current.valor == valor:
              found = True
          else:
              previous = current
              current = current.proximo
      if previous == None:
          self.head = current.proximo
      else:
          previous.proximo = current.proximo
  
    def remove1(self, valor):
        temp = self.head
        if (temp != None):
            if (temp.valor == valor):
                self.head = temp.proximo
                temp = None
                return
        while(temp != None):
            if temp.valor == valor:
                break
            prev = temp
            temp = temp.proximo
        if(temp == None):
            return
        prev.proximo = temp.proximo
        temp = None

    def pesquisa(self, valor):
        current = self.head
        encontrou = False
        while current != None and not encontrou:
            if current.valor == valor:
                encontrou = True
                return encontrou
            else:
                current = current.proximo
        return encontrou

    def pesquisaRetornaPosicao(self, valor):
        current = self.head
        posicao = 0
        while current != None:
            if current.valor == valor:
                posicao += 1
                return posicao
            else:
                current = current.proximo
                posicao += 1
        return posicao

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

    def valorMinino(self):
        min = 32767
        while self.head != None:
            if min > self.head.valor:
                min = self.head.valor
            self.head = self.head.proximo
        return min

    def valorMaximo(self):
        max = self.head.valor
        atual = self.head
        while atual.proximo != None:
          if atual.valor > max:
            max = atual.valor
          atual = atual.proximo
        return max 
    
    def decrescente(self):
        if self.head == None: return
        aux = self.head
        while aux.proximo != None:
            if aux.valor <= aux.proximo.valor:
                return False
        aux = aux.proximo
        return True 

    def crescente(self):
        if self.head == None: return
        aux = self.head
            while aux.proximo != None:
                if aux.valor >= aux.proximo.valor:
                    return False
                aux = aux.proximo
        return True
