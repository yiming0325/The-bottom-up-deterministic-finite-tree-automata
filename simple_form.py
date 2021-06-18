# Simplify the input string, and then return the simplified string and the corresponding dictionary.
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