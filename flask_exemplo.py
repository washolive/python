"""
Exemplo de uso do microframework Flask.
"""
# from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Seja bem-vindo Flask !"
 
@app.route("/welcome/<string:name>/")
def welcome(name):
    return render_template('template.html', name=name)
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
