import argparse


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
    for line in lines(open(productions)):
        tmp = line.split("->")
        #print(tmp)
        #print("tmp[0]",tmp[0].strip())
        #print("tmp[1]",tmp[1].strip())

        #F
        for char in tmp[0].strip():
            if char.isupper():
                if not char in f:
                    f.append(char)
        
        #Q
        if tmp[1].strip() not in q:
            q.append(tmp[1].strip())

        # productions
        if tmp[0].strip() in p.keys():
            p[tmp[0].strip()].append(tmp[1].strip())
        else:
            p[tmp[0].strip()] = tmp[1].strip()

    #Qf
    for line in lines(open(finalsymbols)):
        qf.append(line.strip())

    #print (p)
    #print (qf)
    #print (q)
    #print (f)
    return q, qf, f, p


arg_par = argparse.ArgumentParser(description='')

arg_par.add_argument('-f', '--finalsymbols', dest='finals', help='finalsymbols', required='True')
arg_par.add_argument('-p', '--productions', dest='prods', help='productions', required='True')
argse = arg_par.parse_args()

#read(argse.finals, argse.prods)
q, qf, f, p = read(argse.finals, argse.prods)

print ("p----",p)
print ("qf---",qf)
print ("q----",q)
print ("f----",f)

t_a = TreeAutomaton(q, qf, f, p)


# B( A( C(0, 1) ), C( 1, A(0) ) 
input_string = "B(A(C(0,1)),C(1,A(0)))"

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


tmp_string = ""
for char in input_string:
    if char in t_a.P.keys():
        tmp_string += t_a.P[char]
        continue
    tmp_string += char

print (tmp_string)


stack = Stack()
count_left = 0

for char in tmp_string:
    if(char == '('):
        print(1)
        stack.push('(')
    elif(char == ')'):
        print(2)
        cur_string = ""
        cur_string += ')'
        while(stack.peek()!='('):
            cur_string = stack.pop() + cur_string
        cur_string = stack.pop() + cur_string
        cur_string = stack.pop() + cur_string
        if cur_string in t_a.P.keys():
            print("*****",cur_string)
            for i in t_a.P[cur_string]:
                stack.push(i)
    else:
        print(3)
        stack.push(char)

res = ""
while not stack.is_empty():
    res = stack.pop() + res

print (res)