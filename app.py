from flask import Flask, render_template
from flask import request 
from flask import jsonify
import os
import vectorspace
import precisionrecall

app = Flask(__name__)
columns = ['Num Document', 'Title', 'Match Sentence', 'Ranking Coefficient']

@app.route("/")
@app.route("/clear")
def home():
    return render_template("index.html",
    qSet = [{'query': 'what similarity laws must be obeyed'}, {'query': 'what are the structural and aeroelastic'}, {'query': 'can a criterion be developed to show'}])

@app.route("/selectQuery", methods=['GET'])
def selectQuery():
    select = request.form.get('queries')
    selectedQry = str(select) #to see what select is
    return selectedQry

@app.route("/selectQuery", methods=['GET','POST'])
def table_display():
  selected = selectQuery()
  vsmRes = vectorspace.start(selected) #calls VSM start function with parameter
  return  render_template('table.html', data = vsmRes, columns = columns)

@app.route("/graph", methods=['GET', 'POST'])
def graphic():
  precisionrecall.start()
  return render_template('graphics.html')

if __name__ == '__main__':
    app.debug = True
