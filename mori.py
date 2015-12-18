from flask import Flask, render_template, request, redirect, url_for
from numpy import genfromtxt
import unittest
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def mori():
  if request.method == 'POST':
    sex = request.form['sex']
    age = request.form['age']
    M, F = make_table("tables/2012.csv")
    if sex == 'f':
        t = F[age]
    else:
        t = M[age]
    q = t['q']
    d = t['d']
    e = t['e']
    return redirect(url_for('results', sex=sex, age=age, q=q, d=d, e=e))
    
  return render_template('main.html')

@app.route("/results")
@app.route("/results/<sex>/<age>/<q>/<d>/<e>/")
def results(sex=None, age=None, q=None, d=None, e=None):
  return render_template('results.html', sex=sex, age=age, q=q, d=d, e=e)


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

