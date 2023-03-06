SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "-05:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE TABLE `usuario` (
  `id_usuario` int(200) NOT NULL AUTO_INCREMENT,
  `a_name` varchar(255) NOT NULL,
  `a_username` varchar(255) NOT NULL,
  `a_password` varchar(255) NOT NULL,
  `a_email` varchar(255) NOT NULL,
  `a_descripcion` varchar(255) NOT NULL,
  `a_celular` varchar(20) NOT NULL,
  `a_ubicacion` varchar(255) NOT NULL,
  `a_imagenperfil` varchar(5000),
  `a_reg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `online` varchar(1) NOT NULL DEFAULT '0',
   PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE amigo (
    id_amigo INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    amigo_id INT,
    fecha_amistad DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id_usuario),
    FOREIGN KEY (amigo_id) REFERENCES usuario(id_usuario)
);

CREATE TABLE publicaciones (
  id_publicacion INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  titulo VARCHAR(255) NOT NULL,
  contenido TEXT NOT NULL,
  imagen LONGBLOB,
  fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_publicacion),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
  `p_imagenproducto` varchar(5000)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `messages`;

CREATE TABLE IF NOT EXISTS `messages` (
  `id_mensajes` int(11) NOT NULL AUTO_INCREMENT,
  `body` text NOT NULL,
  `msg_by` int(11) NOT NULL,
  `msg_to` int(11) NOT NULL,
  `msg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mensajes`)
) ENGINE=MyISAM AUTO_INCREMENT=182 DEFAULT CHARSET=latin1;

--INSERT INTO `messages` (`id`, `body`, `msg_by`, `msg_to`, `msg_time`) VALUES
--(178, 'hlw', 9, 12, '2018-07-23 14:13:38'),
--(177, 'hi', 12, 9, '2018-07-23 14:13:26');

ALTER TABLE `mycart`
  ADD PRIMARY KEY (`id_cart`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `id_usuario_comprador` (`id_usuario_comprador`);

-- Indices de la tabla `producto`
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_usuario` (`id_usuario`);

-- Indices de la tabla `usuario`
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas

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
