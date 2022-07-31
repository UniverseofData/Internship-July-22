{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "61f3eed0-331a-4364-a683-53463140c872",
   "metadata": {},
   "source": [
    "Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.\n",
    "\n",
    "One fine day, a finite number of tourists come to stay at the hotel.\n",
    "The tourists consist of:\n",
    "→ A Captain.\n",
    "→ An unknown group of families consisting of  members per group where  ≠ .\n",
    "\n",
    "The Captain was given a separate room, and the rest were given one room per group.\n",
    "\n",
    "Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.\n",
    "\n",
    "Mr. Anant needs you to help him find the Captain's room number.\n",
    "The total number of tourists or the total number of groups of families is not known to you.\n",
    "You only know the value of  and the room number list.\n",
    "\n",
    "Input Format\n",
    "\n",
    "The first line consists of an integer, , the size of each group.\n",
    "The second line contains the unordered elements of the room number list.\n",
    "\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "Output Format\n",
    "\n",
    "Output the Captain's room number.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "15e84da5-aa1d-487f-8773-d9e9e692d263",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "N = int(input())\n",
    "\n",
    "storage = map(int, input().split())\n",
    "storage = sorted(storage)\n",
    "\n",
    "for i in range(len(storage)):\n",
    "    if(i != len(storage)-1):\n",
    "        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):\n",
    "            print(storage[i])\n",
    "            break;\n",
    "    else:\n",
    "        print(storage[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cec32c11-df78-4e69-a049-2037f5a042b9",
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
