from Stack import Stack

#input_string = "B( ( A (C(0,* 1))),C(1, A ( 0 )) )"

# Check the number of brackets
def check_brackets(s):
    stack = Stack()
    for char in s:
        if char == '(':
            stack.push(char)
        if char == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

# Check for special characters
def check_symbols(s):
    for char in s:
        if char.isdigit() or char.isalpha() or char.isspace():
            continue
        elif char in [',','(',')']:
            continue
        else:
            return False
    return True

# Remove spaces
def remove_space(s):
    tmp_string = ""
    for char in s:
        if char == ' ':
            continue
        else:
            tmp_string = tmp_string + char
    return tmp_string


#res = check_brackets(input_string)
#res = check_symbols(input_string)
#res = remove_space(input_string)
#print(res)

def run(s):
    s = remove_space(s)
    sig1 = check_brackets(s)
    sig2 = check_symbols(s)
    print("s:",s)
    if sig1 and sig2:
        return True,s
    else:
        return False,s
