{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f2ea4f87-ff44-4d23-a2b7-f941c8c85cea",
   "metadata": {},
   "source": [
    "Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.\n",
    "\n",
    "Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.\n",
    "\n",
    "Example\n",
    "\n",
    "The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1f52214c-bb56-48ce-9a92-65cee5674d17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " Harry\n",
      " 37.21\n",
      " Berry\n",
      " 37.21\n",
      " Teena\n",
      " 37.2\n",
      " Akruti\n",
      " 41\n",
      " Harsh\n",
      " 39\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Harry\n",
      "Berry\n",
      "Harry\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    students_grade=[]\n",
    "    for _ in range(int(input())):\n",
    "        name = input()\n",
    "        score = float(input())\n",
    "        students_grade.append([name,score])\n",
    "        sorted_scores=sorted(list(set([x[1]for x in students_grade])))\n",
    "    #fetching 2nd lowest score from unique_sorted_Scores\n",
    "    second_lowest=sorted_scores[1]\n",
    "    low_final_list=[]\n",
    "    for student in students_grade:\n",
    "        #checking 2nd lowest_score to each student(score)\n",
    "        if second_lowest==student[1]:\n",
    "            low_final_list.append(student[0])\n",
    "            for student in sorted(low_final_list):\n",
    "                print(student)\n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "323cfbad-cf2e-47a9-b4a3-f85284175ae4",
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
