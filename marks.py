n=int(input("total nunber of student present in class:-"))
U=[]
for i in range(n):
    roll=int(input("\nenter the roll no of student:"))
    U.append(roll)
print("\ntotal nunber of student present in class:",U)
    
p=int(input("Enter the total no of students present in class:-"))
P=[]
M=[]
for j in range(p):
    roll=int(input("\nenter the roll no of student present in class:-"))
    P.append(roll)
print("\nEnter the total no of students present in class:-",P)
    
for y in range(p):
    mark=int(input("\nEnter the marks of the student:-"))
    M.append(mark)
print("\nEnter the marks of the student:-",M)
  
#<--to find the average---------------------------------------------------------->
sum=0
for i in range(p):
    sum=sum+M[i]
avg=sum/p
print("\nsum of the marks",sum)
print("\naverage of marks",avg)

#<----------Highest and lowest of the marks------------------------------------->

def highlow():
    high=M[0]
    for i in range(1,p):
        if M[i]>high:
             high=M[i]
    print("Highest value is:",high)


    low=M[0]
    for i in range(1,p):
        if M[i]<low:
             low=M[i]
    print("lowest value is:",low)
 
highlow()    

#----Number of the absent students---------------------------------------------->
R=[]
for i in U:
    flag=0
    for j in(P):
        if i==j:
            flag=1
            break
    if flag==0:
        R.append(i)
print("roll no absent students:",R)
#---------to calculate frequency------------------------------------------------>

def frequency():
    F=[]
    for i in range(p):
        F.append(0)
    for i in range(p):
        for j in range(p):
            if M[i]==M[j]:
               F[i]=F[i]+1
    maxfreq=F[0]

    for i in range(1,p):
        if M[i]>maxfreq:
             maxfreq=M[i]
             maxfreq=i
    print("frequency is:",maxfreq)
            
frequency()
