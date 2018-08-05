-- MySQL dump 10.13  Distrib 5.7.21, for osx10.13 (x86_64)
--
-- Host: localhost    Database: academie
-- ------------------------------------------------------
-- Server version	5.7.21

DROP SCHEMA IF EXISTS `academie`;

CREATE SCHEMA IF NOT EXISTS `academie` DEFAULT CHARACTER SET utf8 ;
USE `academie` ;

-- -----------------------------------------------------
-- Table `academie`.`livre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `academie`.`livre` ;

CREATE TABLE IF NOT EXISTS `academie`.`livre` (
  `livre_id` INT NOT NULL AUTO_INCREMENT,
  `livre_auteur` TEXT NOT NULL,
  `livre_titre` TEXT NOT NULL,
  `livre_editeur` TEXT NOT NULL,
  `livre_annee` TEXT NOT NULL,
  `livre_localisation` TEXT NOT NULL,
  PRIMARY KEY (`place_id`))
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

-- -----------------------------------------------------
-- Création d'un compte mysql et attribution de droits
-- -----------------------------------------------------

-- SET SQL_MODE = ''; --
GRANT USAGE ON *.* TO academie_user;
DROP USER academie_user;
CREATE USER 'academie_user' IDENTIFIED BY 'password';

GRANT ALL ON `academie`.* TO 'academie_user';
GRANT SELECT ON TABLE `academie`.* TO 'academie_user';
GRANT SELECT, INSERT, TRIGGER ON TABLE `academie`.* TO 'academie_user';
GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE `academie`.* TO 'academie_user';

-- Dump completed on 2018-07-03 14:45:03
