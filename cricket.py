U=[]
A=[]
B=[]
C=[]
n=int(input("Enter strengths of student"))
for i in range (1,n+1):
    U.append(i)
a=int(input("Enter no of student like cricket"))
for i in range (a):
    A.append(int(input("Enter roll no of cricket player")))
b=int(input("Enter no of student like badminton"))
for i in range (b):
    B.append(int(input("Enter roll no of badminton player")))
c=int(input("Enter no of student like football:-"))
for i in range (c):
    C.append(int(input("Enter roll no of football player:-")))
print("Cricket player are=",A)
print("badminton player are=",B)
print("football player are=",C)

# play both cricket and badminton----------------------------------------------
R1=[]
def result1(A,B):
    for i in range(a):
        for j in range(b):
            if A[i]==B[j]:
                R1.append(A[i])
    print("who play both cricket and badminton:-",R1)
    return R1
result1(A,B)            

#Cricket or badminton but not both---------------------------------------------
T1=[]
for i in range(a):
    T1.append(A[i])
    
for i in range(b):
    flag=0
    for j in range(a):
        if B[i]==A[j]:
            flag=1
            break
    if flag==0:
        T1.append(B[i])

T2=[]
def result2(T1,R1):
    for i in range(len(T1)):
        flag=0
        for j in range(len(R1)):
            if T1[i]==R1[j]:
                flag=1
                break
        if flag==0:
            T2.append(T1[i])
    print("students who play cricket or badminton but not both:-",T2)
    return T2
result2(T1,R1)

#neithr badminton nor cricket--------------------------------------------------
T3=[]
def result3(U,T1):
    for i in range(n):
        flag=0
        for j in range(len(T1)):
            if U[i]==T1[j]:
                flag=1
                break
        if flag==0:
            T3.append(U[i])
    print("Student who play neither cricket nor badminton:-",T3)
    return T3
result3(U,T1)

#Student who play cricket and football but not badminton-----------------------
T4=[]
for i in range(a):
    T4.append(A[i])
for i in range(c):
    flag=0
    for j in range(a):
        if C[i]==A[j]:
            flag=1
            break
    if flag==0:
        T4.append(C[i])
T5=[]
def result4(T4,B):
    for i in range(len(T4)):
        flag=0
        for j in range(b):
            if T4[i]==B[j]:
                flag=1
                break
        if flag==0:
            T5.append(T4[i])
    print("Student who play cricket and football but not badminton:-",T5)
    return T5
result4(T4,B)
