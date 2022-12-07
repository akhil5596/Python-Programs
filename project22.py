name=["aakil","rohan","ryan"]
marks=[60,40,50]
updatemark=80
marks[1]=updatemark
for i in range(len(marks)-1):
    if marks[i]<marks[i+1]:
        a=marks[i+1]
        marks[i+1]=marks[i]
        marks[i]=a
        b = name[i + 1]
        name[i + 1] = name[i]
        name[i] = b
print(marks)
print(name)
