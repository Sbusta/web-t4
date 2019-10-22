from flask import Flask, request, render_template
import requests

app = Flask(__name__,template_folder='templates')

tipoIndicadores_list=['Estrés hídrico','Nitrógeno foliar','Índice de cosecha','Densidad volumétrica radial']

@app.route('/crearIndicador',methods=['GET'])
def crearIndicador():
    return render_template('crearIndicador.html',tipoIndicador=tipoIndicadores_list)

@app.route('/listarIndicador',methods=['GET'])
def ListarIndicador():
    sensores_list = requests.get('http://localhost:5000/indicadores').json()
    return render_template('listarIndicadores.html',indicador=indicadores_list)

@app.route('/guardarIndicador',methods=['POST'])
def guardarIndicador():
    sensor = dict(request.values)
    sensor['prioridad'] = int(sensor['prioridad'])
    request.post('http://localhost:5000/indicadores',json=sensor)
    return(listarIndicadores())

app.run(port=8080,debug=True)