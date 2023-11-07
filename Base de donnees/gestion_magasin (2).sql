-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  mar. 07 nov. 2023 à 11:56
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `gestion_magasin`
--

-- --------------------------------------------------------

--
-- Structure de la table `magasin`
--

DROP TABLE IF EXISTS `magasin`;
CREATE TABLE IF NOT EXISTS `magasin` (
  `MagasinID` int(11) NOT NULL AUTO_INCREMENT,
  `NomMagasin` varchar(255) DEFAULT NULL,
  `Adresse` varchar(255) DEFAULT NULL,
  `Telephone` varchar(255) DEFAULT NULL,
  `Email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`MagasinID`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `magasin`
--

INSERT INTO `magasin` (`MagasinID`, `NomMagasin`, `Adresse`, `Telephone`, `Email`) VALUES
(35, 'MAGASIN 11', 'ADRESSE 12', 'TELEPHONE 12', 'SOUMLAJOIE@Gmail.com'),
(51, 'magasion 100', 'ADRESSE3', '0456789887', 'SOUMLAJOIE@Gmail.com'),
(53, 'super marche', 'Abidjan mall', '225 0556479756', 'alibass@mail.com'),
(55, 'Abidjan mall', 'Abidjan', '+2255654567890', 'alibass@mail.com'),
(56, 'DELEGUE', 'ABIDJAN', '225897545', 'soum344@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

DROP TABLE IF EXISTS `produit`;
CREATE TABLE IF NOT EXISTS `produit` (
  `ProduitID` int(11) NOT NULL AUTO_INCREMENT,
  `NomProduit` varchar(255) DEFAULT NULL,
  `Categorie` varchar(255) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `PrixUnitaire` double DEFAULT NULL,
  PRIMARY KEY (`ProduitID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`ProduitID`, `NomProduit`, `Categorie`, `Description`, `PrixUnitaire`) VALUES
(1, 'SAC', 'Vetements', 'SAC A MAIN', 400),
(2, 'BIJOU', 'ACCESOIRES', 'SAC A MAIN', 500),
(3, 'sac de riz', 'Aliments', 'papillon', 25000),
(4, 'pantalon', 'vetement', 'jeans', 2000),
(5, 'Ciments', 'Accesoires', 'Ciment ivoire', 2300),
(6, 'Jeans', 'vetement', 'jeans americain', 5000);

-- --------------------------------------------------------

--
-- Structure de la table `stock`
--

DROP TABLE IF EXISTS `stock`;
CREATE TABLE IF NOT EXISTS `stock` (
  `StockID` int(11) NOT NULL,
  `MagasinID` int(11) DEFAULT NULL,
  `ProduitID` int(11) DEFAULT NULL,
  `QuantiteEnStock` int(11) DEFAULT NULL,
  PRIMARY KEY (`StockID`),
  KEY `MagasinID` (`MagasinID`),
  KEY `ProduitID` (`ProduitID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `utlisateur`
--

DROP TABLE IF EXISTS `utlisateur`;
CREATE TABLE IF NOT EXISTS `utlisateur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifiant` varchar(100) NOT NULL,
  `mot_pass` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `utlisateur`
--

INSERT INTO `utlisateur` (`id`, `identifiant`, `mot_pass`) VALUES
(1, 'soumlajoie', 'soum564797'),
(2, 'emmanuela', 'pbkdf2:sha256:600000$sWjHUGjXMeSCvFLE$063c57fd872517be8a23c35b93d3355ae3e7d6ed30327084d2bfffdaafe5f910'),
(3, 'bakibako', 'pbkdf2:sha256:600000$RMXpVl08d0XhWohn$ab7113dbba6b7de6ca5954e02e28f65c3ed325051df1387d16be0c8fc3d6843f'),
(4, 'sidiksoum', 'pbkdf2:sha256:600000$lvlHDwUm0jDT3Aut$e44344b7fbfdf804f822c0a7617602c760ffd326cd6d2be47f828b7e9f4d80e1');

-- --------------------------------------------------------

--
-- Structure de la table `vente`
--

DROP TABLE IF EXISTS `vente`;
CREATE TABLE IF NOT EXISTS `vente` (
  `VenteID` int(11) NOT NULL AUTO_INCREMENT,
  `DateVente` date DEFAULT NULL,
  `MagasinID` int(11) NOT NULL,
  `ProduitID` int(11) NOT NULL,
  `QuantiteVendue` int(11) DEFAULT NULL,
  `MontantTotal` double DEFAULT NULL,
  PRIMARY KEY (`VenteID`),
  KEY `fk_magasinID` (`MagasinID`),
  KEY `fk_produitID` (`ProduitID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `vente`
--

INSERT INTO `vente` (`VenteID`, `DateVente`, `MagasinID`, `ProduitID`, `QuantiteVendue`, `MontantTotal`) VALUES
(1, '2023-11-08', 51, 5, 10, 2000),
(2, '2023-11-08', 51, 5, 10, 2000),
(3, '2023-11-16', 51, 4, 6, 12000),
(4, '2023-11-16', 51, 4, 6, 12000),
(5, '2023-11-05', 51, 6, 7, 35000),
(6, '2023-11-19', 53, 3, 2, 50000),
(7, '2023-11-04', 51, 4, 15, 30000),
(8, '2023-11-06', 35, 4, 6, 12000),
(9, '2023-11-05', 53, 5, 20, 46000),
(10, '2023-11-07', 55, 3, 22, 550000),
(11, '2023-11-23', 55, 3, 4, 100000),
(12, '2023-12-01', 56, 4, 4, 8000);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `vente`
--
ALTER TABLE `vente`
  ADD CONSTRAINT `fk_magasinID` FOREIGN KEY (`MagasinID`) REFERENCES `magasin` (`MagasinID`),
  ADD CONSTRAINT `fk_produitID` FOREIGN KEY (`ProduitID`) REFERENCES `produit` (`ProduitID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
