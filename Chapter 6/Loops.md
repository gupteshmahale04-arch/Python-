# Loops in Python
Loops are used to repeat a block of code multiple times. They help perform tasks such as:
- Printing a message several times
- Iterating over lists
- Generating patterns
Example without a loop:
            print("Hello Saumya!")
            print("Hello Saumya!")
            print("Hello Saumya!")

 Instead of writing the same statement multiple times, we can use a loop to make the code more efficient           

 # 🌀 2. while Loop
A while loop runs as long as a condition is True.
🔧 Syntax
             while condition:
                       # code block
Example ::
-        i = 1
          while i <= 5:
               print("Hello, Saumya Singh!")
                 i += 1
Output ::
-     Hello, Saumya Singh!
      Hello, Saumya Singh!
     Hello, Saumya Singh!
     Hello, Saumya Singh!
      Hello, Saumya Singh!

# 3 for Loop
A for loop is used to iterate (go through) sequences like lists, tuples, or strings.
- Syntax:
for element in sequence:
   #code block
- Example:
foods = ["Pizza", "Samosa", "GulabJamun"]
for item in foods:
print("Saumya likes", item)
- Output:
-       Saumya likes Pizza
        Saumya likes Samosa
        Saumya likes GulabJamun
- for Loop with range()
The range() function generates a sequence of numbers. It is often used with loops.
Syntax:
-         for variable in range(start, stop, step):
            # loop body
- Python range() Function
range(start,stop,step)
The range() function is used to generate a sequence of numbers. It accepts up to three parameters:
- start: The number to begin the sequence from. Default is 0.
- stop: The number at which to stop (exclusive).
- step: The increment between each number in the sequence. Default is 1.
- Example : 
          for i in range(1,6):
            print ("Iteration:",i)
- Output : 
            Iteration: 1
            Iteration: 2
            Iteration: 3
            Iteration: 4
            Iteration: 5

#  break, continue, and pass
🔹 break Statemen
The break Statemen stope the loop immediately when it is encoutered 
- Example 
         for num in range (1,10):
         if num == 5:
          break
        print ( num )

  Output  : 1
            2
            3
            4
  
# pass Statement
The pass statement does nothing - it's used as a placeholder when you want to
keep a block empty.
- Example:
            for i in range(1,2) :
              pass 
# 5 Nested Loops
A loop inside another loop is called a nested loop.
Example:
              for i in range(1, 4):
              for j in range(1, 4):
               print(i, j)
Output:
11
12
13
21
22
2.3
31
32
33



        

          