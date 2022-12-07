n1 = int(input("enter number 1"))
n2 = int(input("enter number 2"))
n3 = int(input("enter number 3"))
n4 = int(input("enter number 4"))
if(n1>n2):
    a = n1
else:
    a = n2

    if(n3>n4):
        b = n3
    else:
        b = n4

        if(a>b):
            gr = a
        else:
            gr = b
            print(gr)