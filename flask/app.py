from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def first():
    return(render_template('index.html'))

@app.route('/index/')
def sixth():
    return(render_template('index.html'))

@app.route('/index2/')
def second():
    return(render_template("index2.html"))

@app.route('/index3/')
def third():
    return(render_template("index3.html"))

@app.route('/index4/')
def fourth():
    return(render_template("index4.html"))

@app.route('/index5/')
def fifth():
    return(render_template("index5.html"))

if __name__ == '__main__':
    app.run(debug=True)