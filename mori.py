from flask import Flask, render_template, request, redirect, url_for, jsonify
from numpy import genfromtxt
app = Flask(__name__)

def make_table(path):
    csv = genfromtxt(path, delimiter=",", skip_header=7, skip_footer=3)
    M = {}
    F = {}
    for row in csv:
        x = row[0]
        M[x] = { 'q': row[2], 'd': row[4], 'e': row[5] }
        F[x] = { 'q': row[8], 'd': row[10], 'e': row[11] }
    return M, F

M, F = make_table("tables/2012.csv")

@app.route("/", methods=['GET', 'POST'])
def mori():
  if request.method == 'POST':
    sex = request.form['sex']
    age = request.form['age']
    if sex == 'f':
        t = F[age]
    else:
        t = M[age]
    q = t['q']
    d = t['d']
    e = t['e']
    data = jsonify(age=age,sex=sex,q=q,d=d,e=e)
    return redirect(url_for('results', data=data))

  return render_template('main.html')


@app.route("/results")
@app.route("/results/<data>")
def results(data=None):
    return render_template('results.html', data=data)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
  app.run()

