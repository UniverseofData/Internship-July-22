{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7147fb4a-f60f-400b-9e87-41cf15fd6472",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request, session\n",
    "from flask_session import Session\n",
    "\n",
    "app = Flask(__name__)\n",
    "app.config[\"SESSION_PERMANENT\"] = False\n",
    "app.config[\"SESSION_TYPE\"] = \"filesystem\"\n",
    "Session(app)\n",
    "\n",
    "notes = []\n",
    "@app.route('/', methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if session.get(\"notes\") is None:\n",
    "        session[\"notes\"] = []\n",
    "    if request.method =='POST':\n",
    "        note = request.form.get(\"note\")\n",
    "        if note != \"\":\n",
    "            session[\"notes\"].append(note)\n",
    "        \n",
    "    return render_template(\"home.html\", notes=session['notes'])\n",
    "\n",
    "if __name__ == '__main__':\n",
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
