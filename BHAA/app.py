from flask import Flask, render_template
app = Flask(__name__)

    # exemplaires = []
    # if notice:
exemplaires =[
{
    "auteur":"AUGUSTE-ALEX GUILLAUMOT",
    "titre": "Château de Marly-le-Roy",
    "éditeur": "A. MOREL",
    "année de publication": "1865",
    "localisation": "étagère A"
},
{
    "auteur": "A.L.T. VAUDOYER",
    "titre": "Description du theatre de marcellus a rome",
    "éditeur": "DUSILLION",
    "année de publication": "1812",
    "localisation": "étagère C"
},
{
    "auteur": "DE COTTE",
    "titre": "Devis, conditions, prix et adjudications",
    "éditeur":"inconnu",
    "année de publication": "1728",
    "localisation": "étagère A"
},
{
    "auteur": "J. GUADET",
    "titre": "Elements et theorie de l\'architecture",
    "éditeur": "LIBRAIRIE DE LA CONSTRUCTION MODERNE",
    "année de publication": "inconnu",
    "localisation": "étagèreD"
},
{
    "auteur": "JEAN MONVAL",
    "titre": "Soufflot",
    "éditeur": "LIBRAIRIE ALPHONSE LEMERRE",
    "année de publication": "1918",
    "localisation": "étagère E"
},
{
    "auteur": "FRANCOIS DERAND",
    "titre": "Architecture des voutes",
    "éditeur": "SEBASTIEN CRAMOISY",
    "année de publication": "1643",
    "localisation": "étagère M"
},
{
    "auteur": "CESAR DALY",
    "titre": "Decorations interieures peintes-architecture-Volume1",
    "éditeur": "LIBRAIRIE GENERALE DE L\'ARCHITECTURE ET DES TRAVAUX PUBLICS - DUCHER ET CIE",
    "année de publication": "1877",
    "localisation": "étagère I"
},
{
    "auteur": "GASTON MASPERO",
    "titre": "L\'archeologie egyptienne",
    "éditeur": "Quantin",
    "année de publication": "1887",
    "localisation":"étagère E"
},
{
    "auteur": "GEORGES GROMORT",
    "titre": "Essai sur la théorie de l\'architecture: cours professé à l\'école nationale supérieure des beaux-arts",
    "éditeur": "CH.MASSIN",
    "année de publication": "1983",
    "localisation": "inconnu"
}
]

@app.route("/")
def index():
    mots = [" Bienvenue sur la page d'accueil "]
    return render_template("pages/index.html", titre="Bienvenue", mots=mots)

@app.route("/catalogue")
def catalogue():
    mots = [" Voici le catalogue "]
    return render_template("pages/catalogue.html", titre="Catalogue", mots=mots)

@app.route("/notice")
def notice():
    mots = [" Visualisation de notice exemplaire "]
    return render_template("pages/notice.html", titre="Notice", mots=mots)


@app.route("/notice/<int:notice_id>")
def exemplaire(notice_id):
    return render_template("pages/notice.html", titre="Exemplaire", exemplaire=exemplaires[notice_id])

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
