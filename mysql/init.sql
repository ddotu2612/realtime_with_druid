CREATE TABLE `stockalert` (
  `chat_id` varchar(20) NOT NULL,
  `ticker` varchar(20) NOT NULL,
  `indicator` varchar(20) NOT NULL,
  `threshold` float,
  `direction` int
);

insert into `stockalert` (`chat_id`, `ticker`, `indicator`, `threshold`, `direction`) values 
('1', 'ABC', 'price', 12.4, 1);

COMMIT;