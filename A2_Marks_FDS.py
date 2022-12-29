def avg():
    sum=0
    count=0
    for mark in marklist:
        if mark != -1:
            sum +=mark
            count +=1
    print(f"\n\tthe avarage score of class is : {sum/count}")


def score():
    max=marklist[0]
    min=marklist[0]
    for mark in marklist:
        if mark != -1:
            if mark < min:
                min=mark
            if mark >max:
                max =mark
    print("\n\tthe maximum marks are ",max," and the minimum marks are ",min)


def absent():
    count=0
    for mark in marklist:
        if mark == -1:
            count+=1
    print("\n\tthe number of absent student is ",count)



def frequency():
    freq={}
    high=0
    for mark in marklist:
        if mark != -1:
            if freq.get(mark)==None:
                freq[mark]=1
            else :
                freq[mark]+=1
                high=mark
    print("\n\tthe higest frequency of mark is ",freq.get(high),"which is of marks ",high)
    
n=int(input ("enter the number of student "))
marklist = []
print("(if student is absent enter '-1; )")
for i in range(n):
    print("enter marks for student no .",i+1,":")
    marklist.append(int (input()))
print(marklist)

avg()
score()
absent()
frequency()



