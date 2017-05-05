# Lesson 0 - The Very Basics
## Lesson 0 Video
[![Alt text](/L0.png)](https://www.youtube.com/watch?v=6MvrhPKIt6s&feature=youtu.be)
## Installation
Python is a programming langauge that is designed to very straight forward to use. To run python you will need to install it. I recommend the anaconda python package manager, it comes preinstalled with most of what we'll be using.
https://www.continuum.io/downloads. You will also need to install rebound. You can install rebound with the pip command:
```bash
pip install rebound
```

Rebound can also be found here: https://github.com/hannorein/rebound

To use python open a command prompt (windows) or terminal (mac) and type "conda install and type "python", if you installed this correctly your screen should show a >>> prompt and you can type python code directly into the termainal. This mode of writing python is mostly for testing and most coding is done in a .py file to make editting easier.

To create a .py file you will need a text editor, my personal favorite is [Atom](https://atom.io/), followed by [Sublime Text 2](https://sublimetext.com/2), but you can also use a development enviornment or TextEdit (mac) or Notepad (win) if you want. You type your python code into the file, save it as a something.py and then run it.

## Command Line Basics
To run a .py file from your command line interfact (command prompt or terminal) you need to navigate to the directory containing the file. The basic navigation command is change directory or "cd". Here is how you use it:
```bash
cd ..
```
(go up one directory)
```bash
cd directoryname
```
(enter directory)

Once you are in the directory of a .py file you've created you type:
```bash
python filename.py
```
This will run your saved python script.
## Printing
Printing in python is crucial to debugging, to print in python add a line like this to a .py file and then run it.
```python
print(variable)
```
## Lists
Another part of python that we will be using is lists. Lists are declared in this format [1,2,3] and you can access an item with list[#]. 
```python
listNameHere = ["item 0 this is a string because it's in quotes",10,15]
print(listNameHere[0])
```
This will return  
"item 0 this is a string because it's in quotes"
Strings start at index 0, what we would normally think of as item 1 in a list is really string[0].

## Commenting
```python
print("Most lines are run in python")
# But lines starting with a # are commented and ignored.
# Commenting your code is useful to explain what it does when you will be sharing it with others.
# It is bad form to publish uncommented code.
```
[Continue to Lesson 1](https://github.com/UncleIroh/Learning-Rebound/blob/master/Lesson1.md)
