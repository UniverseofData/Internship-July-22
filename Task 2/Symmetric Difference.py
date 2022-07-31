{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a3e9e468-8a7b-4a6b-bd19-3afaa4cc500e",
   "metadata": {},
   "source": [
    "Objective\n",
    "Today, we're learning about a new data type: sets.\n",
    "\n",
    "Concept\n",
    "\n",
    "If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73d02c4d-556b-44b8-a479-03d0dc47f37a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n",
      " 2 4 5 9\n",
      " 4\n",
      " 2 4 11 12\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "9\n",
      "11\n",
      "12\n"
     ]
    }
   ],
   "source": [
    "N,a=int(input()),map(int,input().split())\n",
    "M,b=int(input()),map(int,input().split())\n",
    "\n",
    "a=set(a)\n",
    "b=set(b)\n",
    "\n",
    "#sorted function is used to sort the resultant set\n",
    "for x in sorted(a.difference(b).union(b.difference(a))):\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e98dcf9d-aa3a-41b5-8da5-fa0acf4fc408",
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
