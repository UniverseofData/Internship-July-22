{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1e882ba6-3cdb-4222-981d-04ac94e73440",
   "metadata": {},
   "source": [
    "Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.\n",
    "\n",
    "str.isalnum()\n",
    "This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).\n",
    "\n",
    ">>> print 'ab123'.isalnum()\n",
    "True\n",
    ">>> print 'ab123#'.isalnum()\n",
    "False\n",
    "str.isalpha()\n",
    "This method checks if all the characters of a string are alphabetical (a-z and A-Z).\n",
    "\n",
    ">>> print 'abcD'.isalpha()\n",
    "True\n",
    ">>> print 'abcd1'.isalpha()\n",
    "False\n",
    "str.isdigit()\n",
    "This method checks if all the characters of a string are digits (0-9).\n",
    "\n",
    ">>> print '1234'.isdigit()\n",
    "True\n",
    ">>> print '123edsd'.isdigit()\n",
    "False\n",
    "str.islower()\n",
    "This method checks if all the characters of a string are lowercase characters (a-z).\n",
    "\n",
    ">>> print 'abcd123#'.islower()\n",
    "True\n",
    ">>> print 'Abcd123#'.islower()\n",
    "False\n",
    "str.isupper()\n",
    "This method checks if all the characters of a string are uppercase characters (A-Z).\n",
    "\n",
    ">>> print 'ABCD123#'.isupper()\n",
    "True\n",
    ">>> print 'Abcd123#'.isupper()\n",
    "False\n",
    "Task\n",
    "\n",
    "You are given a string .\n",
    "Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.\n",
    "\n",
    "Input Format\n",
    "\n",
    "A single line containing a string .\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "Output Format\n",
    "\n",
    "In the first line, print True if  has any alphanumeric characters. Otherwise, print False.\n",
    "In the second line, print True if  has any alphabetical characters. Otherwise, print False.\n",
    "In the third line, print True if  has any digits. Otherwise, print False.\n",
    "In the fourth line, print True if  has any lowercase characters. Otherwise, print False.\n",
    "In the fifth line, print True if  has any uppercase characters. Otherwise, print False.\n",
    "\n",
    "Sample Input\n",
    "\n",
    "qA2\n",
    "Sample Output\n",
    "\n",
    "True\n",
    "True\n",
    "True\n",
    "True\n",
    "True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "278894d0-334f-4ae0-9110-eb0ccf5ef231",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "    s = input()\n",
    "    print(any(map(str.isalnum, s)))\n",
    "    print(any(map(str.isalpha, s)))\n",
    "    print(any(map(str.isdigit, s)))\n",
    "    print(any(map(str.islower, s)))\n",
    "    print(any(map(str.isupper, s)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05b4bed5-e3c0-4bfc-80be-8bb6ccdf88a0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8317b564-6263-4487-8560-62cbe4af1d81",
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
