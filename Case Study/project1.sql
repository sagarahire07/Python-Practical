CREATE SCHEMA `project1` ;

CREATE TABLE `project1`.`project_table` (
  `prn_no` INT NOT NULL,
  `First_name` VARCHAR(45) NOT NULL,
  `Middle_name` VARCHAR(45) NOT NULL,
  `Last_name` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `Mobile_number` VARCHAR(45) NOT NULL,
  `Email_id` VARCHAR(45) NOT NULL,
  `DOB` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PrnNo`));

INSERT INTO `project1`.`project_table` (`prn_no`, `First_name`, `Middle_name`, `Last_name`, `Address`, `Mobile_number`, `Email_id`, `DOB`) VALUES ('2020', 'shubham', 'Chandrakant', 'karoshi', 'kolhapur', '9978658766', 'shubham@gmail.com', '25072002');
INSERT INTO `project1`.`project_table` (`prn_no`, `First_name`, `Middle_name`, `Last_name`, `Address`, `Mobile_number`, `Email_id`, `DOB`) VALUES ('2021', 'vicky', 'shubhash', 'pawar', 'mumbai', '9819664758', 'vickypawar1212@gmail.com', '04042002');
INSERT INTO `project1`.`project_table` (`prn_no`, `First_name`, `Middle_name`, `Last_name`, `Address`, `Mobile_number`, `Email_id`, `DOB`) VALUES ('2022', 'Neha', 'Sanjay', 'Ahire ', 'Mumbai', '9769416909', 'Nehaaire@gmail.com', '06042011');
INSERT INTO `project1`.`project_table` (`prn_no`, `First_name`, `Middle_name`, `Last_name`, `Address`, `Mobile_number`, `Email_id`, `DOB`) VALUES ('2023', 'apoorv', 'pandit', 'ahire', 'Mumbai', '8108908559', 'apoorvaahire@gmail.com', '02052010');
INSERT INTO `project1`.`project_table` (`prn_no`, `First_name`, `Middle_name`, `Last_name`, `Address`, `Mobile_number`, `Email_id`, `DOB`) VALUES ('2031', 'Sagar', 'Sanjay', 'Ahire', 'Mumbai', '9819339677', 'sagarahire@gmail.com', '05052002');
INSERT INTO `project1`.`project_table` (`prn_no`, `First_name`, `Middle_name`, `Last_name`, `Address`, `Mobile_number`, `Email_id`, `DOB`) VALUES ('2032', 'Rohit', 'Sanjay', 'Ahire', 'Mumbai', '9619039504', 'rohitahire@gmail.com', '30062000');

