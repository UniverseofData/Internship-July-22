{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8d1184a2-7e3f-4dc6-97d5-34f0c6bd926c",
   "metadata": {},
   "source": [
    "Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.\n",
    "\n",
    "Input Format\n",
    "\n",
    "The first line contains . The second line contains an array   of  integers each separated by a space."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ddf3ffa2-1fac-4cb5-82bd-9fe2963d3e6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " 2 3 6 6 5\n"
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
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    arr = map(int, input().split())\n",
    "print(sorted(list(set(arr)))[-2])\n",
    "    "
   ]
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
