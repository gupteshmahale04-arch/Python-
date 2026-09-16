- # Chapter 3 
 - # Strings in Python
1) What is a String?
 - A string is a data type in Python that stores a sequence of characters - letters,
numbers, or symbols - enclosed in single (' '), double (" "), or triple ("' ''')
quotes.
- Examples:
-          str1 = 'Hello'
           str2 = "Saumya Singh"
           str3='''Welcome ''' to Python! 

- Note ::  Strings are immutable, meaning once created, their content cannot
be changed directly.

 # Creating Strings
 - You can create strings in different ways:
-       name = "Samosa"
        greet = 'Hello'
        msg = """Python is fun!"""
- # String Concatenation:
- print ("Hello " + "World")
#Output: Hello World
 - # Length of String:
- len("GulabJamun") # Output: 10 
#  Indexing 
- Each chapter in a string has a position (index )
starting from 0 .
- Example :
-              str = "guptesh ji"
- in which g is in 0 indexing and t is 3 indexing, sphes is also give a indexing 
-        index : 0 1 2 3 4 5 6 7 8 9 
        chars  : G U P T E S H _ J I  

        Str = "guptesh"
        print(str[0])   # g
        print(str[5])   # s
 
#  Strings are immutable
- str[0]="r"  # Error : Strings cannot be changed directly 
   

# Slicing 
- Slicing lets you access a part of a string 
- * syntax :
-          string [ start : end ] # end index is excluded 
 -  Example :
-            
             str = "GulabJamun"
            print (str [0:5])   # Gulab
            print (str [ :6])   # GulabJ
            print(str [5:])     # Jamun
- # Negative Indexing
 
-      G   u  l  a  b  J  a  m  u  n
       10 -9 -8 -7 -6 -5 -4 -3 -2 -1

str = "GulabJamun" 

print(str[-5 :- 1])   # Jamu

# Common String Methods
- Method               | Description                                 | Example
---------------------|---------------------------------------------|-----------------------------------------------
.upper()             | Converts all characters to uppercase        | "samosa".upper() → 'SAMOSA'
.lower()             | Converts all characters to lowercase        | "Saumya".lower() → 'saumya'
.title()             | Capitalizes the first letter of each word   | "hello world".title() → 'Hello World'
.find(sub)           | Returns index of first occurrence           | "banana".find("na") → 2
.replace(old, new)   | Replaces all occurrences                    | "Python is cool".replace("cool", "awesome") → 'Python is awesome'
.count(sub)          | Counts occurrences                          | "mango".count("a") → 1
.endswith(suffix)    | Checks if string ends with given substring  | "coder.".endswith(".") → True
 .capitalize()        | Capitlazes first letter only                | "python".capitalize()  -> Python

 # Formatted Strings (f-Strings)
f-Strings make it easy to include variables inside strings.
Example:
name = "Saumya Singh"
age = 21
print(f"My name is {name} and I am {age} years old.")


Output:
My name is Saumya Singh and I am 21 years old.
# Escape Sequences
Escape sequences allow the use of special formatting in strings.
   Sure! Here's the text content from the image you uploaded, formatted clearly:

| Escape Sequence | Description | Example             |
|-----------------|-------------|---------------------|
| `\n`            | New line    | `"Hello\nWorld"` → prints on two lines |
Escape Sequence | Description     | Example Input → Output 
\t              | Tab space       | "\tA\tB" → adds a tab between A and B
\\              | Backslash       | "C:\\newfolder" → C:\newfolder
\'              | Single quote    | 'It\'s great' → It's great
\"              | Double quote    | "He said \"Hi\"" → He said "Hi"


# 🧠 Mini Project: Emoji Converter 😊
Convert text-based emotions into emojis.
Code Example:
Emoji Converter – Basic Version (No if, no loop)
msg = input("Enter your message: ")

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😢")
msg = msg.replace(":D", "😃")
msg = msg.replace("<3", "❤️")

print(msg)

Example Run:

Enter your message: Hello :) I am learning Python from Samaya :D
Output: Hello 😀 I am learning Python 😃
 
# Extra String Opeeration 

- Concatenation
"Hello" + "Samosa" → 'HelloSamosa'
- Repetition
"Yum! " * 3 → 'Yum! Yum! Yum! '
- Membership
"lo" in "Hello" → True
- Length
len("Samosa") → 6


