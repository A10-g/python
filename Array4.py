from array import*
Arr=array("i",[2,1,4,5,7,1])
se=1
c=0
for i in Arr:
    if Arr==se:
        Arr.remove(i)
        break
    c = c + 1
for i in Arr:
    print(i)
print(Arr)
