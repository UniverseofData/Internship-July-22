{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3dfe7d44-2fe1-46d2-bf8b-9ba420034cbe",
   "metadata": {},
   "source": [
    "You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.\n",
    "\n",
    "For Example:\n",
    "\n",
    "Www.HackerRank.com → wWW.hACKERrANK.COM\n",
    "Pythonist 2 → pYTHONIST 2  \n",
    "Function Description\n",
    "\n",
    "Complete the swap_case function in the editor below.\n",
    "\n",
    "swap_case has the following parameters:\n",
    "\n",
    "string s: the string to modify\n",
    "Returns\n",
    "\n",
    "string: the modified string\n",
    "Input Format\n",
    "\n",
    "A single line containing a string .\n",
    "\n",
    "Constraints"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "05f51dbd-9652-4469-bcab-d1af1034e8eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " HackerRank.com presents \"Pythonist 2\"\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hACKERrANK.COM PRESENTS \"pYTHONIST 2\"\n"
     ]
    }
   ],
   "source": [
    "def swap_case(s):\n",
    "\n",
    "    # sWAP cASE in Python - HackerRank Solution START\n",
    "    Output = '';\n",
    "    for char in s:\n",
    "        if(char.isupper()==True):\n",
    "            Output += (char.lower());\n",
    "        elif(char.islower()==True):\n",
    "            Output += (char.upper());\n",
    "        else:\n",
    "            Output += char;\n",
    "    return Output;\n",
    "if __name__ == '__main__':\n",
    "    s = input()\n",
    "    result = swap_case(s)\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8762bac1-8efb-4e13-a935-cdab4eabd0aa",
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
