# a=[x for x in input().split()]
# for i in a:
#     if i=="and" or i=="or" or i=="of" or i=="to" or i=="in":
#         continue
#     else:
#         c=(i[0]).upper()
#         print(c,end="")

e="t"
while(e=="t"):
    a = [x for x in input().split()]
    for i in a:
        if 'a'<=i<='z' or 'A'<=i<="Z":
            if i == "and" or i == "or" or i == "of" or i == "to" or i == "in":
                continue
            else:
                c = (i[0]).upper()
                print(c, end="")
            e="u"
        else:
            print("Invalid input")