{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0e372245-6562-49a6-a856-acd23a0f85c6",
   "metadata": {},
   "source": [
    "Given an integer, , print the following values for each integer  from  to :\n",
    "\n",
    "Decimal\n",
    "Octal\n",
    "Hexadecimal (capitalized)\n",
    "Binary\n",
    "Function Description\n",
    "\n",
    "Complete the print_formatted function in the editor below.\n",
    "\n",
    "print_formatted has the following parameters:\n",
    "\n",
    "int number: the maximum value to print\n",
    "Prints\n",
    "\n",
    "The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.\n",
    "\n",
    "Input Format\n",
    "\n",
    "A single integer denoting .\n",
    "\n",
    "Constraints\n",
    "\n",
    "Sample Input\n",
    "\n",
    "17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fefd10ab-32ab-44d5-8e97-217c62d944ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1  1  1  1 \n",
      " 2  2  2 10 \n"
     ]
    }
   ],
   "source": [
    "def print_formatted(number):\n",
    "    # your code goes here\n",
    "    # String Formatting in Python - HackerRank Solution START\n",
    "    l1 = len(bin(number)[2:])\n",
    "   \n",
    "    for i in range(1,number+1):\n",
    "        print(str(i).rjust(l1,' '),end=\" \")\n",
    "        print(oct(i)[2:].rjust(l1,' '),end=\" \")\n",
    "        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=\" \")\n",
    "        print(bin(i)[2:].rjust(l1,' '),end=\" \")\n",
    "        print(\"\")\n",
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    print_formatted(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b23727e-f3a6-45f0-9d64-56f1e036214f",
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
