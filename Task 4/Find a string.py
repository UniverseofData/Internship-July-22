{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bffe1b84-bf71-4d4f-8e4f-f44a78a071ae",
   "metadata": {},
   "source": [
    "In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.\n",
    "\n",
    "NOTE: String letters are case-sensitive.\n",
    "\n",
    "Input Format\n",
    "\n",
    "The first line of input contains the original string. The next line contains the substring.\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "Each character in the string is an ascii character.\n",
    "\n",
    "Output Format\n",
    "\n",
    "Output the integer number indicating the total number of occurrences of the substring in the original string.\n",
    "\n",
    "Sample Input\n",
    "\n",
    "ABCDCDC\n",
    "CDC\n",
    "Sample Output\n",
    "\n",
    "2\n",
    "Concept\n",
    "\n",
    "Some string processing examples, such as these, might be useful.\n",
    "There are a couple of new concepts:\n",
    "In Python, the length of a string is found by the function len(s), where  is the string.\n",
    "To traverse through the length of a string, use a for loop:\n",
    "\n",
    "for i in range(0, len(s)):\n",
    "    print (s[i])\n",
    "A range function is used to loop over some length:\n",
    "\n",
    "range (0, 5)\n",
    "Here, the range loops over  to .  is excluded."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "27023c10-8acc-49c0-8ed7-18b41647dd1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " ABCDCDC\n",
      " CDC\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "def count_substring(string, sub_string):\n",
    "    count=0\n",
    "    for i in range(len(string)):\n",
    "        for j in range(len(sub_string)):\n",
    "            if string[i+j]==sub_string[j] and j==(len(sub_string)-1):\n",
    "                count=count+1  \n",
    "            if string[i+j]!=sub_string[j]:\n",
    "                break  \n",
    "        if i==len(string)-len(sub_string):\n",
    "            break            \n",
    "    return count\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    string = input().strip()\n",
    "    sub_string = input().strip()\n",
    "    \n",
    "    count = count_substring(string, sub_string)\n",
    "    print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b23dfbff-6a56-49c7-b5a0-6a0beba3abb1",
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
