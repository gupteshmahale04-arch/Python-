#  Write code to open a file named my data.txt in read mode 
# file=open("First.py","r")
# data=file.read()
# print(data)

# 2. Write a program to read a text from a given file certificate.txt and find
#  whether it contains the word live. 
# fil=input("enter the name of file ")

# file=open(fil,"r")
# data=file.read()

# data = data.lower()
# word=input("Enter the sherch word  ")
# if word in data:
#     print(f"Yes ",word," is in file ")
# else:
#      print(f"NO ",word," is in file ")
# print(data) 





# 3. What happens if you open a non-existing file in "r" mode?
# file=open("mydata.txt","r")
# data=file.read()
# print(data)

# 4. Open a file called report. txt in write mode.
file=open("First2.py","w") # r ,x,
file.write("Chapter 9 hi")



# 4. Create a file named saumya_info.txt using "x" mode.
file=open("First2.py","x") # r ,x,
file.write("Chapter 9 hi")

# 5. Write opening check whether a program to safely a file exists before 

# 1. Read a file named story. txt and print the full content.
with open("First.py","r") as f :
    
    data =f.read()
    print("File Data",data)
    


# 2. Read only the first line of bio. txt
with open("First.py","r") as f :
    
     line1=f.readline()
     print("Line 1 ",line1)
# 3. Print how many lines are present in notes. txt.
with open("First.py","r") as f :
    
     lines=f.readlines()
     print(lines)
     print(len(lines))
