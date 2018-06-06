from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    mots = [" Bienvenue sur la page d'accueil de catalogarch "]
    return render_template('index.html', titre="Bienvenue !", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)

#retirer mode debug une fois le développement terminé !
