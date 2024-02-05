def isValid(s):
    """function for valid brackets problem"""
    brackets_dic = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    new_string = []
    for i in s:
        if new_string and brackets_dic.get(new_string[-1]) == i:
            new_string.pop()
        else:
            new_string.append(i)
    if new_string:
        return False
    return True


print(isValid("({}[])"))
print(isValid("({}])"))
