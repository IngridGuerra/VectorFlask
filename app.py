from flask import Flask, render_template
from flask import request 
from flask import jsonify
import vectorspace

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
    data = [{'query': 'what similarity laws must be obeyed'}, {'query': 'what are the structural and aeroelastic'}, {'query': 'can a criterion be developed to show'}])

@app.route("/getQueries", methods = ['GET'])
def sendQueries():
    query_dict = {'1': 'first query', '2': 'second query', '3': 'third query'}
    return jsonify(queries=query_dict)

@app.route("/saveForm", methods = ['POST'])
def save_user():
    #use request.form when accesing form data
    # each field of request.form['...'] is the name of the input on the HTML.
    print('ID Estudiante: '     + request.form['id'])
    print('Nombre Estudiante: ' + request.form['nombre'])
    print('Correo Estudiante: ' + request.form['correo'])
    return 'Estudiante Guardado'

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/selectQuery", methods=['GET','POST'])
def saveQuery():
    select = request.form.get('queries')
    selectedQry = str(select)
    return vectorspace.start(selectedQry) #to see what select is
