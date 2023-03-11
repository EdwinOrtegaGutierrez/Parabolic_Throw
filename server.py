from flask import Flask, render_template as html, request
import json
import ParabolicThrow as pt

# Abrir el archivo
with open('static/json/data.json', 'r') as file:
    # Cargar el contenido del archivo en una variable
    dataG = json.load(file)

app = Flask(__name__, template_folder="templates")

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

@app.route('/', methods=['GET','POST'])
def index():
    v0, theta, g, tmax, rmax = 0,0,0,0,0
    if request.method == 'POST':
        v0 = float(request.form['velocity'])
        theta = float(request.form['angle']) 
        g = float(dataG[request.form.get('gravity')])

        tmax, rmax = pt.function(v0, theta, g)
    return html("index.html", v0=v0, theta=theta, g=g, tmax=format(tmax, ".3f"), rmax=format(rmax, ".3f"))

if __name__ == "__main__":
    #app.secret_key = 'super secret key' #NECESARIO PARA MANDAR MENSAJES PRIVADOS
    app.run(host = '0.0.0.0', port=80, debug=True)