# -*- coding: utf-8 -*
from __future__ import print_function 
import sys
import math



"""
dct = {
    -1: [0, 60000],
    0: [100, 20, 7],
    100: [30],
    30: [400, 500],
    60000: [70, 80],
    7: [9, 11, 13],
}


def ptree(parent, tree, indent=''):

    if parent != -1:
        print(parent)

    if parent not in tree:
        return

    shift = math.ceil(math.log10(parent)) \
            if parent >= 10 else 1
    indent += ' ' * int(shift)

    for child in tree[parent][:-1]:
        print(indent + '|' + '-' * 4, end='')
        ptree(child, tree, indent + '|' + ' ' * 4)

    child = tree[parent][-1]
    print(indent + '`' + '-' * 4, end='')
    ptree(child, tree, indent + ' ' * 4)


print (" 1")
ptree(-1, dct)
print(dct)

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# B( A( C(0, 1) ), C( 1, A(0) ) )
s_test = "B(A(C(0,1)),C(1,A(0)))"
def to_dct(s):
    stack = Stack()
    dct_test = {}
    for char in s:
        if (char == '('):
            stack.push(char)
            continue
        elif (char == ')'):
            tmp_list = []
            tmp_char = stack.pop()
            while (tmp_char != '('):
                if (tmp_char == ','):
                    tmp_char = stack.pop()
                else:
                    tmp_list.append(tmp_char)
                    tmp_char = stack.pop()
            dct_test[stack.peek()]=tmp_list
        else:
            stack.push(char)
    return dct_test


dct_test = to_dct(s_test)
print (dct_test)
"""

# B( A( C(0, 1) ), C( 1, A(0) ) )
# 1  2  3 4  5     6  7  8 9    

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class Node(object):
    def __init__(self, value="", id=0, children=None):
        self.value = value
        self.children = []
        self.id = id

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.children.append(node2)
node1.children.append(node3)

print (node1.value)
for child in node1.children:
    print (child.value)

if('A'.isupper()):
    print("true")

stack = Stack()
"""
num = 0
id = 0
children = []
def contruct_tree(input_string):
    for i in range(len(input_string)):
        num = 1
        if(input_string[i] == '('):
            stack.push('(')
        elif(input_string[i] == ')'):
            tmp_char = stack.pop()
            num += 1
            child = []
            while(tmp_char != '('):
                if(tmp_char == ','):
                    node = Node(tmp_char, i-num)
                    num += 1
                    stack.pop()
                    child.append(node)
                else:
                    node = Node(tmp_char,i-num)
                    num += 1
                    child.append(node)
            node = Node(stack.peek(),i-num)
            num += 1
        else:
            stack.push(input_string[i])
    #node = Node(char, num)
    #num += 1
    #children.append(node)
    #return children
"""

#s_test = "B(A(C(0,1)),C(1,A(0)))"
s_test = "B(A(C,D),E,F)"
s_test1 = "B(A(C,1D),2E,3F)"

def simple_form(s):
    s_pattern = {}
    key = 0
    tmp_string = ""
    simple_string = ""
    for char in s:
        if char in [',','(',')']:
            if not tmp_string=="":
                s_pattern[key] = tmp_string
                simple_string = simple_string + str(key) + char
                key += 1
            else:
                simple_string = simple_string + char
            tmp_string = ""
        else:
            tmp_string = tmp_string + char
    return  simple_string,s_pattern

s_string,s_pattern = simple_form(s_test1)
print(s_string)
print(s_pattern)

def to_dct(s):
    stack = Stack()
    dct_test = {}
    for i in range(len(s)):
        count = 0
        if (s[i] == '('):
            stack.push(s[i])
        elif (s[i] == ')'):
            print ("i:",i)
            print ("s[i]",s[i])
            tmp_list = []
            tmp_char = stack.pop()
            count += 1
            while (tmp_char != '('):
                if (tmp_char == ','):
                    tmp_char = stack.pop()
                    count += 1
                elif (tmp_char == '*'):
                    if stack.is_empty():
                        break
                    tmp_char = stack.pop()
                    count += 1
                else:
                    tmp_list.append(i-count)
                    tmp_char = stack.pop()
                    count += 1
            count += 1
            print("count",count)
            dct_test[i-count]=tmp_list
            print ("i-count",i-count)
            print ("tmp_list",tmp_list)
           # while not stack.is_empty():
           #     print ("s_test", stack.pop())
        else:
            stack.push(s[i])
        
        for i in range(count):
            stack.push('*')
        #    while not stack.is_empty():
        #        print ("s_test", stack.pop())


    return dct_test

dct_test = to_dct(s_test)
print (dct_test)
print (len(s_test))
print ("-------------")
dct_test1 = to_dct(s_string)
print (dct_test1)
print (len(s_string))

def ptree(parent, tree, s, pattern, indent=''):
    #print ("s:",s)
    if parent != -1:
        if int(s[parent]) in pattern.keys():
            print(pattern[int(s[parent])])
        else:
            print(s[parent])

    if parent not in tree:
        return

    shift = math.ceil(math.log10(parent)) \
            if parent >= 10 else 1
    indent += ' ' * int(shift)

    for child in tree[parent][:-1]:
        print(indent + '|' + '-' * 4, end='')
        ptree(child, tree, s, pattern, indent + '|' + ' ' * 4)
        #print ("child:",child)

    child = tree[parent][-1]
    print(indent + '`' + '-' * 4, end='')
    ptree(child, tree, s, pattern, indent + ' ' * 4)


#ptree(0, dct_test, s_test)
ptree(0, dct_test1, s_string, s_pattern)
print (s_pattern.keys())
"""
children_test = contruct_tree(s_test)
for i in children_test:
    print (i.id)
    print (i.value)
"""