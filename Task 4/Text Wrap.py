{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dc34eec2-98c4-4d27-aab9-8d26aecccd2e",
   "metadata": {},
   "source": [
    "You are given a string  and width .\n",
    "Your task is to wrap the string into a paragraph of width .\n",
    "\n",
    "Function Description\n",
    "\n",
    "Complete the wrap function in the editor below.\n",
    "\n",
    "wrap has the following parameters:\n",
    "\n",
    "string string: a long string\n",
    "int max_width: the width to wrap to\n",
    "Returns\n",
    "\n",
    "string: a single string with newline characters ('\\n') where the breaks should be\n",
    "Input Format\n",
    "\n",
    "The first line contains a string, .\n",
    "The second line contains the width, .\n",
    "\n",
    "Constraints\n",
    "\n",
    "Sample Input 0\n",
    "\n",
    "ABCDEFGHIJKLIMNOQRSTUVWXYZ\n",
    "4\n",
    "Sample Output 0\n",
    "\n",
    "ABCD\n",
    "EFGH\n",
    "IJKL\n",
    "IMNO\n",
    "QRST\n",
    "UVWX\n",
    "YZ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "416b2015-41c6-4013-babf-32fe66caf319",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " ABCDEFGHIJKLIMNOQRSTUVWXYZ\n",
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ABCD\n",
      "EFGH\n",
      "IJKL\n",
      "IMNO\n",
      "QRST\n",
      "UVWX\n",
      "YZ\n"
     ]
    }
   ],
   "source": [
    "import textwrap\n",
    "\n",
    "def wrap(string, max_width):\n",
    "    return textwrap.TextWrapper(width=max_width).fill(text=string)\n",
    " \n",
    "if __name__ == '__main__':\n",
    "    string, max_width = input(), int(input())\n",
    "    result = wrap(string, max_width)\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8294c7c6-a305-4924-afce-1d7ab00ac40d",
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
