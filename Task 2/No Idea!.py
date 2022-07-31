{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7882eb7b-aa37-4a1b-8218-04e9da7881b9",
   "metadata": {},
   "source": [
    "There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.\n",
    "\n",
    "Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "666331cf-fde1-4fc6-93ac-c83a02d38c4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3 2\n",
      " 1 5 3\n",
      " 3 1\n",
      " 5 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "io = input().split()\n",
    "m = int(io[0])\n",
    "n = int(io[1])\n",
    "\n",
    "storage = list()\n",
    "count = 0\n",
    "\n",
    "storage = list(map(int, input().strip().split()))\n",
    "\n",
    "A = set(map(int, input().strip().split()))\n",
    "B = set(map(int, input().strip().split()))\n",
    "\n",
    "for i in storage:\n",
    "    if i in A:\n",
    "        count = count+1\n",
    "    if i in B:\n",
    "        count = count-1\n",
    "\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96bb3548-0231-496d-8688-20ee5993710f",
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
