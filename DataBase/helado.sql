-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2023 a las 05:25:10
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `helado`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `precioxcantidad`
--

CREATE TABLE `precioxcantidad` (
  `precio` float NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` int(4) NOT NULL,
  `idProducto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `nombre` varchar(20) DEFAULT NULL,
  `StockTotal` float DEFAULT NULL,
  `idProducto` int(4) NOT NULL,
  `idTipoProducto` int(4) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`nombre`, `StockTotal`, `idProducto`, `idTipoProducto`, `descripcion`) VALUES
('chocolate', 30, 1, 1, 'Helado Vegano con chocolate 70% cacao.'),
('Avellano', 15, 2, 1, 'Helado de Avellana, con chips de chocolate y trozos de avellana.'),
('Patagónico', 20, 3, 1, 'Helado de crema americana con mix de frutos rojos de la Patagonia Argentina.'),
('Bombón Suizo', 20, 4, 2, 'Helado de chocolate con corazón de dulce de leche natural y cobertura de chocolate con praliné de al'),
('Bombón Escocés', 20, 5, 2, 'Helado de crema americana con corazón de dulce de leche natural y cobertura de chocolate. Los bombon'),
('Almendrado', 20, 6, 2, 'Nuestro postre almendrado está realizado con ingredientes de altísima calidad. Tiene 15 porciones.'),
('Paleta Minion', 30, 7, 3, 'Cubierta de chocolate blanco italiano de origen belga, teñido con los clásicos colores azul y amaril'),
('Paleta Argenta', 30, 8, 3, 'Cubierta de chocolate blanco teñido con los colores argentinos, relleno de dulce de leche.'),
('Paleta Chantilly', 30, 9, 3, 'Rellena de crema chantilly, recubierto de chocolate belga semidulce y trocitos de maní caramelizados');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipodeproducto`
--

CREATE TABLE `tipodeproducto` (
  `idTipoProducto` int(3) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipodeproducto`
--

INSERT INTO `tipodeproducto` (`idTipoProducto`, `nombre`, `descripcion`) VALUES
(1, 'Sabores', 'Representan el listado de sabores de helados de venta a granel.'),
(2, 'Postres', 'Nuestros postres son helados y vienen listos para fraccionar en porciones. Rinden hasta 8 porciones.'),
(3, 'Paletas', 'Barras heladas en palitos');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `precioxcantidad`
--
ALTER TABLE `precioxcantidad`
  ADD PRIMARY KEY (`fecha`,`idProducto`),
  ADD KEY `idProducto` (`idProducto`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idProducto`),
  ADD KEY `idTipoProducto` (`idTipoProducto`);

--
-- Indices de la tabla `tipodeproducto`
--
ALTER TABLE `tipodeproducto`
  ADD PRIMARY KEY (`idTipoProducto`),
  ADD UNIQUE KEY `idTipoProducto` (`idTipoProducto`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `precioxcantidad`
--
ALTER TABLE `precioxcantidad`
  ADD CONSTRAINT `precioxcantidad_ibfk_1` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`idTipoProducto`) REFERENCES `tipodeproducto` (`idTipoProducto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
