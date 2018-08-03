from flask import Flask, render_template
app = Flask(__name__)

# selon le cours python dispensé à l'ENC par M. Thibault Clérice

livres =[
    {
        "id":"1",
        "auteur":"AUGUSTE-ALEX GUILLAUMOT",
        "titre": "Château de Marly-le-Roy",
        "éditeur": "A. MOREL",
        "publication": "1865",
        "localisation": "étagère A"
    },
    {
        "id":"2",
        "auteur": "A.L.T. VAUDOYER",
        "titre": "Description du theatre de marcellus a rome",
        "éditeur": "DUSILLION",
        "publication": "1812",
        "localisation": "étagère C"
    },
    {
        "id":"3",
        "auteur": "DE COTTE",
        "titre": "Devis, conditions, prix et adjudications",
        "éditeur":"inconnu",
        "publication": "1728",
        "localisation": "étagère A"
    },
    {
        "id":"4",
        "auteur": "J. GUADET",
        "titre": "Elements et theorie de l\'architecture",
        "éditeur": "LIBRAIRIE DE LA CONSTRUCTION MODERNE",
        "publication": "inconnu",
        "localisation": "étagèreD"
    },
    {
        "id":"5",
        "auteur": "JEAN MONVAL",
        "titre": "Soufflot",
        "éditeur": "LIBRAIRIE ALPHONSE LEMERRE",
        "publication": "1918",
        "localisation": "étagère E"
    },
    {
        "id":"6",
        "auteur": "FRANCOIS DERAND",
        "titre": "Architecture des voutes",
        "éditeur": "SEBASTIEN CRAMOISY",
        "publication": "1643",
        "localisation": "étagère M"
    },
    {
        "id":"7",
        "auteur": "CESAR DALY",
        "titre": "Decorations interieures peintes-architecture-Volume1",
        "éditeur": "LIBRAIRIE GENERALE DE L\'ARCHITECTURE ET DES TRAVAUX PUBLICS - DUCHER ET CIE",
        "publication": "1877",
        "localisation": "étagère I"
    },
    {
        "id":"8",
        "auteur": "GASTON MASPERO",
        "titre": "L\'archeologie egyptienne",
        "éditeur": "QUANTIN",
        "publication": "1887",
        "localisation":"étagère E"
    },
    {
        "id":"9",
        "auteur": "GEORGES GROMORT",
        "titre": "Essai sur la théorie de l\'architecture: cours professé à l\'école nationale supérieure des beaux-arts",
        "éditeur": "CH.MASSIN",
        "publication": "1983",
        "localisation": "inconnu"
    }
    ]

@app.route("/")
def index():
    mots = [" Bienvenue sur la page d'accueil "]
    return render_template("pages/index.html", titre="Bienvenue", mots=mots)

@app.route("/catalogue")
def catalogue():
    return render_template("pages/catalogue.html", titre="Catalogue", livres=livres)

@app.route("/notice")
def notice():
    return render_template("pages/notice.html", titre="Notice", livres=livres)

# afficher une notice avec URL propre "notice/1"
# @app.route("/notice/<int:notice_id>")
# def notice(notice_id):
#     return render_template("pages/notice.html", titre="Notice", livres=livres[notice_id])

@app.route("/connexion")
def connexion():
    mots = [" Connectez-vous "]
    return render_template("pages/connexion.html", titre="Connexion", mots=mots)

@app.route("/erreur")
def erreur():
    mots = [" ERREUR "]
    return render_template("pages/erreur.html", titre="Erreur", mots=mots)

@app.route("/recherche")
def recherche():
    mots = [" Que recherchez-vous ? "]
    return render_template("pages/recherche.html", titre="Recheche", mots=mots)

@app.route("/localisation")
def localisation():
    mots = [" Etagères de la bibliothèque "]
    return render_template("pages/localisation.html", titre="Localisation", mots=mots)

if __name__ == '__main__':
    app.run(debug=True)


#retirer mode debug une fois le développement terminé !
