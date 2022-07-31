{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f1fd107c-d92a-4c40-adf0-a4eb78e8942a",
   "metadata": {},
   "source": [
    "You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)\n",
    "\n",
    "Different sizes of alphabet rangoli are shown below:\n",
    "\n",
    "#size 3\n",
    "\n",
    "----c----\n",
    "--c-b-c--\n",
    "c-b-a-b-c\n",
    "--c-b-c--\n",
    "----c----\n",
    "\n",
    "#size 5\n",
    "\n",
    "--------e--------\n",
    "------e-d-e------\n",
    "----e-d-c-d-e----\n",
    "--e-d-c-b-c-d-e--\n",
    "e-d-c-b-a-b-c-d-e\n",
    "--e-d-c-b-c-d-e--\n",
    "----e-d-c-d-e----\n",
    "------e-d-e------\n",
    "--------e--------\n",
    "\n",
    "#size 10\n",
    "\n",
    "------------------j------------------\n",
    "----------------j-i-j----------------\n",
    "--------------j-i-h-i-j--------------\n",
    "------------j-i-h-g-h-i-j------------\n",
    "----------j-i-h-g-f-g-h-i-j----------\n",
    "--------j-i-h-g-f-e-f-g-h-i-j--------\n",
    "------j-i-h-g-f-e-d-e-f-g-h-i-j------\n",
    "----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----\n",
    "--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--\n",
    "j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j\n",
    "--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--\n",
    "----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----\n",
    "------j-i-h-g-f-e-d-e-f-g-h-i-j------\n",
    "--------j-i-h-g-f-e-f-g-h-i-j--------\n",
    "----------j-i-h-g-f-g-h-i-j----------\n",
    "------------j-i-h-g-h-i-j------------\n",
    "--------------j-i-h-i-j--------------\n",
    "----------------j-i-j----------------\n",
    "------------------j------------------\n",
    "The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).\n",
    "\n",
    "Function Description\n",
    "\n",
    "Complete the rangoli function in the editor below.\n",
    "\n",
    "rangoli has the following parameters:\n",
    "\n",
    "int size: the size of the rangoli\n",
    "Returns\n",
    "\n",
    "string: a single string made up of each of the lines of the rangoli separated by a newline character (\\n)\n",
    "Input Format\n",
    "\n",
    "Only one line of input containing , the size of the rangoli.\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "Sample Input\n",
    "\n",
    "5\n",
    "Sample Output\n",
    "\n",
    "--------e--------\n",
    "------e-d-e------\n",
    "----e-d-c-d-e----\n",
    "--e-d-c-b-c-d-e--\n",
    "e-d-c-b-a-b-c-d-e\n",
    "--e-d-c-b-c-d-e--\n",
    "----e-d-c-d-e----\n",
    "------e-d-e------\n",
    "--------e--"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "295a5e3d-e90f-47e5-b670-78ca8fc6574e",
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
      "--------e--------\n",
      "------e-d-e------\n",
      "----e-d-c-d-e----\n",
      "--e-d-c-b-c-d-e--\n",
      "e-d-c-b-a-b-c-d-e\n",
      "--e-d-c-b-c-d-e--\n",
      "----e-d-c-d-e----\n",
      "------e-d-e------\n",
      "--------e--------\n"
     ]
    }
   ],
   "source": [
    "def print_rangoli(size):\n",
    "    # your code goes here\n",
    "    # Alphabet Rangoli in Python \n",
    "    width  = size*4-3\n",
    "    string = ''\n",
    "\n",
    "    for i in range(1,size+1):\n",
    "        for j in range(0,i):\n",
    "            string += chr(96+size-j)\n",
    "            if len(string) < width :\n",
    "                string += '-'\n",
    "        for k in range(i-1,0,-1):    \n",
    "            string += chr(97+size-k)\n",
    "            if len(string) < width :\n",
    "                string += '-'\n",
    "        print(string.center(width,'-'))\n",
    "        string = ''\n",
    "\n",
    "    for i in range(size-1,0,-1):\n",
    "        string = ''\n",
    "        for j in range(0,i):\n",
    "            string += chr(96+size-j)\n",
    "            if len(string) < width :\n",
    "                string += '-'\n",
    "        for k in range(i-1,0,-1):\n",
    "            string += chr(97+size-k)\n",
    "            if len(string) < width :\n",
    "                string += '-'\n",
    "        print(string.center(width,'-'))\n",
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    print_rangoli(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11a30aaf-6719-479a-9fca-00bf5bd1aeb8",
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
