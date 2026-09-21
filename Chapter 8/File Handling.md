
# Introduction to File Handling
File handling allows Python programs to store, read, and manage data saved on
the computer - such as notes, logs, student records, or CSV files.
- Real-world uses:
. Saving login logs
· Writing reports
. Storing student data
· Reading configuration files
. Exporting analytics in CSV

# 2 Types of Files
File Type  |Description              |Example Extensions
Text Files  | Human-readable content  |txt, .csv, . log
Binary Files |Data stored in encoded |.png, . jpg, .mp4, .pdf,
form. exe
# Examples:
. A file named notes.txt storing Saumya's Python concepts -> text file
· A file named profile.jpg storing Saumya's photo -> binary file
# Opening Files
Python uses the open() function:
-        file = open("filename", "mode")

#Here's the text extracted from the image you uploaded:

# Common Modes for File Handling

| Mode | Meaning                          |
|------|----------------------------------|
| "r"  | Read (default)                   |
| "w"  | Write (overwrites file)          |
| "a"  | Append (adds at end)             |
| "x"  | Create new file; error if exists |
| "t"  | Text mode                        |
| "b"  | Binary mode                      |

# Example :
-    f=open("notes.txt" ,"r")
     print(f.read())
     f.close()
# 6 Using with Statement
This is the recommended method because it automatically closes the file.
with open("notes.txt", "r") as f:
content = f.read()
Benefits:
. Safer
· Cleaner
. No need for close()

# Automating File Tasks (Copy, Rename, Delete)
Using Python modules:
Think of a module as a toolbox.
Each module gives you tools (functions) that you don't have to write again.
- Copy file
import shutil
shutil. copy("demo.txt", "backup_demo. txt")
 - Rename file
import os




