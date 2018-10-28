mylist=[]
num=1
while True:
    if num!="0" and len (mylist)<20:
        num=input("your number:")
        while not num.isdigit():
            num=input("Please only number:") 
        mylist.append(int(num))
    else:
        break
print(mylist)

def  prime_numbers(y):
    count=0
    if y == 2:
        print (y, end=" ")
            
    elif y==0 or y==1:
        print(" ")
    elif y%2!=0:
        for a in range(2, y//2):
            if y % a == 0:
                count = 1
                continue
        if count==0:
            print (y, end=" ")
a=[prime_numbers(y) for y in mylist]