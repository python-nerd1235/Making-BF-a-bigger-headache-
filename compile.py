#to convert a BF program to uanary
def compile(code):
        o='0x'
        for i in code:
            if i=='+':o+='8'
            elif i=='-':o+='9'
            elif i=='.':o+='a'
            elif i==',':o+='b'
            elif i=='>':o+='c'
            elif i=='<':o+='d'
            elif i=='[':o+='e'
            elif i==']':o+='f'
        return o
print(f"number of zeros:{int(compile(input()),16)}")
