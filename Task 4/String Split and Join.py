{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "db84c184-c0cd-4444-b904-28e15cfc0147",
   "metadata": {},
   "source": [
    "In Python, a string can be split on a delimiter.\n",
    "\n",
    "Example:\n",
    "\n",
    ">>> a = \"this is a string\"\n",
    ">>> a = a.split(\" \") # a is converted to a list of strings. \n",
    ">>> print a\n",
    "['this', 'is', 'a', 'string']\n",
    "Joining a string is simple:\n",
    "\n",
    ">>> a = \"-\".join(a)\n",
    ">>> print a\n",
    "this-is-a-string \n",
    "Task\n",
    "You are given a string. Split the string on a \" \" (space) delimiter and join using a - hyphen.\n",
    "\n",
    "Function Description\n",
    "\n",
    "Complete the split_and_join function in the editor below.\n",
    "\n",
    "split_and_join has the following parameters:\n",
    "\n",
    "string line: a string of space-separated words\n",
    "Returns\n",
    "\n",
    "string: the resulting string\n",
    "Input Format\n",
    "The one line contains a string consisting of space separated words."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d519856f-6c7e-4568-83a2-a56bf6a26b38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " this is a string\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this-is-a-string\n"
     ]
    }
   ],
   "source": [
    "def split_and_join(line):\n",
    "    a = line.split(\" \")\n",
    "    a = \"-\".join(a)\n",
    "    return a\n",
    "if __name__ == '__main__':\n",
    "    line = input()\n",
    "    result = split_and_join(line)\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "457630a2-c2f5-4cdd-9fe3-430a6470d991",
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
