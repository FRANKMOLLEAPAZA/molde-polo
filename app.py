
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        try:
            largo = float(request.form['largo'])
            ancho = float(request.form['ancho'])
            manga = float(request.form['manga'])
            cuello = float(request.form['cuello'])
            pecho = float(request.form['pecho'])
            largo_total = float(request.form['largo_total'])
            ancho_hombro = float(request.form['ancho_hombro'])
            ancho_manga = float(request.form['ancho_manga'])
            margen_costura = float(request.form['margen_costura'])

            if largo <= 0 or ancho <= 0 or manga <= 0 or cuello <= 0 or pecho <= 0 or largo_total <= 0 or ancho_hombro <= 0 or ancho_manga <= 0 or margen_costura < 0:
                return "❌ Error: Todas las medidas deben ser mayores que cero y margen de costura no negativo."

            medidas = {
                "Largo": largo,
                "Ancho": ancho,
                "Manga": manga,
                "Cuello": cuello,
                "Pecho": pecho,
                "Largo Total": largo_total,
                "Ancho Hombro": ancho_hombro,
                "Ancho Manga": ancho_manga,
                "Margen Costura": margen_costura
            }
            return render_template('resultado.html', medidas=medidas)

        except ValueError:
            return "❌ Error: Ingrese solo números válidos."

    return render_template('formulario.html')

if __name__ == "__main__":
    app.run(debug=True)
