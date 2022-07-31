{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "84efea1b-acfd-4582-b073-f3769058e9a9",
   "metadata": {},
   "source": [
    "The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4a1665a2-70b1-4e08-a80f-8a2b0a11242c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n",
      " Krishna 67 68 69\n",
      " Arjun 70 98 63\n",
      " Malika 52 56 60\n",
      " Malika\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "56.00\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    student_marks = {}\n",
    "    for _ in range(n):\n",
    "        line = input().split()\n",
    "        name, scores = line[0], line[1:]\n",
    "        scores = map(float, scores)\n",
    "        student_marks[name] = scores\n",
    "    query_name = input()\n",
    "    marks=0\n",
    "    for i in student_marks[query_name]:\n",
    "        marks=marks+i\n",
    "    avg=marks/3\n",
    "    print(\"%.2f\"%avg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de128a5e-c438-4cb9-9a06-e7ccb7d505ec",
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
