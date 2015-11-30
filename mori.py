from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def mori():
  return render_template('main.html')

@app.route("/results")
@app.route("/results/<sex>/<age>/")
def show(sex=None, age=None):
  return render_template('results.html', sex=sex, age=age)

if __name__ == "__main__":
  app.run()
