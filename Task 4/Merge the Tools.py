{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0cbf0aba-9e8c-4890-920c-476d4b7e8495",
   "metadata": {},
   "source": [
    "Consider the following:\n",
    "\n",
    "A string, , of length  where .\n",
    "An integer, , where  is a factor of .\n",
    "We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:\n",
    "\n",
    "The characters in  are a subsequence of the characters in .\n",
    "Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .\n",
    "Given  and , print  lines where each line  denotes string .\n",
    "\n",
    "Example\n",
    "\n",
    "\n",
    "There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so . The third substring has  different characters, so . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.\n",
    "\n",
    "Function Description\n",
    "\n",
    "Complete the merge_the_tools function in the editor below.\n",
    "\n",
    "merge_the_tools has the following parameters:\n",
    "\n",
    "string s: the string to analyze\n",
    "int k: the size of substrings to analyze\n",
    "Prints\n",
    "\n",
    "Print each subsequence on a new line. There will be  of them. No return value is expected.\n",
    "\n",
    "Input Format\n",
    "\n",
    "The first line contains a single string, .\n",
    "The second line contains an integer, , the length of each substring.\n",
    "\n",
    "Constraints\n",
    "\n",
    ", where  is the length of \n",
    "It is guaranteed that  is a multiple of .\n",
    "Sample Input\n",
    "\n",
    "STDIN       Function\n",
    "-----       --------\n",
    "AABCAAADA   s = 'AABCAAADA'\n",
    "3           k = 3\n",
    "Sample Output\n",
    "\n",
    "AB\n",
    "CA\n",
    "AD\n",
    "Explanation\n",
    "\n",
    "Split  into  equal parts of length . Convert each  to  by removing any subsequent occurrences of non-distinct characters in :\n",
    "\n",
    "Print each  on a new line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b4f8432-782a-44a7-888e-c4670f2d3a55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " AABCAAADA\n",
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AB\n",
      "CA\n",
      "AD\n"
     ]
    }
   ],
   "source": [
    "def merge_the_tools(string, k):\n",
    "    split_string=(string[i:i+k] for i in range(0,len(string),k))\n",
    "    for i in split_string:\n",
    "        u=[]\n",
    "        u.append(i[0])\n",
    "        for j in range(1,len(i)):\n",
    "            if i[j] in u:\n",
    "                continue\n",
    "            else:\n",
    "                u.append(i[j])\n",
    "\n",
    "        print(''.join(str(e) for e in u))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    string, k = input(), int(input())\n",
    "    merge_the_tools(string, k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "150d15dc-abd5-422b-ae34-2acec466f89c",
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
