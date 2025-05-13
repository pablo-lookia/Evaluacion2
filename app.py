from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#E1: Promedio y asistencia
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            resultado = {
                'promedio': round(promedio, 2),
                'estado': estado
            }
        except ValueError:
            resultado = {'error': 'Por favor ingresa solo números válidos.'}

    return render_template('ejercicio1.html', resultado=resultado)

#E2: Nombre más largo
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)

        resultado = {
            'nombre_largo': nombre_largo,
            'longitud': longitud
        }

    return render_template('ejercicio2.html', resultado=resultado)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
