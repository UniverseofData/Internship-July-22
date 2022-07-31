{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "47c37f9b-fd11-405b-a00b-9ac890ff0bba",
   "metadata": {},
   "source": [
    ".symmetric_difference()\n",
    "The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.\n",
    "Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.\n",
    "The set is immutable to the .symmetric_difference() operation (or ^ operation)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bff7cc3d-92c9-4a2b-9e06-071670448d3d",
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
      "4\n"
     ]
    }
   ],
   "source": [
    "n1 = int(input())\n",
    "set_1 = set(map(int,input().split()))\n",
    "n2 = int(input())\n",
    "set_2 = set(map(int,input().split()))\n",
    "print(len(set_1-set_2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a341c0f-6d62-4140-853d-5a2363921bdd",
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
