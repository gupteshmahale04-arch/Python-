<!--Data Types & Operators  -->
- # {Data Types}
- 
-  Python has several built - in data types .They define the type of variable halds .
-      | Type  |  Example       |  Description  
       __________________________________________________________________
       alse               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not___________________________________________
- * * Note: Use the type() function to check a variable's data type.
-       x=10 
        print(type(x))
        #<class'int'>
- _______________________________________________

- # {Keywords in Python}

- Keywords are reserved words that have special meaning in Python and cannot
be used as variable names.
- Examples of common keywords: 

- and  |   as |  assert  | break  | class 
- continue | def | del | elif | else
- except | False | finally | for | from 
-  global  | if | import  |  in  | is  
- lambda | none | nonlocal | not | or
- pass | raise  | return  | true  | try 
- While  | with | yield 
-______________________________________________
- # {Expected expression}
- In Python, an "Expected expression" error usually means the interpreter or your editor’s linter (like Pylance in VS Code) found a place where it expected a valid Python expression (like a variable, value, or function call) but instead got something invalid or incomplete.

- 
-  # { Explanation}
- 
- * input() takes user input as a string 
- * int() converts it to an integer
- * print() displays the result

-  # {Sintex}
- * 
-  Example:
- 
           print("Counting from 1 to 5:")
           for i in range(1, 6):
           print(i, end=" ")
           print()  # New line   
 - # {Type Conversion }               
- Type conversion means changing one data type to another.
01. Implicit Conversion (Automatic) 

Python automatically converts smaller data types to larger ones to prevent data
loss.
- Example
           x = 5    # int
        y = 2.5    # float
        z = x + y   # Python converts int -+ float
         print(z)   # 7.5
02. Explicit Conversion (Manual)

- Manually convert data types using built-in functions:
         x = "10"
         y= int(x)  # str -> int 
        print(y + 5) # Output: 15


- * * Common functions :int (x) float(x) str(x)
bool(x)

- # {Operators }
- Operators perform operations on variables and values.
-          Type      | Example      |Description
          Arithmetic  |+ - * / % **   |Math operations ( ** for power)
          Comparison   | == != > < >= <= |  Compare values, returns True or False

            Logical |   and , or ,no | Combine conditions

          Assignment | + += -= *= /=  | Assign or modify values