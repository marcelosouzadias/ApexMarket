from flask import Flask
from flask import render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    hoje = date.today().strftime("%d/%m/%Y")
    return render_template("index.html", data_atual=hoje)

@app.route("/sobre")
def sobre():
    return "Página Sobre"

if __name__ == "__main__":
    app.run(debug=True)