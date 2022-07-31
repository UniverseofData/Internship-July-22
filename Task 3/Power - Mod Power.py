{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "10068ad4-9fbc-4641-8740-d290e69ae1b4",
   "metadata": {},
   "source": [
    "So far, we have only heard of Python's powers. Now, we will witness them!\n",
    "\n",
    "Powers or exponents in Python can be calculated using the built-in power function. Call the power function  as shown below:\n",
    "\n",
    ">>> pow(a,b) \n",
    "or\n",
    "\n",
    ">>> a**b\n",
    "It's also possible to calculate .\n",
    "\n",
    ">>> pow(a,b,m)  \n",
    "This is very helpful in computations where you have to print the resultant % mod.\n",
    "\n",
    "Note: Here,  and  can be floats or negatives, but, if a third argument is present,  cannot be negative.\n",
    "\n",
    "Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().\n",
    "\n",
    "Task\n",
    "You are given three integers: , , and . Print two lines.\n",
    "On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).\n",
    "\n",
    "Input Format\n",
    "The first line contains , the second line contains , and the third line contains .\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "\n",
    "Sample Input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "54c995bf-5dd5-4f4a-8fb6-bed3465b5c90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n",
      " 4\n",
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "a = int(input())\n",
    "b = int(input())\n",
    "m = int(input())\n",
    "\n",
    "print(pow(a,b))\n",
    "\n",
    "print(pow(a,b,m))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0819a194-d71c-4ac0-a00c-0e87ddd49bc0",
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
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
