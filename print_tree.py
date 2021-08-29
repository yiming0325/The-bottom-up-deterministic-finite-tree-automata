# -*- coding: utf-8 -*
from __future__ import print_function 
import sys
import math
from simple_form import simple_form
from Stack import Stack 


# B( A( C(0, 1) ), C( 1, A(0) ) )
# 1  2  3 4  5     6  7  8 9    

# Write the parent node and child node in the form of a dictionary
def to_dct(s):
    stack = Stack()
    dct_test = {}
    for i in range(len(s)):
        count = 0
        if (s[i] == '('):
            stack.push(s[i])
        elif (s[i] == ')'):
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
            dct_test[i-count]=tmp_list
        else:
            stack.push(s[i])
        for i in range(count):
            stack.push('*')
    return dct_test

# Print out the tree according to the dictionary
# This method is referenced in: https://stackoverflow.com/questions/1649027/how-do-i-print-out-a-tree-structure
def ptree(parent, tree, s, pattern, indent=''):
    if parent != -1:
        if int(s[parent]) in pattern.keys():
            file = open('display.txt','a')
            file.write(pattern[int(s[parent])]+'\n')
            file.close()
        else:
            file = open('display.txt','a')
            file.write(s[parent]+'\n')
            file.close()
    if parent not in tree:
        return
    shift = math.ceil(math.log10(parent)) \
            if parent >= 10 else 1
    indent += ' ' * int(shift)
    for child in tree[parent][:-1]:
        file = open('display.txt','a')
        file.write(indent + '|' + '-' * 4)
        file.close()
        ptree(child, tree, s, pattern, indent + '|' + ' ' * 4)
    child = tree[parent][-1]
    file = open('display.txt','a')
    file.write(indent + '`' + '-' * 4)
    file.close()
    ptree(child, tree, s, pattern, indent + ' ' * 4)


def print_tree(s,s_pattern):
    dct = to_dct(s)
    ptree(0, dct, s, s_pattern)
