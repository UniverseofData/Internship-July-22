{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ac9105ba-e79e-44ee-b593-487628ad7951",
   "metadata": {},
   "source": [
    "ou are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:\n",
    "\n",
    "Hello firstname lastname! You just delved into python.\n",
    "\n",
    "Function Description\n",
    "\n",
    "Complete the print_full_name function in the editor below.\n",
    "\n",
    "print_full_name has the following parameters:\n",
    "\n",
    "string first: the first name\n",
    "string last: the last name\n",
    "Prints\n",
    "\n",
    "string: 'Hello  ! You just delved into python' where  and  are replaced with  and .\n",
    "Input Format\n",
    "\n",
    "The first line contains the first name, and the second line contains the last name.\n",
    "\n",
    "Constraints\n",
    "\n",
    "The length of the first and last names are each ≤ .\n",
    "\n",
    "Sample Input 0\n",
    "\n",
    "Ross\n",
    "Taylor\n",
    "Sample Output 0\n",
    "\n",
    "Hello Ross Taylor! You just delved into python.\n",
    "Explanation 0\n",
    "\n",
    "The input read by the program is stored as a string data type. A string is a collection of characters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f81e32db-e8b6-44e4-894f-c13e8bfaa9ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Ross\n",
      " Taylor\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Ross Taylor! You just delved into python.\n"
     ]
    }
   ],
   "source": [
    "def print_full_name(first, last):\n",
    "     print(\"Hello %s %s! You just delved into python.\"%(first,last))\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    first_name = input()\n",
    "    last_name = input()\n",
    "    print_full_name(first_name, last_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc162cc7-1c37-4baa-afd3-0abcc3bd1690",
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
