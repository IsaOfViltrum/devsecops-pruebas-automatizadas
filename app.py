from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicacion Flask de pruebas DevSecOps"

@app.route("/hello")
def hello():
    name = request.args.get("name", "Mundo")
    return f"<h1>Hola {name}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)