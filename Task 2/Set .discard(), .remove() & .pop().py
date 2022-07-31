{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3069065e-69fc-4efe-99ab-d4cc7a0c4cab",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "You have a non-empty set , and you have to execute  commands given in  lines.\n",
    "\n",
    "The commands will be pop, remove and discard."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b2fe2ac-ddaa-4e06-9f87-2936d4919440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 9\n",
      " 1 2 3 4 5 6 7 8 9\n",
      " 10\n",
      " pop\n",
      " remove 9\n",
      " discard 9\n",
      " discard 8\n",
      " remove 7\n",
      " pop\n",
      " discard 6\n",
      " remove 5\n",
      " pop\n",
      " discard 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "s = set(map(int, input().split()))\n",
    "num = int(input())\n",
    "for i in range(num):\n",
    "    ip = input().split()\n",
    "    if ip[0]==\"remove\":\n",
    "        s.remove(int(ip[1]))\n",
    "    elif ip[0]==\"discard\":\n",
    "        s.discard(int(ip[1]))\n",
    "    else :\n",
    "        s.pop()\n",
    "print(sum(list(s)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f57bc21e-2961-43b6-bb8f-58eaf99b8c14",
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
