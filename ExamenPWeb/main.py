from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        # Lógica para calcular descuento
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_sin_descuento = tarros * 9000
        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Lógica para autenticar usuarios
        usuarios_registrados = {'juan': 'admin', 'pepe': 'user'}

        if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena:
            mensaje = f'Bienvenido {("administrador " if usuario == "juan" else "usuario ")}{usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
