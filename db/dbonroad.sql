-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 15, 2020 at 05:58 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbonroad`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblfeedback`
--

CREATE TABLE IF NOT EXISTS `tblfeedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `workId` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `fdate` datetime NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblfeedback`
--

INSERT INTO `tblfeedback` (`fid`, `workId`, `feedback`, `fdate`) VALUES
(1, 6, 'srthtrhgt', '2020-01-07 11:48:28');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`username`, `password`, `utype`, `status`) VALUES
('shilpa@gmail.com', 'shilpa@123', 'user', '1'),
('jeena@gmail.com', 'jeena@123', 'user', '1'),
('raghu@gmail.com', 'raghu@123', 'mechanic', '1'),
('mridul@gmail.com', 'mridul@123', 'mechanic', '1'),
('admin@gmail.com', 'admin', 'admin', '1'),
('shyam@gmail.com', 'shyam@123', 'mechanic', '0'),
('arjun@gmail.com', 'arjun@123', 'mechanic', '0');

-- --------------------------------------------------------

--
-- Table structure for table `tblmechanic`
--

CREATE TABLE IF NOT EXISTS `tblmechanic` (
  `mName` varchar(50) NOT NULL,
  `mContact` varchar(50) NOT NULL,
  `mLocation` varchar(50) NOT NULL,
  `lat` float(10,6) NOT NULL,
  `lon` float(10,6) NOT NULL,
  `mEmail` varchar(50) NOT NULL,
  PRIMARY KEY (`mEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblmechanic`
--

INSERT INTO `tblmechanic` (`mName`, `mContact`, `mLocation`, `lat`, `lon`, `mEmail`) VALUES
('Arjun', '9519517530', 'Aluva', 10.102020, 76.363380, 'arjun@gmail.com'),
('Mridul', '9517538246', 'Aluva', 10.102020, 76.363380, 'mridul@gmail.com'),
('Raghavendra', '9632587410', 'Fort Kochi', 9.958230, 76.252922, 'raghu@gmail.com'),
('Shyam', '9874563210', 'Fort Kochi', 9.958230, 76.252922, 'shyam@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tbluser`
--

CREATE TABLE IF NOT EXISTS `tbluser` (
  `uName` varchar(50) NOT NULL,
  `uContact` varchar(50) NOT NULL,
  `uEmail` varchar(50) NOT NULL,
  PRIMARY KEY (`uEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbluser`
--

INSERT INTO `tbluser` (`uName`, `uContact`, `uEmail`) VALUES
('Jeena', '9651470283', 'jeena@gmail.com'),
('Shilpa', '9568401238', 'shilpa@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tblworkrequest`
--

CREATE TABLE IF NOT EXISTS `tblworkrequest` (
  `workId` int(11) NOT NULL AUTO_INCREMENT,
  `uEmail` varchar(50) NOT NULL,
  `wDesc` varchar(100) NOT NULL,
  `lat` varchar(10) NOT NULL,
  `lon` varchar(10) NOT NULL,
  `wEmail` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`workId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `tblworkrequest`
--

INSERT INTO `tblworkrequest` (`workId`, `uEmail`, `wDesc`, `lat`, `lon`, `wEmail`, `status`) VALUES
(1, 'shilpa@gmail.com', 'fgrerf', '10.10354', '76.35909', '', 'Requested'),
(2, 'shilpa@gmail.com', 'jhg', '10.10490', '76.36973', '', 'Requested'),
(3, 'shilpa@gmail.com', 'sdfcsw', '10.10388', '76.36613', '', 'Requested'),
(4, 'shilpa@gmail.com', 'zdfvgdrf', '10.10118', '76.36870', '', 'Requested'),
(5, 'shilpa@gmail.com', 'rfgverfg', '10.10557', '76.36596', '', 'Requested'),
(6, 'shilpa@gmail.com', 'rfgerfg', '10.10695', '76.36356', 'mridul@gmail.com', 'completed');
