from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def person():
    return render_template("test.html")

@app.route('/say/<name>')
def hi_name(name):
    return "Hi " + name

@app.route('/repeat/<x>/<phrase>')
def repeat(x, phrase):
    return int(x)*(phrase + " ")
    

if __name__=="__main__":
    app.run(debug=True)

