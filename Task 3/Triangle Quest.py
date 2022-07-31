{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9d365066-b81d-408e-80a4-2d62ee1af50a",
   "metadata": {},
   "source": [
    "You are given a positive integer . Print a numerical triangle of height  like the one below:\n",
    "\n",
    "1\n",
    "22\n",
    "333\n",
    "4444\n",
    "55555\n",
    "......\n",
    "Can you do it using only arithmetic operations, a single for loop and print statement?\n",
    "\n",
    "Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.\n",
    "\n",
    "Note: Using anything related to strings will give a score of .\n",
    "\n",
    "Input Format\n",
    "A single line containing integer, .\n",
    "\n",
    "Constraints\n",
    "\n",
    "Output Format\n",
    "Print  lines as explained abov"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6f3b5a85-c57a-4252-bc81-413d9b4b4e8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,int(input())): \n",
    "    print(((10**i)//9)*i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca19fe04-69d5-49be-a459-fec827bed019",
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
