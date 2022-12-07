messege = input("enter message: ")
if("aakil" in messege):
    spam = True
elif("akhil" in messege):
    spam = True
else:
    spam = False

if(spam):
    print("this messege is spam")
else:
    print("this message is not spam")