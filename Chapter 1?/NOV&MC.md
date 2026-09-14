<!-- Variables & Mamory Concept -->
{ Variabales }
- 
- Variabales =>name that stores a value in memory
-  * in Python variabul  are ues to store data that can be referenced and manipulated during program execution
- 
-  * Example : 
-              x=10  
-              y ="hello "
- 
- 
- * Python automatically decides  the data type 
- 
- * Variables are references (Labels) pointing to memory object 
- 
- * Use id () check memory location : print(id(x))  
- 
- * A variabales name can be composed by characters, numbers , the "_" underscore character . it can't start with a number . These are all valid variable names:
-  
- * *  name1 
- * * AGE
- * * aGE 
- * * a111111
- * * my_name  
- * * __name 
- *  These are invalid variable names :
- * * 123
- * * test!
- * * name%
- 
- * Other then anything is valid unless it's a python keyword .There are some keyword like  if , for , while ,import.
- 
{Teking User Input}
- 

- * Use input () to get user iput
 
 - * Example :
 -      name = input ("Enter your name :")
 -      print( "hello" , name )

 - 
 - input()always returns string
 -  
 - * Convert it before performing calculation 
 - 
 - * for the intiger [age  = int(input('Enter Your Age :'))  ]
  
- 
{Expressions}
- 
- * Combination of Operators and Operants
- 
- * x = 10 (not expression )
- 
- * x+3( Expression  . 2[x and 3 ] Operands and 1 [ + ] Operator and result value ) 

- 
{ Statement }
- 
- *  A statment on the other hand in operation on a value ,for example these are 2 Statement : 
-      name = " ram "
-     print(name )
- 
- * If in one line many statement aer write for this use [ ; ]
- 
- * Example:
 -           a = 2 ; b = 4 print(a+b)
 -           name  = "ram "; print(name )
 - 
 { Comment }
 - 
 - * IN python programing everything after a hash mark "#" is ignored and considered a comment .
 - 
 - * Comment is a provaid same information for a code 
 - * Example  :

 -        #this is a addition code of two number
          
         A=int(input("Enter 1st no.:")) 
         
         B=int(input("Enter 2ed no.:"))
         
         Print=("Addition is the;"A+B)
- Shortcut Of Comment {{CTRL+/}}  
            

{ Indentation }
- 
- *  Indentation in Python is meaningful
- * in the othet lenguages it is not meaningful
- *  You cannot indent randomly like this :
  -         name = "guptesh"
            ....print(name) 

- * Everything indented belongs to a block like a control statment or condition block or function or class body .Well  see more about those later on.  

- 
- * Assignment 2 
- 
- *  * Assignment 2 => W A P to Calculate the Area of a circule using user inpurt 
-           # Area Of Circule 
            D = int ( input ("Enter the Diameter :"))
            print("Diameter is :",D)
            area=2*3.12*D
            print(" Area of a circule :" ,area)

