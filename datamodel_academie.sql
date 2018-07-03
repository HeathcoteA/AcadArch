-- MySQL dump 10.13  Distrib 5.7.21, for osx10.13 (x86_64)
--
-- Host: localhost    Database: academie
-- ------------------------------------------------------
-- Server version	5.7.21

DROP SCHEMA IF EXISTS `academie`;

CREATE SCHEMA IF NOT EXISTS `academie` DEFAULT CHARACTER SET utf8 ;
USE `academie` ;

-- -----------------------------------------------------
-- Table `academie`.`bibliotheque`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `academie`.`bibliotheque` ;

CREATE TABLE IF NOT EXISTS `academie`.`bibliotheque` (
  `biblio_id` INT NOT NULL AUTO_INCREMENT,
  `biblio_auteur` TEXT,
  `biblio_titre` TEXT,
  `biblio_editeur` TEXT,
  `biblio_années` TEXT,
  `biblio_localisation` TEXT,
  PRIMARY KEY (`biblio_id`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `academie`.`user`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `academie`.`user` ;

CREATE TABLE IF NOT EXISTS `academie`.`user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_nom` tinytext NOT NULL,
  `user_login` varchar(45) NOT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`))
ENGINE=InnoDB;

-- -----------------------------------------------------
-- Table `academie`.`motscles`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `academie`.`motscles`;

CREATE TABLE IF NOT EXISTS `academie`.`motscles` (
	`motscles_id` INT NOT NULL AUTO_INCREMENT,
    `motscles_valeur` VARCHAR(40),
    PRIMARY KEY (`motscles_id`))
    ENGINE = InnoDB;


-- SET SQL_MODE = ''; --
GRANT USAGE ON *.* TO academie_user;
DROP USER academie_user;
CREATE USER 'academie_user' IDENTIFIED BY 'password';

GRANT ALL ON `academie`.* TO 'academie_user';
GRANT SELECT ON TABLE `academie`.* TO 'academie_user';
GRANT SELECT, INSERT, TRIGGER ON TABLE `academie`.* TO 'academie_user';
GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE `academie`.* TO 'academie_user';

-- éléments copiés-collés de Pythounews à voir ensuite -- 
-- SET SQL_MODE=@OLD_SQL_MODE; --
-- SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS; --
-- SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS; -- 

SET autocommit = 0;
-- -----------------------------------------------------
-- Data for table `academie`.`bibliotheque`
-- -----------------------------------------------------
START TRANSACTION;
USE `academie`;
insert into `academie`.`bibliotheque`values
(1, 'AUGUSTE-ALEX GUILLAUMOT', 'Château de Marly-le-Roy', 'A. MOREL', '1865', 'B.1.1'),
(2, 'A. L. T. VAUDOYER', 'Description du theatre de marcellus a rome', 'DUSILLION', '1812', 'B.2.1'),
(3, 'DE COTTE', 'Devis, conditions, prix et adjudications', NULL, '1728', 'D.2.1'),
(4, 'J. GUADET', 'Elements et theorie de l\'architecture', 'LIBRAIRIE DE LA CONSTRUCTION MODERNE', NULL, 'D.3.1'),
(5, 'JEAN MONVAL', 'Soufflot', 'LIBRAIRIE ALPHONSE LEMERRE', '1918', 'D.2.3'),
(6, 'FRANCOIS DERAND', 'Architecture des voutes', 'SEBASTIEN CRAMOISY', '1643', 'F.2.1'),
(7, 'CESAR DALY', 'Decorations interieures peintes-architecture-Volume1', 'LIBRAIRIE GENERALE DE L\'ARCHITECTURE ET DES TRAVAUX PUBLICS\r\nDUCHER ET CIE', '1877', 'I.2.2'),
(8, 'GASTON MASPERO','L\'archeologie egyptienne','Quantin', '1887',null),
(9, 'GEORGES GROMORT', 'Essai sur la théorie de l\'architecture: cours professé à l\'école nationale supérieure des beaux-arts','CH.MASSIN', '1983', null);
COMMIT;

-- -----------------------------------------------------
-- Data for table `academie`.`user`
-- -----------------------------------------------------
START TRANSACTION;
USE `academie`;
INSERT INTO `academie`.`user` VALUES
(1,'Administrator','admin@example.com','motdepasse'),
(2,'Stagiaire01','stagiaire01@example.com','motdepasse01'),
(3,'Stagiaire02','stagiaire02@example.com','motdepasse02'),
(4,'Stagiaire03','stagiaire03@example.com','motdepasse03'),
(5,'Stagiaire04','stagiaire04@example.com','motdepasse04'),
(6,'Stagiaire05','stagiaire05@example.com','motdepasse05'),
(7,'Stagiaire06','stagiaire06@example.com','motdepasse06');
COMMIT;

-- -----------------------------------------------------
-- Data for table `academie`.`motscles`
-- -----------------------------------------------------
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

-- Dump completed on 2018-06-29 14:45:03
