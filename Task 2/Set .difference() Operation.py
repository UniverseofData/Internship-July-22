{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e4e0bf81-eba9-42ef-89a8-7dfcb1f2f57e",
   "metadata": {},
   "source": [
    "Task\n",
    "Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.\n",
    "\n",
    "You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "95bc59ac-57d7-4f80-bc90-50b136b0fbc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 9\n",
      " 1 2 3 4 5 6 7 8 9\n",
      " 9\n",
      "  10 1 2 3 11 21 55 6 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "# Enter your code here. Read input from STDIN. Print output to STDOUT\n",
    "eng_num = int(input())\n",
    "eng_set = set(map(int,input().split()))\n",
    "fren_num = int(input())\n",
    "fren_set = set(map(int,input().split()))\n",
    "\n",
    "print(len(eng_set.difference(fren_set)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d127eb9f-0dfb-40d5-ba6e-461f7889f407",
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
