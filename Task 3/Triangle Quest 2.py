{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "305b1c63-016c-4496-9900-91cb6fe2c2f3",
   "metadata": {},
   "source": [
    "ou are given a positive integer .\n",
    "Your task is to print a palindromic triangle of size .\n",
    "\n",
    "For example, a palindromic triangle of size  is:\n",
    "\n",
    "1\n",
    "121\n",
    "12321\n",
    "1234321\n",
    "123454321\n",
    "You can't take more than two lines. The first line (a for-statement) is already written for you.\n",
    "You have to complete the code using exactly one print statement.\n",
    "\n",
    "Note:\n",
    "Using anything related to strings will give a score of .\n",
    "Using more than one for-statement will give a score of .\n",
    "\n",
    "Input Format\n",
    "\n",
    "A single line of input containing the integer .\n",
    "\n",
    "Constraints\n",
    "\n",
    "Output Format\n",
    "\n",
    "Print the palindromic triangle of size  as explained above.\n",
    "\n",
    "Sample Input\n",
    "\n",
    "5\n",
    "Sample Output\n",
    "\n",
    "1\n",
    "121\n",
    "12321\n",
    "1234321\n",
    "123454321"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "af12b0cc-a024-4db1-b9d0-00ebb8df2410",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "121\n",
      "12321\n",
      "1234321\n",
      "123454321\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also\n",
    "    print(((10**i)//9)**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b51e319-d3f1-4d60-a9de-08dc9573468f",
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
