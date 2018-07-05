from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    mots = [" Bienvenue sur la page d'accueil "]
    return render_template('pages/index.html', titre="Bienvenue !", mots=mots)

@app.route('/catalogue')
def catalogue():
    mots = [" Bienvenue sur la page de catalogue "]
    return render_template('pages/catalogue.html', titre="Catalogue", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)

#retirer mode debug une fois le développement terminé !
