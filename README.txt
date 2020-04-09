W pliku baza.py proszę uzupełnić dane!

Aplikacja jest we wczesnej fazie! Wiele opcji może nie działać!

Kod SQL do stworzenia tablicy:

CREATE TABLE `XO` (
  `id` varchar(255) DEFAULT NULL,
  `x1` varchar(1) DEFAULT NULL,
  `x2` varchar(1) DEFAULT NULL,
  `x3` varchar(1) DEFAULT NULL,
  `x4` varchar(1) DEFAULT NULL,
  `x5` varchar(1) DEFAULT NULL,
  `x6` varchar(1) DEFAULT NULL,
  `x7` varchar(1) DEFAULT NULL,
  `x8` varchar(1) DEFAULT NULL,
  `x9` varchar(1) DEFAULT NULL,
  `gracz1` bit(1) DEFAULT NULL,
  `gracz2` bit(1) DEFAULT NULL,
  `teraz` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;