CREATE TABLE `empresa` (
  `id_empresa` int(100) NOT NULL,
  `e_nombre` varchar(100) NOT NULL,
  `e_username` varchar(100) NOT NULL,
  `e_password` varchar(100) NOT NULL,
  `e_email` varchar(100) NOT NULL,
  `e_celular` varchar(100) NOT NULL,
  `e_ubicacion` text NOT NULL,
  `e_activo` int(100) NOT NULL DEFAULT '0'
  `e_rating` int(11) NOT NULL DEFAULT '0',
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `farmer`
--

CREATE TABLE `agricultor` (
  `id_agricultor` int(255) NOT NULL,
  `a_name` varchar(255) NOT NULL,
  `a_username` varchar(255) NOT NULL,
  `a_password` varchar(255) NOT NULL,
  `a_email` varchar(255) NOT NULL,
  `a_celular` varchar(255) NOT NULL,
  `a_ubicacion` text NOT NULL,
  `a_activo` int(255) NOT NULL DEFAULT '0',
  `a_rating` int(11) NOT NULL DEFAULT '0',
  `a_imagenperfil` varchar(255) NOT NULL DEFAULT 'png',
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `farmer`
--

--INSERT INTO `farmer` (`fid`, `fname`, `fusername`, `fpassword`, `fhash`, `femail`, `fmobile`, `faddress`, `factive`, `frating`, `picExt`, `picStatus`) VALUES
--(3, 'Kaivalya Hemant Mendki', 'ThePhenom', '$2y$10$22ezmzHRa9c5ycHmVm5RpOnlT4LwFaDZar1XhmLRJQKGrcVRhPgti', '61b4a64be663682e8cb037d9719ad8cd', 'kmendki98@gmail.com', '8600611198', 'abcde', 0, 0, 'png', 0);

-- --------------------------------------------------------

--
-- Table structure for table `fproduct`
--

CREATE TABLE `producto` (
  `p_fid` int(255) NOT NULL,
  `p_pid` int(255) NOT NULL,
  `p_nombreproducto` varchar(255) NOT NULL,
  `p_categoria` varchar(255) NOT NULL,
  `p_descripcion` varchar(255) NOT NULL,
  `p_precio` float NOT NULL,
  `p_imagen` varchar(255) NOT NULL DEFAULT 'blank.png',
  `p_estado` int(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fproduct`
--

--INSERT INTO `fproduct` (`fid`, `pid`, `product`, `pcat`, `pinfo`, `price`, `pimage`, `picStatus`) VALUES
--(3, 27, 'Mango', 'Fruit', '<p>Mango raseela</p>\r\n', 500, 'Mango3.jpeg', 1),
--(3, 28, 'Ladyfinger', 'Vegetable', '<p>Its veggie</p>\r\n', 1000, 'Ladyfinger3.jpg', 1),
--(3, 29, 'Bajra', 'Grains', '<p>bajre di rti</p>\r\n', 400, 'Bajra3.jpg', 1),
--(3, 30, 'Banana', 'Fruit', '<p>Jalgaon banana</p>\r\n', 400, 'Banana3.jpg', 1);


-- --------------------------------------------------------

--
-- Table structure for table `mycart`
--

CREATE TABLE `mycart` (
  `c_bid` int(10) NOT NULL,
  `c_pid` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mycart`
--

--INSERT INTO `mycart` (`bid`, `pid`) VALUES
--(3, 27),
--(3, 30);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaccion` (
  `t_id` int(10) NOT NULL,
  `t_bid` int(10) NOT NULL,
  `t_pid` int(10) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--