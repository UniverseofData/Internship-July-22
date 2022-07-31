{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "347c7530-ade3-4b60-97b4-4de53ed47744",
   "metadata": {},
   "source": [
    "Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a1120faa-ad1e-449f-90f3-96c8ee1bb1d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n",
      " 1\n",
      " 2\n",
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    x = int(input())\n",
    "    y = int(input())\n",
    "    z = int(input())\n",
    "    n = int(input())\n",
    "ans = [[i, j, k] for i in range(x + 1)for j in range(y + 1) for k in range(z + 1) if i + j + k != n]\n",
    "print(ans)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f814bdf5-8141-4eda-affe-03e6b1eee2cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n",
      " 1\n",
      " 2\n",
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    x = int(input())\n",
    "    y = int(input())\n",
    "    z = int(input())\n",
    "    n = int(input())\n",
    "    \n",
    "    lists = []\n",
    "    \n",
    "    for i in range(x+1):\n",
    "        for j in range(y+1):\n",
    "            for k in range(z+1):\n",
    "                if (i+j+k)!=n:\n",
    "                    lists.append([i,j,k])\n",
    "                \n",
    "                    \n",
    "    print(lists)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f78368c3-4cd1-4e88-8b3f-a04c5572191a",
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
