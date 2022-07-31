{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6fad0938-6126-49fa-b47c-b30997643c55",
   "metadata": {},
   "source": [
    "Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:\n",
    "\n",
    "Mat size must be X. ( is an odd natural number, and  is  times .)\n",
    "The design should have 'WELCOME' written in the center.\n",
    "The design pattern should only use |, . and - characters.\n",
    "Sample Designs\n",
    "\n",
    "    Size: 7 x 21 \n",
    "    ---------.|.---------\n",
    "    ------.|..|..|.------\n",
    "    ---.|..|..|..|..|.---\n",
    "    -------WELCOME-------\n",
    "    ---.|..|..|..|..|.---\n",
    "    ------.|..|..|.------\n",
    "    ---------.|.---------\n",
    "    \n",
    "    Size: 11 x 33\n",
    "    ---------------.|.---------------\n",
    "    ------------.|..|..|.------------\n",
    "    ---------.|..|..|..|..|.---------\n",
    "    ------.|..|..|..|..|..|..|.------\n",
    "    ---.|..|..|..|..|..|..|..|..|.---\n",
    "    -------------WELCOME-------------\n",
    "    ---.|..|..|..|..|..|..|..|..|.---\n",
    "    ------.|..|..|..|..|..|..|.------\n",
    "    ---------.|..|..|..|..|.---------\n",
    "    ------------.|..|..|.------------\n",
    "    ---------------.|.---------------\n",
    "Input Format\n",
    "\n",
    "A single line containing the space separated values of  and .\n",
    "\n",
    "Constraints\n",
    "\n",
    "Output Format\n",
    "\n",
    "Output the design pattern.\n",
    "\n",
    "Sample Input\n",
    "\n",
    "9 27"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "15340045-f277-4c6c-8000-0fa8cbc60267",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 9 27\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------.|.------------\n",
      "---------.|..|..|.---------\n",
      "------.|..|..|..|..|.------\n",
      "---.|..|..|..|..|..|..|.---\n",
      "----------WELCOME----------\n",
      "---.|..|..|..|..|..|..|.---\n",
      "------.|..|..|..|..|.------\n",
      "---------.|..|..|.---------\n",
      "------------.|.------------\n"
     ]
    }
   ],
   "source": [
    "n,m=input().split()\n",
    "c='|'\n",
    "v='.'\n",
    "\n",
    "n=int(n)\n",
    "m=int(m)\n",
    "j=n//2-1\n",
    "for i in range(n):\n",
    "    if i==n//2:\n",
    "        print('WELCOME'.center(m,'-'))\n",
    "    else:\n",
    "        if i<n/2:    \n",
    "            print(((v+c+v)*(2*i+1)).center(m,'-'))\n",
    "        else:\n",
    "            print(((v+c+v)*(2*j+1)).center(m,'-'))\n",
    "            j=j-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e33f3c7e-e6f8-4191-a62e-266dd7f0d1e7",
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
