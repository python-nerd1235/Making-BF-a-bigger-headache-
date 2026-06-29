from ONL import ONL
o=None
fine=input('>')
with open(fine+'.bf','r') as f:
    o=ONL.compile(f.read())
    print(f'hex: {o}\nnumber: {int(o, 16)}')
with open(fine+'.bfhex','w') as f:
    f.write(str(o))
    print('Done.')