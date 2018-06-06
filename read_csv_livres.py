import pandas
#librairie exterieure pour utiliser les classes pour la BD
from sqlalchemy.ext.declarative import declarative_base
#utiliser les fonctions associées à la librairie
from sqlalchemy import Column, Integer, String, Text, create_engine, MetaData
from sqlalchemy.orm import sessionmaker

Base=declarative_base()
metadata=MetaData()

#creation de la classe
class academie(Base):
    __tablename__='bibliotheque'
    id= Column(Integer, primary_key=True)
    author= Column(String(200), nullable=False)
    title=Column(String(400), nullable=False)
    publisher=Column(String(200), nullable=False)
    date=Column(Text, nullable=False)
    location=Column(String(200), nullable=False)

    #creation de la base et connexion au server: remplacer user et pwd !
engine=create_engine('mysql://user:pwd@localhost/academie')

#creation de la table
Base.metadata.create_all(engine)

#creation d'une session pour la base de données
session=sessionmaker()
session.configure(bind=engine)
s=session()

#importation des données avec librairie Pandas
file = pandas.read_csv('livres.csv',';')
file.to_sql(con=engine, name="bibliotheque", if_exists='replace')
