{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbe6e6d8-e14d-4948-b3da-0848203bc93c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import flask \n",
    "import re\n",
    "from unittest import result\n",
    "from flask import Flask, render_template,request\n",
    "\n",
    "# Create the Object \n",
    "app = Flask(__name__)\n",
    "\n",
    "# Define the Routes and bind it with a Function\n",
    "@app.route('/',methods=['GET','POST'])\n",
    "def regex101():\n",
    "    if request.method=='POST':\n",
    "        xprsn = request.form['xpn']\n",
    "        tststrng = request.form['tst']\n",
    "        cnt=0\n",
    "        if (len(xprsn) ==0 or len(tststrng) == 0):\n",
    "            cnt=-1\n",
    "            return render_template(\"regex_frontend.html\",result=\"Please provide input\",count=cnt)\n",
    "        else:\n",
    "            lst=[]\n",
    "            for match in re.finditer(r'{}'.format(xprsn),tststrng):\n",
    "                stn=''\n",
    "                cnt+=1\n",
    "                stn=stn+\"Match {} \\\"{}\\\" at start and end indices [{} , {}]\".format(cnt,match.group(),match.start(),match.end())\n",
    "                lst.append(stn)\n",
    "            return render_template(\"regex_frontend.html\",result =\"Matches found\", xpn=xprsn, tst=tststrng, lsts=lst, count=cnt)\n",
    "\n",
    "    return render_template(\"regex_frontend.html\",count=-1)\n",
    "\n",
    "    # Below is another method to find the validation of RegEx gives result as match and no match, total matches, invalid RegEx and  \n",
    "    # indices of every matched string. You can manipulate it the way you want to use it.\n",
    "    '''    \n",
    "        def valid_regex(user_regex):\n",
    "        try:\n",
    "            re.compile(user_regex)\n",
    "            valid = True\n",
    "        except re.error:\n",
    "            valid = False\n",
    "        return valid\n",
    "        if valid_regex(user_input):\n",
    "            regex = re.compile(user_input)\n",
    "            matches = regex.findall(string)\n",
    "            if matches!=[]:\n",
    "                print('Matches found:', matches)\n",
    "                print('Total Matches:',len(matches))\n",
    "            else:\n",
    "                print(\"No matches found\")\n",
    "        else:\n",
    "            print('\\nThe Regular Expression was not valid, so no matches.')\n",
    "        cnt=0\n",
    "        for match in re.finditer(r'{}'.format(user_input),string):\n",
    "            cnt+=1\n",
    "        print(\"Match {} \\\"{}\\\" at start and end indices [{} , {}]\".format(cnt,match.group(),match.start(),match.end()))\n",
    "    '''\n",
    "        \n",
    "\n",
    "# Run the App\n",
    "if __name__=='__main__':\n",
    "    app.run(debug=True)"
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
