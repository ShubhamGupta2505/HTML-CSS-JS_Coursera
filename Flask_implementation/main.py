from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    title = "Shubham Gupta Blog"
    return render_template("index.html",title=title)

@app.route('/about')
def about():
    title = "About Shubham Gupta"
    names=["john","Shubham","alok","quata","ajlds"]
    return render_template("about.html",names= names, title = title)