from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def accueil():
    mots = [" Bienvenue sur la page d'accueil de catalogarch "]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)

#retirer mode debug une fois le développement terminé !
