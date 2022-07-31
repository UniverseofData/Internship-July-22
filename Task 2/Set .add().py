{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a74b8f1b-a601-4eda-beed-4010693c9c6f",
   "metadata": {},
   "source": [
    "f we want to add a single element to an existing set, we can use the .add() operation.\n",
    "It adds the element to the set and returns 'None'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f26eec2a-a7f3-44b7-8545-1e9815ef8a3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 7\n",
      " UK\n",
      " China\n",
      " USA\n",
      " France\n",
      " New Zealand\n",
      " UK\n",
      " France\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "N = int(input())\n",
    "\n",
    "countries = set()\n",
    "\n",
    "for i in range(N):\n",
    "    countries.add(input())\n",
    "\n",
    "print(len(countries))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0246419-020a-4d72-aeca-569e6632f518",
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
