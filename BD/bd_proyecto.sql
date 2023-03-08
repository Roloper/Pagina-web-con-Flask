--Integrantes
---Alvarado Flores Sebastian Paulo 		20200149
---Alvarez Mamani Javier Arturo 		20200236
---Barral Larios Luis Elias 			20200036
---Campos Acosta Marx Dalesxandro 		20200163
---Carranza Dávila Williams 			18200137
---Chávez Domínguez Josseph del Piero 	20200099
---Figueroa Munive Sebastian Estefano 		19200221
---Perez Olaguivel Rolando German 		20200197


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

CREATE TABLE user_connections (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  connection_id INT NOT NULL,
  status ENUM('pendiente', 'aceptada') NOT NULL DEFAULT 'pendiente',
  PRIMARY KEY (id),
  INDEX user_connection_idx (user_id, connection_id),
  CONSTRAINT fk_user_connections_user_id FOREIGN KEY (user_id) REFERENCES usuario (id_usuario),
  CONSTRAINT fk_user_connections_connection_id FOREIGN KEY (connection_id) REFERENCES usuario (id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE publicaciones (
  id_publicacion INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  titulo VARCHAR(255) NOT NULL,
  contenido TEXT NOT NULL,
  imagen VARCHAR(255),
  PRIMARY KEY (id_publicacion),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--No implementada
CREATE TABLE `mycart` (
  `id_cart` int(200) NOT NULL,
  `id_usuario_comprador` int(200) NOT NULL,
  `id_producto` int(200) NOT NULL,
  `c_cantidad` int(255) NOT NULL,
  `c_fecha` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--No implementada
CREATE TABLE `producto` (
  `id_producto` int(200) NOT NULL PRIMARY KEY,
  `id_usuario` int(200) NOT NULL,
  `p_nombreproducto` varchar(255) NOT NULL,
  `p_categoria` varchar(255) NOT NULL,
  `p_descripcion` varchar(255) NOT NULL,
  `p_precio` float NOT NULL,
  `p_imagenproducto` varchar(5000),
  FOREIGN KEY (`id_usuario`) REFERENCES `usuario`(`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--No implemntado
CREATE TABLE IF NOT EXISTS `messages` (
  `id_mensajes` int(11) NOT NULL AUTO_INCREMENT,
  `body` text NOT NULL,
  `msg_by` int(11) NOT NULL,
  `msg_to` int(11) NOT NULL,
  `msg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mensajes`)
) ENGINE=MyISAM AUTO_INCREMENT=182 DEFAULT CHARSET=latin1;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
