/*!40101 SET NAMES utf8mb4 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`library` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `library`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `ID` int NOT NULL UNIQUE,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `members` */

insert  into `user`(`ID`,`password`,`name`) values 

(1,'password1','Noel'),

(2,'password2','Jake'),

(3,'password3','Daniel');

/*Table structure for table `book` */

DROP TABLE IF EXISTS `book`;

CREATE TABLE `book` (
  `ID` int NOT NULL UNIQUE,
  `title` varchar(50) NOT NULL,
  `publisher` varchar(10) NOT NULL,
  `yearOfPublication` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `books` */

insert  into `book`(`ID`,`title`, `publisher`,`yearOfPublication`) values

(1,'Unlocking Android', 'amazon', 2009),
(2,'Android in Action, Second Edition', 'Manning', 2011),
(3,'Third Book', 'Manning', 2011),
(4,'Fore Four Fall', 'Manning', 2011),
(5,'Hi Five', 'Manning', 2011),
(6,'Six Sixes', 'Manning', 2011);

/*Table structure for table `fine` */

DROP TABLE IF EXISTS `fine`;

CREATE TABLE `fine` (
  `userID` int NOT NULL,
  `aggregatedAmount` double NOT NULL,
  PRIMARY KEY (`userID`),
  CONSTRAINT `fines_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fine` */

insert  into `fine`(`userID`, `aggregatedAmount`) values

(2, 30);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `ID` int NOT NULL,
  `amount` double NOT NULL,
  `userID` int NOT NULL,
  `fineUserID` int,
  PRIMARY KEY (`ID`),
  KEY `userID` (`userID`),
  KEY `fineUserID` (`fineUserID`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`ID`),
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`fineUserID`) REFERENCES `fine` (`userID`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `reserve` */

DROP TABLE IF EXISTS `reserve`;

CREATE TABLE `reserve` (
  `bookID` int NOT NULL,
  `reserverID` int NOT NULL,
  PRIMARY KEY (`bookID`, `reserverID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `borrow` */

DROP TABLE IF EXISTS `borrow`;

CREATE TABLE `borrow` (
  `bookID` int NOT NULL,
  `borrowerID` int NOT NULL,
  `borrowEndDate` date NOT NULL,
  PRIMARY KEY (`bookID`,`borrowerID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `borrow` */

insert  into `borrow`(`bookID`,`borrowerID`,`borrowEndDate`) values

(1, 1, '2021-02-06');

/*Table structure for table `author` */

DROP TABLE IF EXISTS `author`;

CREATE TABLE `author` (
  `authorID` int NOT NULL,
  `bookID` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`authorID`,`bookID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `author` */

insert  into `author`(`authorID`,`bookID`,`name`) values

(1, 1, 'W. Frank Ableson'),
(2, 2, 'Robi Sen'),
(2, 3, 'Robi Sen'),
(2, 4, 'Robi Sen'),
(2, 5, 'Robi Sen'),
(2, 6, 'Robi Sen');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `categoryID` int NOT NULL,
  `bookID` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`categoryID`,`bookID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`categoryID`,`bookID`,`name`) values

(1, 1, 'Open Source'),
(2, 2, 'Java'),
(1, 3, 'Open Source'),
(1, 4, 'Open Source'),
(1, 5, 'Open Source'),
(2, 6, 'Java');