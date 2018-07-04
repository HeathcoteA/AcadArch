-- ---------------------------------------------------------------------
-- Le mode autocommit par défaut est désactivé grâce à cette ligne
-- les transactions sécurisent les envois de données par blocs committés
-- ---------------------------------------------------------------------
SET autocommit = 0;
-- ----------------------------------
-- Data for table `academie`.`user`
-- ----------------------------------
START TRANSACTION;
USE `academie`;
INSERT INTO `academie`.`user` VALUES
(1,'Admin','admin@example.com','motdepasse'),
(2,'Stagiaire','stagiaire@example.com','motdepasse'),
(3,'Stagiaire','stagiaire@example.com','motdepasse'),
(4,'Stagiaire','stagiaire@example.com','motdepasse'),
(5,'Stagiaire','stagiaire@example.com','motdepasse'),
(6,'Stagiaire','stagiaire@example.com','motdepasse'),
(7,'Stagiaire','stagiaire@example.com','motdepasse');
COMMIT;

-- ------------------------------------
-- Data for table `academie`.`motscles`
-- ------------------------------------
START TRANSACTION;
USE `academie`;
insert into `academie`.`motscles` values
  (1,'Monographie'),
  (2, 'Architecture classique française'),
  (3,'Antiquité romaine'),
  (4, 'Archéologie'),
  (5,'Economie du bâtiment'),
  (6, 'Théorie de l architecture'),
  (7, 'Enseignement  de l architecture'),
  (8, 'Biographie d\'architecte'),
  (9, 'Architecture du XVIIIe'),
  (10, 'Traité de construction'),
  (11, 'Stéréotomie'),
  (12, 'Coupe des pierres'),
  (13, 'L\'architecture privée'),
  (14, 'Traité de construction'),
  (15, 'Ornements'),
  (16, 'Décoration intérieure'),
  (17, 'Antiquités égyptiennes'),
  (18, 'Législation du bâtiment'),
  (19, 'Expositions'),
  (20,'Architecture arabo-musulmane'),
  (21,'Antiquité grecque'),
  (22,'Architecture de la Renaissance'),
  (23,'Architecture médiévale'),
  (24,'Architecture pré-colombienne'),
  (25,'Architecture d\'extrême-orient'),
  (26,'Architecture du XIXe'),
  (27,'Sculpture'),
  (28,'Art urbain');
  COMMIT;
