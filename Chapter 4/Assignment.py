# 1. Ask the user for their 3 favorite movies and store them in a list.




FM1=input("Enter the Your 1 favorite movies   ::::   ")

FM2=input("Enter the Your 2 favorite movies   ::::   ")

FM3=input("Enter the Your 3 favorite movies   ::::   ")

FM4=input("Enter the Your 4 favorite movies   ::::   ")

FM5=input("Enter the Your 5 favorite movies   ::::   ")

FM =[ FM1,FM2,FM3,FM4,FM5]



# 2. Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and
# lowest marks using max() and min().

marks = (87, 64, 33, 95, 76)
print(max(marks))

print(min(marks))
# 3. Write a program to check grade based on marks (A/B/C/D) using if-elif-else.
marks=int(input("Enter the markes"))

if marks<=90:
    print("your grade is A+")
elif marks<=80:
    print("your grade is A")
elif marks<=70:
    print("your grade is B+")
elif marks<=60:
    print("your grade is B")
elif marks<=50:
    print("your grade is c+")
elif marks<=40:
    print("your grade is c")
else :
    print("your are fail")

    