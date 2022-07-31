{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "da3852fd-4a86-441f-bffa-fca4d0f592b1",
   "metadata": {},
   "source": [
    "The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.\n",
    "\n",
    "You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8d5f3ebb-1122-48eb-b121-21ae4bef041d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 9\n",
      " 1 2 3 4 5 6 7 8 9\n",
      " 9\n",
      " 10 1 2 3 11 21 55 6 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "english = set(input().split())\n",
    "b = int(input())\n",
    "french = set(input().split())\n",
    "p = len(english.union(french))\n",
    "print (p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6148375a-a908-4f15-9509-4e7d1dcb934f",
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
