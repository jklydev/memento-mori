from flask import Flask, render_template, request, redirect, url_for
from numpy import genfromtxt
import unittest
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def mori():
  if request.method == 'POST':
    sex = request.form['sex']
    age = request.form['age']
    return redirect(url_for('results', sex=sex, age=age))
    
  return render_template('main.html')

@app.route("/results")
@app.route("/results/<sex>/<age>/")
def results(sex=None, age=None):
  return render_template('results.html', sex=sex, age=age)


def make_table(path):
    csv = genfromtxt(path, delimiter=",", skip_header=7, skip_footer=3)
    M = {}
    F = {}
    for row in csv:
        x = row[0]
        M[x] = { 'q': row[2], 'd': row[4], 'e': row[5] }
        F[x] = { 'q': row[8], 'd': row[10], 'e': row[11] }
    return M, F

if __name__ == "__main__":
  app.run()

