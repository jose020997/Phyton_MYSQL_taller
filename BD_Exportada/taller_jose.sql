-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-06-2022 a las 21:26:39
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `taller_jose`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arregla`
--

CREATE TABLE `arregla` (
  `Cod_Averia` int(5) NOT NULL,
  `Matricula` varchar(7) NOT NULL,
  `DNI` int(9) NOT NULL,
  `Fech_Repara` date NOT NULL,
  `Horas` int(3) NOT NULL,
  `Problema` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arregla`
--

INSERT INTO `arregla` (`Cod_Averia`, `Matricula`, `DNI`, `Fech_Repara`, `Horas`, `Problema`) VALUES
(1, '1234567', 22222222, '2022-06-06', 26, 'Tubo de escape roto, hemos cambiado el espejo tambien'),
(2, 'jose12', 22222222, '2022-06-08', 2, 'huele a gasolina'),
(3, '123', 0, '0000-00-00', 0, 'Cambio de aceite');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `DNI` int(9) NOT NULL,
  `Nombre` varchar(80) NOT NULL,
  `Telefono` int(11) NOT NULL,
  `Correo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`DNI`, `Nombre`, `Telefono`, `Correo`) VALUES
(11111111, 'carlitos', 234234234, 'carlitos@carlitos'),
(11111133, 'manoli', 5676577, 'manoli@manoli'),
(12121212, 'jose', 682002121, 'jose@jose'),
(26509008, 'Jose Antonio', 682800160, 'jabg0014@red.ujaen.es'),
(88888888, 'rosita', 456454545, 'rosita@flor.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coche`
--

CREATE TABLE `coche` (
  `Matricula` varchar(20) NOT NULL,
  `DNI` int(9) NOT NULL,
  `Modelo` varchar(20) NOT NULL,
  `Marca` varchar(20) NOT NULL,
  `Color` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `coche`
--

INSERT INTO `coche` (`Matricula`, `DNI`, `Modelo`, `Marca`, `Color`) VALUES
('123', 26509008, 'bmw', 'serie6', 'azul'),
('12312311', 11111111, 'bmw', 'azul', 'azul'),
('1231234', 11111111, 'bmw', 'vmw', 'ghjl'),
('123412', 11111133, 'jjj', 'jjj', 'jj'),
('123455', 26509008, 'bmw', 'serie5', 'azul'),
('1234567', 26509008, 'Fiesta', 'Ford', 'Gris'),
('jose12', 26509008, 'Fiesta', 'Ford', 'Gris'),
('matricul12', 88888888, 'bmw', 'serie7', 'verde');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mecanico`
--

CREATE TABLE `mecanico` (
  `DNI` int(9) NOT NULL,
  `Nombre` varchar(40) NOT NULL,
  `Fecha_Contrata` date NOT NULL,
  `Salario` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `mecanico`
--

INSERT INTO `mecanico` (`DNI`, `Nombre`, `Fecha_Contrata`, `Salario`) VALUES
(0, '0', '0000-00-00', 0),
(22222222, 'David Barrios Lopez', '2022-06-05', 1200),
(45454545, 'carlitos', '2022-06-08', 1500),
(2147483647, 'Carlos', '2022-06-08', 1566);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `arregla`
--
ALTER TABLE `arregla`
  ADD PRIMARY KEY (`Cod_Averia`),
  ADD KEY `DNI` (`DNI`) USING BTREE,
  ADD KEY `Matricula` (`Matricula`) USING BTREE;

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`DNI`);

--
-- Indices de la tabla `coche`
--
ALTER TABLE `coche`
  ADD PRIMARY KEY (`Matricula`),
  ADD KEY `DNI` (`DNI`) USING BTREE;

--
-- Indices de la tabla `mecanico`
--
ALTER TABLE `mecanico`
  ADD PRIMARY KEY (`DNI`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `arregla`
--
ALTER TABLE `arregla`
  ADD CONSTRAINT `arregla_ibfk_1` FOREIGN KEY (`Matricula`) REFERENCES `coche` (`Matricula`),
  ADD CONSTRAINT `arregla_ibfk_2` FOREIGN KEY (`DNI`) REFERENCES `mecanico` (`DNI`);

--
-- Filtros para la tabla `coche`
--
ALTER TABLE `coche`
  ADD CONSTRAINT `coche_ibfk_1` FOREIGN KEY (`DNI`) REFERENCES `cliente` (`DNI`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
