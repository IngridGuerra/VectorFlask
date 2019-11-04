from flask import Flask, render_template
from flask import request 
from flask import jsonify
import json
import vectorspace
import precisionrecall

app = Flask(__name__)
#resultData = open("output.json", "r")
#data = resultData.read()
columns = ['Num Document', 'Title', 'Match Sentence', 'Ranking Coefficient']
'''columns = [{
    "field": "No. Document", # which is the field's name of data key 
    "title": "No. Document", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "Title",
    "title": "Title",
    "sortable": True,
  },
  {
    "field": "Sentence",
    "title": "Sentence",
    "sortable": False,
  },
  {
    "field": "Ranking coefficient",
    "title": "Ranking coefficient",
    "sortable": True,
  }]'''

@app.route("/")
@app.route("/clear")
def home():
    return render_template("index.html",
    qSet = [{'query': 'what similarity laws must be obeyed'}, {'query': 'what are the structural and aeroelastic'}, {'query': 'can a criterion be developed to show'}])

#@app.route("/getQueries", methods = ['GET'])
#def sendQueries():
#    query_dict = {'1': 'first query', '2': 'second query', '3': 'third query'}
#    return jsonify(queries=query_dict)

#@app.route("/saveForm", methods = ['POST'])
#def save_user():
#    #use request.form when accesing form data
#    # each field of request.form['...'] is the name of the input on the HTML.
#    print('ID Estudiante: '     + request.form['id'])
#    print('Nombre Estudiante: ' + request.form['nombre'])
#    print('Correo Estudiante: ' + request.form['correo'])
#    return 'Estudiante Guardado'

#@app.route("/form")
#def form():
#    return render_template('form.html')

@app.route("/selectQuery", methods=['GET'])
def saveQuery():
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
