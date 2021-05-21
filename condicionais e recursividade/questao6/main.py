k  = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x2-x1)**2+(y2-y1)**2)**(1/2) < k:
    print('*miau* ta bom, vou buscar')
elif ((x2-x1)**2+(y2-y1)**2)**(1/2) == k:
    print('pfff... ta bom')
else:
    print('ta achando que eu sou cachorro?')
