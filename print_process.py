# -*- coding: utf-8 -*
import argparse
from Stack import Stack
from simple_form  import simple_form
from print_tree import print_tree
import copy

def print_process(simple_string, simple_pattern, t_a):
    stack = Stack()
    for index in range(len(simple_string)):
        if(simple_string[index] == '('):
            stack.push('(')
        elif(simple_string[index] == ')'):
            cur_string = ""
            cur_string += ')'
            while(stack.peek()!='('):
                if(stack.peek()==','):
                    cur_string = stack.pop() + cur_string
                else:
                    cur_string = simple_pattern[int(stack.pop())] + cur_string
            cur_string = stack.pop() + cur_string
            cur_string = simple_pattern[int(stack.pop())] + cur_string
            if cur_string in t_a.P.keys():
                for key,value in simple_pattern.items():
                    if(value == t_a.P[cur_string]):
                        stack.push(str(key))
                        break
                stack_tmp = Stack()
                stack_tmp = copy.deepcopy(stack)
                for i in range(index+1,len(simple_string)):
                    stack_tmp.push(simple_string[i])
                tmp_string = ""
                while not stack_tmp.is_empty():
                    tmp = stack_tmp.pop()
                    tmp_string = tmp + tmp_string
                print_tree(tmp_string,simple_pattern)
                # file = open('print_dic.txt','a')
                file = open('display.txt','a')
                file.write("***************************************"+'\n')
                file.close()
        else:
            stack.push(simple_string[index])