{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1d2126e9-1be3-458b-a426-dadff9436b3d",
   "metadata": {},
   "source": [
    "Kevin and Stuart want to play the 'The Minion Game'.\n",
    "\n",
    "Game Rules\n",
    "\n",
    "Both players are given the same string, .\n",
    "Both players have to make substrings using the letters of the string .\n",
    "Stuart has to make words starting with consonants.\n",
    "Kevin has to make words starting with vowels.\n",
    "The game ends when both players have made all possible substrings.\n",
    "\n",
    "Scoring\n",
    "A player gets +1 point for each occurrence of the substring in the string .\n",
    "\n",
    "For Example:\n",
    "String  = BANANA\n",
    "Kevin's vowel beginning word = ANA\n",
    "Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.\n",
    "\n",
    "For better understanding, see the image below:\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5dbe31e7-f1dc-4ffa-a1bc-c031b44fb875",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " BANANA\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stuart 12\n"
     ]
    }
   ],
   "source": [
    "def minion_game(string):\n",
    "    # your code goes here\n",
    "    player1 = 0;\n",
    "    player2 = 0;\n",
    "    str_len = len(string)\n",
    "    for i in range(str_len):\n",
    "        if s[i] in \"AEIOU\":\n",
    "            player1 += (str_len)-i\n",
    "        else :\n",
    "            player2 += (str_len)-i\n",
    "    \n",
    "    if player1 > player2:\n",
    "        print(\"Kevin\", player1)\n",
    "    elif player1 < player2:\n",
    "        print(\"Stuart\",player2)\n",
    "    elif player1 == player2:\n",
    "        print(\"Draw\")\n",
    "    else :\n",
    "        print(\"Draw\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    s = input()\n",
    "    minion_game(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3062266c-a231-4e2b-82f2-f9e4fbef331c",
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
