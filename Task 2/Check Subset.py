{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "76f09cd7-27d9-4ef4-9b00-565089cccd48",
   "metadata": {},
   "source": [
    "You are given two sets,  and .\n",
    "Your job is to find whether set  is a subset of set .\n",
    "\n",
    "If set  is subset of set , print True.\n",
    "If set  is not a subset of set , print False.\n",
    "\n",
    "Input Format\n",
    "\n",
    "The first line will contain the number of test cases, .\n",
    "The first line of each test case contains the number of elements in set .\n",
    "The se`cond line of each test case contains the space separated elements of set .\n",
    "The third line of each test case contains the number of elements in set .\n",
    "The fourth line of each test case contains the space separated elements of set ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "816bf9a5-dfd3-4b1b-968a-bd5a4912e9c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n",
      " 5\n",
      " 1 2 3 5 6\n",
      " 9\n",
      " 9 8 5 6 3 2 1 4 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n",
      " 2\n",
      " 5\n",
      " 3 6 5 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 7\n",
      " 1 2 3 5 6 8 9\n",
      " 3\n",
      " 9 8 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "T = int(input())\n",
    "\n",
    "for _ in range(T):\n",
    "    a = input()\n",
    "    A = set(input().split())\n",
    "    b = int(input())\n",
    "    B = set(input().split())\n",
    "    print(A.issubset(B))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e0ba12f-ee81-4344-8830-9a7e99cf2491",
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
