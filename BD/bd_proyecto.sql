-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-03-2023 a las 09:50:44
-- Versión del servidor: 10.4.13-MariaDB
-- Versión de PHP: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "-05:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_proyecto`

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `id_empresa` int(200) NOT NULL,
  `id_dueno` int(200) NOT NULL,
  `e_nombre` varchar(255) NOT NULL,
  `e_username` varchar(255) NOT NULL,
  `e_password` varchar(255) NOT NULL,
  `e_email` varchar(255) NOT NULL,
  `e_celular` varchar(20) NOT NULL,
  `e_ubicacion` varchar(255) NOT NULL,
  `e_imagenperfil` varchar(255) NOT NULL DEFAULT 'png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mycart`
--

CREATE TABLE `mycart` (
  `id_cart` int(200) NOT NULL,
  `id_usuario_comprador` int(200) NOT NULL,
  `id_producto` int(200) NOT NULL,
  `c_cantidad` int(255) NOT NULL,
  `c_fecha` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(200) NOT NULL,
  `id_usuario` int(200) NOT NULL,
  `p_nombreproducto` varchar(255) NOT NULL,
  `p_categoria` varchar(255) NOT NULL,
  `p_descripcion` varchar(255) NOT NULL,
  `p_precio` float NOT NULL,
  `p_imagenproducto` varchar(255) NOT NULL DEFAULT 'blank.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(200) NOT NULL,
  `a_name` varchar(255) NOT NULL,
  `a_username` varchar(255) NOT NULL,
  `a_password` varchar(255) NOT NULL,
  `a_email` varchar(255) NOT NULL,
  `a_celular` varchar(20) NOT NULL,
  `a_ubicacion` varchar(255) NOT NULL,
  `a_imagenperfil` varchar(255) NOT NULL DEFAULT 'png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id_empresa`),
  ADD KEY `id_dueno` (`id_dueno`);

--
-- Indices de la tabla `mycart`
--
ALTER TABLE `mycart`
  ADD PRIMARY KEY (`id_cart`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `id_usuario_comprador` (`id_usuario_comprador`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id_empresa` int(200) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mycart`
--
ALTER TABLE `mycart`
  MODIFY `id_cart` int(200) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(200) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(200) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD CONSTRAINT `empresa_ibfk_1` FOREIGN KEY (`id_dueno`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `mycart`
--
ALTER TABLE `mycart`
  ADD CONSTRAINT `mycart_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  ADD CONSTRAINT `mycart_ibfk_2` FOREIGN KEY (`id_usuario_comprador`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
