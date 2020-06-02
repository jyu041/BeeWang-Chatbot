# BeeWang-Chatbot
This program's aim is to create a fake artificial intelligence chatbot using simple coding. I probably look stupid for making such ridiculous program, but I don't care, I am going to make something fun. Because I don't know calculus, so this is all I can start from. There will be more features and improvements in the future of this program.
# Dependencies:
 - glob 
 - json
 - string 
 - random 
 - time 
 - os
 - difflib
 - pyttsx3
 - speech_recognition
# Limitations:
I don't know too much about how ram works with python, I am sure it is quite optimized. But this program stores all the "model" data in a dictionary when besing used, I am afraid that OOM(Out Of Memory) Errors could occur when the data set grows to super size. I don't really know how to fix problems like this, but that would only happen if this program gets a lot of users. So it should not be a big problem.
Another limitation is that I believe this program only works on windows, and would stay like that for a while, because I do not know how to use text to speech for MacOS and Linux systems.
# Usage:
To use this program, make sure you have all the dependencies installed first, sadly I did not create a requriements.txt file for quick install for those(could be coming in the future). When the dependencies are installed, you may just double click to run the program or run commands like "python3 main.py", and the program should work perfectly fine. 
To change the folder of whiles stored at, go inside the program and find the variable: "PATH", edit that would different directories.
# ChangeLog:
-- **Version 2:**
* Changed to a seem to more efficient text to speech engine, now using pyttsx3 instead of win32com
* Added new speech to text recognition to the program, so you could talk to it, but requries internet
-- **Version 1:**
* um just the basic thing lol
