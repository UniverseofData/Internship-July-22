{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a6aa9039-ce78-48b1-b7cf-d872e65c53ee",
   "metadata": {},
   "source": [
    "One of the built-in functions of Python is divmod, which takes two arguments  and  and returns a tuple containing the quotient of  first and then the remainder .\n",
    "\n",
    "For example:\n",
    "\n",
    ">>> print divmod(177,10)\n",
    "(17, 7)\n",
    "Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.\n",
    "\n",
    "Task\n",
    "Read in two integers,  and , and print three lines.\n",
    "The first line is the integer division  (While using Python2 remember to import division from __future__).\n",
    "The second line is the result of the modulo operator: .\n",
    "The third line prints the divmod of  and .\n",
    "\n",
    "Input Format\n",
    "The first line contains the first integer, , and the second line contains the second integer, .\n",
    "\n",
    "Output Format\n",
    "Print the result as described above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b5464d9-4dc3-4c74-a67e-46e63c130b64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 177\n",
      " 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17\n",
      "7\n",
      "(17, 7)\n"
     ]
    }
   ],
   "source": [
    "a = int(input());\n",
    "b = int(input());\n",
    "print(a//b);\n",
    "print(a%b);\n",
    "print(divmod(a,b));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84e76d7d-8e65-4cb0-b7a7-e86c794a1347",
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
