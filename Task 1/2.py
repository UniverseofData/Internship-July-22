{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1e7877f8-43a9-4c17-9bbb-4a2e829b279b",
   "metadata": {},
   "source": [
    "Task\n",
    "Given an integer, , perform the following conditional actions:\n",
    "\n",
    "If  is odd, print Weird\n",
    "If  is even and in the inclusive range of  to , print Not Weird\n",
    "If  is even and in the inclusive range of  to , print Weird\n",
    "If  is even and greater than , print Not Weird\n",
    "Input Format\n",
    "\n",
    "A single line containing a positive integer, .\n",
    "\n",
    "Constraints\n",
    "\n",
    "Output Format\n",
    "\n",
    "Print Weird if the number is weird. Otherwise, print Not Weird."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4dff890f-c9d1-498c-ad97-388534fdb0a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Weird\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "if n % 2:\n",
    "    print(\"Weird\")\n",
    "elif 2 <= n <= 5:\n",
    "    print(\"Not Weird\")\n",
    "elif 6 <= n <= 20:\n",
    "    print(\"Weird\")\n",
    "else:\n",
    "    print(\"Not Weird\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8381c5e4-df62-44dc-8ebe-f308cd91fa92",
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
