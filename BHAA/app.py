# selon le cours python dispensé à l'ENC par M. Thibault Clérice
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("Application")
# configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://academie_user:password@localhost/academie'
# variable extension
db = SQLAlchemy(app)

#création d'un modèle de classe pour BD
class Livres(db.Model):
    livre_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    livre_titre = db.Column(db.Text)
    livre_auteur = db.Column(db.Text)
    livre_editeur = db.Column(db.Text)
    livre_annee = db.Column(db.String(4))
    livre_localisation = db.Column(db.Text)

# remplissage de la BD academie.livre


@app.route("/")
def index():
    mots = [" Bienvenue sur la page d'accueil "]
    return render_template("pages/index.html", nom="BHAA", mots=mots)

@app.route("/catalogue")
def catalogue():
    livres = Livres.query.all()
    return render_template("pages/catalogue.html", nom="BHAA", livres=livres)

@app.route("/notice/<int:livre_id>")
def notice(livre_id):
    exemplaire_livre = Livres.query.get(livre_id)
    return render_template("pages/notice.html", nom="BHAA", livres=exemplaire_livre)

@app.route("/connexion")
def connexion():
    mots = [" Connectez-vous "]
    return render_template("pages/connexion.html", nom="BHAA", mots=mots)

@app.route("/erreur")
def erreur():
    mots = [" ERREUR "]
    return render_template("pages/erreur.html", nom="BHAA", mots=mots)

@app.route("/recherche")
def recherche():
    mots = [" Que recherchez-vous ? "]
    return render_template("pages/recherche.html", nom="BHAA", mots=mots)

@app.route("/localisation")
def localisation():
    mots = [" Etagères de la bibliothèque "]
    return render_template("pages/localisation.html", nom="BHAA", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)


#retirer mode debug une fois le développement terminé !
