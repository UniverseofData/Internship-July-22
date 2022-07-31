{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7381a1a4-4baa-4bd9-bb41-50b51ff2d808",
   "metadata": {},
   "source": [
    "Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).\n",
    "\n",
    "As we know, the result of  grows really fast with increasing .\n",
    "\n",
    "Let's do some calculations on very large integers.\n",
    "\n",
    "Task\n",
    "Read four numbers, , , , and , and print the result of .\n",
    "\n",
    "Input Format\n",
    "Integers , , , and  are given on four separate lines, respectively.\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "Output Format\n",
    "Print the result of  on one line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5954802d-0f74-4a07-9335-7e3396cf1d78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 9\n",
      " 29\n",
      " 7\n",
      " 27\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4710194409608608369201743232\n"
     ]
    }
   ],
   "source": [
    "A = int(input())\n",
    "B = int(input())\n",
    "C = int(input())\n",
    "D = int(input())\n",
    "\n",
    "print((A**B)+(C**D))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8085f84f-f5d8-4012-a0e4-1ecbad1c239d",
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
