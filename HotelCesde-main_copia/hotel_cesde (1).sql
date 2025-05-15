-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-05-2025 a las 02:12:06
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hotel_cesde`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `origin` varchar(255) DEFAULT NULL,
  `occupation` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `last_name`, `email`, `password`, `status`, `origin`, `occupation`) VALUES
(67676, 'sara', 'tavares', 'sari@gmail.com', '12345', 0, 'itagui', 'modelo'),
(10376767, 'alejandra', 'gonzales', 'aleja@gmail.com', '1234', 0, 'itagui', 'desarrollador'),
(12345678, 'julio', 'jaramillo', 'julio@gmail.com', '1234', 0, 'itagui', 'desarrollador'),
(64684436, 'hector', 'mejia', 'hector@gmail.com', '1234', 0, 'medellin', 'panadero'),
(172773773, 'juanjo', 'velez', 'juan@gmail.com', '1234', 0, 'itagui', 'desarrollador'),
(193838388, 'gladys', 'arteaga', 'gladys@gmail.com', '1234', 0, 'itagui', 'panadera'),
(1038868812, 'alejandro', 'palacio', 'alejo@gmail.com', '1234', 0, 'itagui', 'desarrollador'),
(1104255156, 'Samuel', 'Laguna', 'samuh2004@gmail.com', '123456', 1, 'Medellín', 'Programador'),
(1203445544, 'alejandro', 'arteaga', 'alejo1@gmail.com', '1234', 0, 'itagui', 'desarrollador'),
(1822828282, 'bernardo', 'mira', 'bernardo@gmail.com', '1234', 0, 'medellin', 'desarrollador'),
(2147483647, 'diego', 'palacio', 'diego@gmail.com', '1234', 0, 'medellin', 'pintor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `employees`
--

CREATE TABLE `employees` (
  `user_id` int(11) NOT NULL,
  `rol` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitacion`
--

CREATE TABLE `habitacion` (
  `id` int(11) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habitacion`
--

INSERT INTO `habitacion` (`id`, `numero`, `tipo`, `precio`, `estado`) VALUES
(1, '2210', 'Doble', 200000.00, 'Disponible'),
(2, '2244', 'Doble', 20000.00, 'Ocupada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `monto` decimal(10,2) NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pagos`
--

INSERT INTO `pagos` (`id`, `id_cliente`, `monto`, `metodo_pago`, `fecha`) VALUES
(1, 10376767, 30000.00, 'Efectivo', '2025-05-14 00:29:19'),
(2, 10376767, 3000.00, 'Efectivo', '2025-05-14 18:22:06'),
(3, 1822828282, 20000.00, 'Efectivo', '2025-05-14 19:03:24');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `nombre` varchar(100) NOT NULL,
  `fecha_entrada` date NOT NULL,
  `fecha_salida` date NOT NULL,
  `tipo_habitacion` varchar(100) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`nombre`, `fecha_entrada`, `fecha_salida`, `tipo_habitacion`, `id`) VALUES
('julian', '2024-02-20', '2024-02-25', 'Individual', 1),
('alejandro', '2024-05-03', '2024-05-08', 'Doble', 2),
('alejandra', '2025-05-14', '2025-05-19', 'Doble', 3),
('alejo palacio', '2025-05-14', '2025-05-15', 'Individual', 4),
('bernardo', '2025-04-05', '2025-04-09', 'Doble', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios_elegidos`
--

CREATE TABLE `servicios_elegidos` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `servicio_nombre` varchar(100) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `fecha` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicios_elegidos`
--

INSERT INTO `servicios_elegidos` (`id`, `customer_id`, `servicio_nombre`, `precio`, `fecha`) VALUES
(1, 10376767, 'Spa', 50.00, '2025-05-13 21:23:55'),
(2, 1822828282, 'Desayuno buffet', 15.00, '2025-05-14 19:01:20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `status` enum('active','inactive') NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`user_id`);

--
-- Indices de la tabla `habitacion`
--
ALTER TABLE `habitacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `servicios_elegidos`
--
ALTER TABLE `servicios_elegidos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `customer`
--
ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT de la tabla `habitacion`
--
ALTER TABLE `habitacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `servicios_elegidos`
--
ALTER TABLE `servicios_elegidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `customer` (`customer_id`);

--
-- Filtros para la tabla `servicios_elegidos`
--
ALTER TABLE `servicios_elegidos`
  ADD CONSTRAINT `servicios_elegidos_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
