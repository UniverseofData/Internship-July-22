{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "748be25e-7d98-4851-b151-190c8b15e158",
   "metadata": {},
   "source": [
    "You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.\n",
    "\n",
    "\n",
    "Given a full name, your task is to capitalize the name appropriately.\n",
    "\n",
    "Input Format\n",
    "\n",
    "A single line of input containing the full name, .\n",
    "\n",
    "Constraints\n",
    "\n",
    "The string consists of alphanumeric characters and spaces.\n",
    "Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.\n",
    "\n",
    "Output Format\n",
    "\n",
    "Print the capitalized string, ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4937f59f-09b2-4d56-9018-d920bdf0feb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import os\n",
    "import random\n",
    "import re\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0547f83-2c09-4687-945b-b07819b0accf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Complete the solve function below.\n",
    "def solve(s):\n",
    "    for x in s[:].split():\n",
    "        s = s.replace(x, x.capitalize())\n",
    "    return s\n",
    "if __name__ == '__main__':\n",
    "    fptr = open(os.environ['Output_Path'], 'w')\n",
    "\n",
    "    s = input()\n",
    "\n",
    "    result = solve(s)\n",
    "\n",
    "    fptr.write(result + '\\n')\n",
    "\n",
    "    fptr.close()"
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
