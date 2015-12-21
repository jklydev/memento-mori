from flask import Flask, render_template, request, redirect, url_for, jsonify
from numpy import genfromtxt
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

M, F = make_table("tables/2012.csv")

@app.route("/", methods=['GET', 'POST'])
def mori():
  if request.method == 'POST':
    sex = request.form['sex']
    age = int(request.form['age'])
    #move this to results function
    if sex == 'f':
        t = F[age]
    else:
        t = M[age]
    data = t
    return redirect(url_for('results', data=data))

  return render_template('main.html')


@app.route("/results")
@app.route("/results/<data>")
def results(data=None):
    if data is not None:
        print 'hello'
        t = eval(data)
        age = t['x']
        sex = t['s']
        d = t['d']
        q = t['q']
        e = t['e']
        return render_template('results.html', age=age, sex=sex, q=q, d=d, e=e)
    return redirect(url_for('/'))


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
  app.run()

