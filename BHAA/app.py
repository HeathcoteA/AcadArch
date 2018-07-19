from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    mots = [" Bienvenue sur la page d'accueil "]
    return render_template('pages/index.html', titre="Bienvenue", mots=mots)

@app.route('/catalogue')
def catalogue():
    mots = [" Voici le catalogue "]
    return render_template('pages/catalogue.html', titre="Catalogue", mots=mots)

@app.route('/notice')
def notice():
    mots = [" Visualisation de notice exemplaire "]
    return render_template('pages/notice.html', titre="Notice", mots=mots)

@app.route('/connexion')
def connexion():
    mots = [" Connectez-vous "]
    return render_template('pages/connexion.html', titre="Connexion", mots=mots)

@app.route('/erreur')
def erreur():
    mots = [" ERREUR "]
    return render_template('pages/erreur.html', titre="Erreur", mots=mots)

@app.route('/recherche')
def recherche():
    mots = [" Que recherchez-vous ? "]
    return render_template('pages/recherche.html', titre="Recheche", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)


#retirer mode debug une fois le développement terminé !
