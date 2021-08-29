# -*- coding: utf-8 -*
import argparse
from Stack import Stack
from simple_form  import simple_form
from print_tree import print_tree
from print_process import print_process
import copy
import normal_form 


class TreeAutomaton:
    def __init__(self, states, final_symbols, ranked_alphabet, productions):
        self.Q  = states 
        self.Qf = final_symbols
        self.F = ranked_alphabet 
        self.P = productions


def lines(file_stream):
    for line in file_stream:
        yield line

def read(finalsymbols, productions):
    q = [] #Q
    qf = [] #Qf
    f = [] #F
    p = {} #P

    #F
    for line in lines(open('operator.txt','r')):
        f_operator = line.strip()
        f.append(f_operator)

    #Q
    for line in lines(open('states.txt','r')):
        tmp_state = line.strip()
        q.append(tmp_state)

    # productions
    for line in lines(open(productions)):
        tmp = line.split("->")
        if(tmp == ['\n']):
            continue
        if tmp[0].strip() in p.keys():
            p[tmp[0].strip()].append(tmp[1].strip())
        else:
            p[tmp[0].strip()] = tmp[1].strip()

    #Qf
    for line in lines(open(finalsymbols)):
        qf.append(line.strip())

    return q, qf, f, p


def run():

    q, qf, f, p = read("finalsymbols.txt", "productions.txt")

    t_a = TreeAutomaton(q, qf, f, p)

    # B( A( C(0, 1) ), C( 1, A(0) ) 
    #input_string = "B(A(C(0,1)),C(1,A(0)))"
    #input_string = "B(A(C(01,1)),C(1,A(01)))"
    input_string = ""
    for line in lines(open('input_string.txt','r')):
        if line=='\n' or line=='':
            continue
        input_string = line.strip()

    # format the input string
    sig, input_string = normal_form.run(input_string)

    if not sig:
        file = open('display.txt','w')
        file.write("False"+'\n')
        file.close()
        print "False"
        return

    # change the leaf node
    tmp_string = ""
    item = ""
    for char in input_string:
        if char not in [')',"(",',']:
            item = item + char
        else:
            if item in t_a.P.keys():
                tmp_string = tmp_string + t_a.P[item] + char
                item = ""
            else:
                tmp_string = tmp_string + item + char
                item = ""

    simple_string, simple_pattern, key = simple_form(tmp_string)



    # judge whether the input tree is accepted
    stack = Stack()

    for char in simple_string:
        if(char == '('):
            stack.push('(')
        elif(char == ')'):
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
                stack.push(str(key))
                simple_pattern[key] = t_a.P[cur_string]
                key += 1
                
        else:
            stack.push(char)

    res = ""
    while not stack.is_empty():
        res = stack.pop() + res

    print("res:",res)
    if res != "":
        if simple_pattern[int(res)] in t_a.Qf:
            file = open('display.txt','w')
            file.write("True"+'\n')
            file.write("***************************************"+'\n')
            file.close()
            print_tree(simple_string,simple_pattern)
            file = open('display.txt','a')
            file.write("***************************************"+'\n')
            file.close()

            print_process(simple_string, simple_pattern, t_a)
            print "True"
        else:
            file = open('display.txt','w')
            file.write("False"+'\n')
            file.close()
            print "False"
    else:
        file = open('display.txt','w')
        file.write("False"+'\n')
        file.close()
        print "False"