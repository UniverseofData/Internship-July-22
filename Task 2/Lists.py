{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "161757ff-08b4-4351-93d4-8a34bc375924",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 12\n",
      " insert 0 5\n",
      " insert 0 6\n",
      " insert 1 10\n",
      " print\n",
      " remove 6\n",
      " append 9\n",
      " append 1\n",
      " sort\n",
      " print\n",
      " pop\n",
      " reverse\n",
      " print\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6, 10, 5]\n",
      "[1, 5, 9, 10]\n",
      "[9, 5, 1]\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    N = int(input())\n",
    "    command=[]\n",
    "    for i in range(N):\n",
    "        command.append(input().split())\n",
    "\n",
    "    result=[]\n",
    "    for i in range(N):\n",
    "        if command[i][0]=='insert':\n",
    "            result.insert(int(command[i][1]),int(command[i][2]))\n",
    "        elif command[i][0]=='print':\n",
    "            print(result)\n",
    "        elif command[i][0]=='remove':\n",
    "            result.remove(int(command[i][1]))\n",
    "        elif command[i][0]=='append':\n",
    "            result.append(int(command[i][1]))\n",
    "        elif command[i][0]=='pop':\n",
    "            result.pop()\n",
    "        elif command[i][0]=='sort':\n",
    "            result.sort()\n",
    "        elif command[i][0]=='reverse':\n",
    "            result.reverse()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c13a51b-8e83-435e-872f-4c8e9d963447",
   "metadata": {},
   "source": [
    "## "
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
