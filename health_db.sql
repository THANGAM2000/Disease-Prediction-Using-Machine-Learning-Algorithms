-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2023 at 03:53 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `health_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `health_prediction`
--

CREATE TABLE `health_prediction` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `Symptoms1` varchar(100) NOT NULL,
  `Symptoms2` varchar(100) NOT NULL,
  `Symptoms3` varchar(100) NOT NULL,
  `Symptoms4` varchar(100) NOT NULL,
  `Symptoms5` varchar(100) NOT NULL,
  `rf` varchar(100) NOT NULL,
  `nb` varchar(100) NOT NULL,
  `dt` varchar(100) NOT NULL,
  `best` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `health_prediction`
--

INSERT INTO `health_prediction` (`id`, `name`, `Symptoms1`, `Symptoms2`, `Symptoms3`, `Symptoms4`, `Symptoms5`, `rf`, `nb`, `dt`, `best`) VALUES
(1, 'Name', 'Symptoms1', 'Symptoms2', 'Symptoms3', 'Symptoms4', 'Symptoms5', 'Random Forest', 'NaiveBayes', 'Decision Tree', 'Best'),
(2, 'arun', 'brittle_nails', 'depression', 'fluid_overload', 'history_of_alcohol_consumption', 'loss_of_balance', 'Drug Reaction', 'Drug Reaction', 'Drug Reaction', 'RF-96%'),
(3, 'balu', 'bloody_stool', 'coma', 'dizziness', 'dischromic _patches', 'dizziness', 'Fungal infection', 'Fungal infection', 'Fungal infection', 'RF-96%'),
(4, 'bubloo', 'blurred_and_distorted_vision', 'belly_pain', 'enlarged_thyroid', 'history_of_alcohol_consumption', 'inflammatory_nails', 'Drug Reaction', 'Drug Reaction', 'Psoriasis', 'RF-96%'),
(5, 'qwert', 'blood_in_sputum', 'coma', 'diarrhoea', 'dizziness', 'extra_marital_contacts', 'Gastroenteritis', 'AIDS', 'AIDS', 'RF-96%'),
(6, 'cv', 'chest_pain', 'constipation', 'depression', 'dizziness', 'enlarged_thyroid', 'GERD', 'GERD', 'Typhoid', 'RF-96%'),
(7, 'bvfg', 'abdominal_pain', 'brittle_nails', 'constipation', 'dischromic _patches', 'extra_marital_contacts', 'Jaundice', 'Fungal infection', 'AIDS', 'RF-96%'),
(8, 'abcdes', 'bloody_stool', 'chest_pain', 'constipation', 'diarrhoea', 'distention_of_abdomen', 'GERD', 'GERD', 'Dimorphic hemmorhoids(piles)', 'RF-96%'),
(9, 'dass', 'bloody_stool', 'bruising', 'continuous_feel_of_urine', 'depression', 'distention_of_abdomen', 'Drug Reaction', 'Drug Reaction', ' Migraine', 'RF-96%'),
(10, '', 'Select Here', 'Select Here', 'Select Here', 'Select Here', 'Select Here', '', '', '', 'RF-96%');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`username`, `password`, `name`, `contact`, `email`, `age`, `gender`) VALUES
('naresh', 'a234', 'naresh', '8675456387', 'naresh@gmail.com', '27', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `health_prediction`
--
ALTER TABLE `health_prediction`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `health_prediction`
--
ALTER TABLE `health_prediction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
