{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bb0f9182-f02e-4f9d-88b7-9c9d64c959cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1990\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_leap(year):\n",
    "    leap = False\n",
    "    \n",
    "    if year%4==0 and year%100 !=0:\n",
    "        leap =True\n",
    "    elif year%400==0:\n",
    "        leap =True\n",
    "    \n",
    "    return leap\n",
    "year = int(input())\n",
    "print(is_leap(year))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12c7009f-a56d-478c-88c6-a392c6455a4d",
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
