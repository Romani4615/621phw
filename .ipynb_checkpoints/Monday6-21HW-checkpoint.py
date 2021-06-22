{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Week 2 - Monday Lesson (variable assignment, loops, lists)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tasks Today:\n",
    "\n",
    "1) Int & Float assignments <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>\n",
    "2) String Input-Output <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>\n",
    "3) <b>In-Class Exercise #1</b> <br>\n",
    "4) If Statements <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>\n",
    "5) <b>In-Class Exercise #2</b> <br>\n",
    "6) Elif Statements <br>\n",
    "7) Else Statements <br>\n",
    "8) <b>In-Class Exercise #3</b> <br>\n",
    "9) For Loops <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>\n",
    "10) While Loops <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>\n",
    "11) Built-In Functions <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>\n",
    "12) Try and Except <br>\n",
    "13) Lists <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>\n",
    " &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Int & Float Assignments"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Assigning int"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-9dd2a3966788>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m     \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "# syntax clue for variable assignment is. a **single equal sign**\n",
    "# =\n",
    "# two main datatypeds for numbers\n",
    "# ints and floats\n",
    "# ints are intigers\n",
    "# floats are decimal numbers\n",
    "x = 1\n",
    "# If you want to check the trype of a variable\n",
    "# use the built in function]\n",
    "# Functions\n",
    "#  to. call them is just name_of_function\n",
    "# syntax clue. that a function is bring called is parenthesis right after a weord/name\n",
    "# function. arguments (or inoput variables, or. parameters) neccesary input/info the function needs. to run properly\n",
    "# in this case for type,  it needs a. variable to tel you what type of variable. it is.\n",
    "type(x)\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Assinging float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "<class 'int'>\n",
      "change type!\n",
      "<class 'int'>\n",
      "<class 'int'>\n",
      "change type!\n",
      "<class 'float'>\n",
      "4.0\n"
     ]
    }
   ],
   "source": [
    "# same as int\n",
    "y = 3\n",
    "# conversion float to into and int to float\n",
    "#print(type(y)) #passed y, the return of the. type. function\n",
    "#print('change type!')\n",
    "#int(y)\n",
    "#print(type(y))\n",
    "#why isnt it changing?\n",
    "#some data types can not. be changed\n",
    "# the changeability of. a data type is called its mutabilkity\n",
    "# a data type is. eiyther mutable or. immutable meaning it5 can or cannot be changes\n",
    "\n",
    "#so wat do we do if I want to change the variable that is a mutable data type?\n",
    "# Reassign the variable!\n",
    "#variabkle reassignment is the same as variable reassignment\n",
    "# single equals sign =\n",
    "# however you can use the od value of the variable in ther variable reassignment\n",
    "y = y + 1\n",
    "print(y)\n",
    "\n",
    "# so lets change the type. by. reassignment\n",
    "print(type(y))\n",
    "print('change type!')\n",
    "int(y)\n",
    "print(type(y))\n",
    "print(type(y))\n",
    "print('change type!')\n",
    "y = float(y)\n",
    "print(type(y))\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Performing Calculations on ints and floats"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Addition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# adding a float and int gives you a float\n",
    "z = x + y\n",
    "z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Subtraction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-3.0"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x - y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Multiplication"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x * y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Division"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we have 3 kinds of division in python\n",
    "# normal division\n",
    "#gives you a float\n",
    "4/1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Floor Division"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Floor division gives you the next lowest intiger\n",
    "# Results of division not including remainder\n",
    "# //\n",
    "# gives you an int\n",
    "12//5\n",
    "a = 49\n",
    "b = 12\n",
    "a//b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Modulo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The modulo gives you the remainder of divison\n",
    "# % percent sign\n",
    "12%5\n",
    "a%b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Exponential"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "191581231380566414401"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# **\n",
    "4**2\n",
    "a**b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-12.0"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# You can combine these math operations any way you want\n",
    "# follows the order of. operations\n",
    "12 + (1**41230 - 14/2)*4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### String Input-Output"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### String Assignment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello1 a sentence.!!#$%^$'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Strinsgs are another of our main data ttypes\n",
    "# Srings are in fact immutable(unchangeable)\n",
    "# Whenever we tghink we're changing a string we're actually throwing out the old ne and putting a ne3w one in it's place\n",
    "#isngle or double quotes is our syntax clue for strings\n",
    "#strings work with unicode characters and can be numbers or letters\n",
    "\n",
    "a_string = 'hello1 a sentence.!!#$%^$'\n",
    "a_string"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### print() <br>\n",
    "<p>Don't forget about end=' '</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ott\n",
      "er\n",
      "otter\n"
     ]
    }
   ],
   "source": [
    "# we've all seen print at this point\n",
    "# accepts a variable. or a piece of dat and prints it out to your terminal\n",
    "#print is only useful for development, it wont display things tyo a user\n",
    "#it's primary. use is for developers to actually see what's happening and give. themselves more information\n",
    "\n",
    "#end is an optional argument (or optiuonal parameter)\n",
    "#multiple arguments passed into a function are seperated by comas\n",
    "print('ott\\ner', end='\\n')\n",
    "print('otter')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### String Concatenation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello1 a sentence.!!#$%^$ wow(owen_wilson)\n",
      "hello1 a sentence.!!#$%^$\n",
      "hello1 a sentence.!!#$%^$ wow(owen wilson)\n"
     ]
    }
   ],
   "source": [
    "# you can add strings together\n",
    "# (it's making a whole new sring when you do)\n",
    "\n",
    "print(a_string + ' wow(owen_wilson)' )\n",
    "print(a_string)\n",
    "a_string += ' wow(owen wilson)' #same as a_string = a_string + ' wow(owen wilson)'\n",
    "print(a_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Type Conversion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-55-96b29d8894d0>, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-55-96b29d8894d0>\"\u001b[0;36m, line \u001b[0;32m5\u001b[0m\n\u001b[0;31m    a_number. = 7.2\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#. learning how to work with string conversion is valuble\n",
    "# especially strinf to list of characters of string. to list of worjkds but more on that when we get to lists (below)\n",
    "#if you have a number or a string of numbers you can convert between those\n",
    "# str()\n",
    "a_number. = 7.2\n",
    "str_num = str(a_number)\n",
    "str_num"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tell me somethingotter\n",
      "The input given was otter\n"
     ]
    }
   ],
   "source": [
    "# input function asks. user/dev for. input from the console\n",
    "# you can save the. result of thta input as a variable\n",
    "# parameters is what is shown in the console when asking for the. input variable\n",
    "save_input = input('tell me something')\n",
    "print(f'The input given was {save_input}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### format()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is an f-string with !otter!: 15.5! Wow.\n",
      "we're making a formatted string with   a placeholder -> otter okay\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'the time is 11:54:AM:'"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# you may have seen that f' and {} above\n",
    "# thats why an f-string, the modern way of formatting a string\n",
    "# f-strings. and. formatted strings in general let you place variables/other data inside od strings for a display\n",
    "# Variable names or data goes inside curly brackets {}\n",
    "numses = 15.5 #<=float '15.5' = string\n",
    "animal = 'otter'\n",
    "\n",
    "an_f_string = f'This is an f-string with !{animal}!: {numses}! Wow.'\n",
    "print(an_f_string)\n",
    "\n",
    "#alternative to f-strings is format()\n",
    "# string.format()\n",
    "a_str = \"we're making a formatted string with {other} a placeholder -> {placeholder} okay\" #no point for \"okay\"\n",
    "print(a_str.format(placeholder='otter', other=' ')) #named arguments can be in different orders\n",
    "# vs. positional arguments\n",
    "hour = 11\n",
    "minute = 54\n",
    "'the time is {}:{}:{}:'.format(hour, minute,'AM')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Old Way (python 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# In-Class Exercise 1 <br>\n",
    "<p>Create a format statement that asks for color, year, make, model and prints out the results</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# define four variables that will hold values you ask for using input() function\n",
    "# use formatted string to print out a sentence about the car\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### If Statements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Available operators: Greater(>), Less(<),Equal(==)\n",
    "# Greater or Equal(>=), Less or Equal (<=)\n",
    "\n",
    "# Truth Tree:\n",
    "# T && F = F\n",
    "# T && T = T\n",
    "# T || F = T\n",
    "# F || T = T\n",
    "# F || F = F"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 'is' keyword"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 'in' keyword"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 'not in' keyword'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# In-Class Exercise 2 <br>\n",
    "<p>Ask user for input, check to see if the letter 'p' is in the input</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Using 'and'/'or' with If Statements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Elif Statements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Else Statements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# see above"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### For Loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Using 'in' keyword"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# see above"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Continue Statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# will continue to next iteration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Break Statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# will break out of current loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Pass Statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mostly used as a placeholder, and will continue on same iteration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Double For Loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### While Loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Looping 'While True'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### While & For Loops Used Together"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Built-In Functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### range()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### help()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### isinstance()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### abs()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Try and Except"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Lists"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Declaring Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Indexing a List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### .append()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### .insert()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### .pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "##### .remove()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### del()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Concatenating Two Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n"
     ]
    }
   ],
   "source": [
    "a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "cube = []\n",
    "for i in a_list:\n",
    "    cube.append(i*i*i)\n",
    "print(cube)\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Lists Within Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of 3**4 is : 81\n"
     ]
    }
   ],
   "source": [
    "n = 1\n",
    "for i in range(1,5):\n",
    "    n=3*n\n",
    " \n",
    "print (\"The value of 3**4 is : \",end=\"\")\n",
    "print (n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Looping Through Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n",
      "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n"
     ]
    }
   ],
   "source": [
    "l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "  \n",
    "\n",
    "cube = []\n",
    "for i in l:\n",
    "    cube.append(pow(i, 3))\n",
    "  \n",
    "\n",
    "print(cube)\n",
    "\n",
    "a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "cube = []\n",
    "for i in a_list:\n",
    "    cube.append(i*i*i)\n",
    "print(cube)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise #1 <br>\n",
    "<p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n",
      "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n"
     ]
    }
   ],
   "source": [
    "l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "  \n",
    "\n",
    "cube = []\n",
    "for i in l:\n",
    "    cube.append(pow(i, 3))\n",
    "  \n",
    "\n",
    "print(cube)\n",
    "\n",
    "a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "cube = []\n",
    "for i in a_list:\n",
    "    cube.append(i*i*i)\n",
    "print(cube)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise #2 <br>\n",
    "<p>Get first prime numbers up to 100</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 2  3  4  6  8  12  14  18  20  24  30  32  38  42  44  48  54  60  62  68  72  74  80  84  90  98 "
     ]
    }
   ],
   "source": [
    "# HINT::\n",
    "# An else after an if runs if the if didn’t\n",
    "# An else after a for runs if the for didn’t break\n",
    "#GOOGLED ANSWER, DO NOT UNDERSTAND\n",
    "for num in range(1, 101):\n",
    "    count = 0\n",
    "    for i in range(2, (num//2 + 1)):\n",
    "        if num % i == 1:\n",
    "            count = count + 1\n",
    "            break\n",
    "    if (count == 0 and num  != 1):\n",
    "            print(\" %d\" %num, end = ' ')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exercise 3 <br>\n",
    "<p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n",
      "junior discount\n"
     ]
    }
   ],
   "source": [
    "#GOOGLED ANSWER, DO NOT UNDERSTAND\n",
    "\n",
    "x = input()\n",
    "age = float(x)\n",
    "if age >= 60:\n",
    "    print(\"senior discount\")\n",
    "elif 18 <= age < 60:\n",
    "    print(\"no discount\")\n",
    "else:\n",
    "    print (\"junior discount\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-66-5428a402bfc9>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-66-5428a402bfc9>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    git init\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
