from flask import Flask, render_template, request, redirect, url_for
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

if __name__ == "__main__":
  app.run()
