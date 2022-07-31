{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9ca2c388-d588-496d-a7eb-ebfae2b6174c",
   "metadata": {},
   "source": [
    "Task\n",
    "\n",
    "Now, let's use our knowledge of sets and help Mickey.\n",
    "\n",
    "Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.\n",
    "\n",
    "Formula used:\n",
    "\n",
    "Function Description\n",
    "\n",
    "Complete the average function in the editor below.\n",
    "\n",
    "average has the following parameters:\n",
    "\n",
    "int arr: an array of integers\n",
    "Returns\n",
    "\n",
    "float: the resulting float value rounded to 3 places after the decimal\n",
    "Input Format\n",
    "\n",
    "The first line contains the integer, , the size of .\n",
    "The second line contains the  space-separated integers, .\n",
    "\n",
    "Constraints\n",
    "\n",
    "\n",
    "Sample Input\n",
    "\n",
    "STDIN                                       Function\n",
    "-----                                       --------\n",
    "10                                          arr[] size N = 10\n",
    "161 182 161 154 176 170 167 171 170 174     arr ="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ac34001-9edb-44ff-b6fd-b8f2d548b001",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 10\n",
      " 161 182 161 154 176 170 167 171 170 174\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "169.375\n"
     ]
    }
   ],
   "source": [
    "def average(array):\n",
    "    sum_array = sum(set(array))\n",
    "    len_array = len(set(array))\n",
    "    output = sum_array/len_array\n",
    "    return output;\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    arr = list(map(int, input().split()))\n",
    "    result = average(arr)\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b50c51e6-d549-4166-970d-032ab0203b8f",
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
