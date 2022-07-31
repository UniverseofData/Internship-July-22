{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ce8bae7c-4d00-4065-bfe6-2fdec76d07c4",
   "metadata": {},
   "source": [
    "The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.\n",
    "\n",
    "You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "10dc3d91-0118-4cf6-a049-05c6d629330c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 9\n",
      " 1 2 3 4 5 6 7 8 9\n",
      " 9\n",
      " 10  1 2 3 11 21 55 6 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "E = int(input())\n",
    "English = set(input().split())\n",
    "\n",
    "F = int(input())\n",
    "French = set(input().split())\n",
    "\n",
    "print(len(English & French))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c2de059-f9a8-41aa-afa2-28d9b226a77a",
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
