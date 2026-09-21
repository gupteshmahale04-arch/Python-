file=open("First.py","r")
data=file.read()

print("Data of the file is  ",data)

# Reading file 
file=open("First.py","r")
data=file.read()
file.close()

# with keyword(Read entire file )
with open("First.py","r") as f :
    data =f.read()
    print("File Data",data)

# Read line by line 
with open("First.py","r") as f :
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    line15152=f.readline()
    print("Line 1 ",line1)
    print("Line 2 ",line2)

    print("Line 3 ",line3)
    print("Line 15152 ",line15152)

    # Read all lines 
with open("First.py","r") as f :
    lines =f.readlines()
    print(lines)
    

    #  Rename the file 