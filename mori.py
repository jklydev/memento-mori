from flask import Flask, render_template, request, redirect, url_for, jsonify
from numpy import genfromtxt, rint
app = Flask(__name__)

def make_table(path):
    csv = genfromtxt(path, delimiter=",", skip_header=7, skip_footer=3)
    M = {}
    F = {}
    for row in csv:
        x = row[0]
        M[x] = { 's': 'm', 'x': x, 'q': row[2], 'd': row[4], 'e': row[5] }
        F[x] = { 's': 'f', 'x': x, 'q': row[8], 'd': row[10], 'e': row[11] }
    return M, F

def get_table(sex, age):
    if sex == 'f':
        t = F[age]
    else:
        t = M[age]
    return t

M, F = make_table("tables/2012.csv")

@app.route("/", methods=['GET', 'POST'])
def mori():
  if request.method == 'POST':
    sex = request.form['sex']
    age = request.form['age']
    return redirect(url_for('results', sex=sex, age=age))

  return render_template('main.html')


@app.route("/results")
@app.route("/results/<sex>/<age>")
def results(sex=None, age=None):
    try:
        t = get_table(sex, int(age))
    except:
        return redirect(url_for('mori'))
    age=int(age)
    sex=sex
    expected=t['e']
    life=(age + expected)
    lived = int(100*(age/life))
    mort = t['q']*100
    return render_template('results.html', age=age, sex=sex, lived=lived, mort=mort, life=life, expected=expected)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
  app.run()
