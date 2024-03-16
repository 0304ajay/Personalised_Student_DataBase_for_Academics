-- Tables Creation

CREATE TABLE ADMINISTRATOR_TABLE_1(
    admin_Id INT NOT NULL PRIMARY KEY,
    admin_Name VARCHAR(50),
    passwrd VARCHAR(50)
);


-- PERSONAL DETAILS TABLE
CREATE TABLE PERSONAL_DETAILS_TABLE_2(
    first_Name VARCHAR(30) NOT NULL,
    last_Name VARCHAR(30) NOT NULL,
    Aadhar_Number VARCHAR(12) NOT NULL PRIMARY KEY,
    Date_Of_Birth VARCHAR(12) NOT NULL,
    phone_No VARCHAR(10) NOT NULL,
    Email_Id VARCHAR(30) NOT NULL,
    address VARCHAR(100) NOT NULL
);

-- TABLE FOR STORING THE VOTER DETAILS
CREATE TABLE VOTER_ID_TABLE_3(
 voter_Id VARCHAR(15) PRIMARY KEY,
 father_Name VARCHAR(40) NOT NULL,
 mother_Name VARCHAR(40) NOT NULL
 );
 

 CREATE TABLE TENTH_DETAILS_TABLE_4(
    tenth_School_Name VARCHAR(50) NOT NULL,
    tenth_Roll_No VARCHAR(50) NOT NULL,
    tenth_Year_Of_Passing VARCHAR(15) NOT NULL,
    tenth_Board VARCHAR(50) NOT NULL,
    tenth_Percentage VARCHAR(10) NOT NULL
 );


CREATE TABLE TWELTH_DETAILS_TABLE_5(
    twelth_College_Name VARCHAR(50) NOT NULL,
    twelth_Roll_No VARCHAR(25) NOT NULL,
    twelth_Year_Of_Passing VARCHAR(15) NOT NULL,
    twelth_Board VARCHAR(50) NOT NULL,
    twelth_Percentage VARCHAR(10) NOT NULL
);


CREATE TABLE GRADUATION_DETAILS_TABLE_6(
    graduation_College_Name VARCHAR(50),
    graduation_Roll_No VARCHAR(25),
    graduation_Year_Of_Passing VARCHAR(15),
    graduation_Board VARCHAR(50),
    SEM1_GPA FLOAT,
    SEM2_GPA FLOAT,
    SEM3_GPA FLOAT,
    SEM4_GPA FLOAT,
    SEM5_GPA FLOAT,
    SEM6_GPA FLOAT,
    SEM7_GPA FLOAT,
    SEM8_GPA FLOAT,
    graduation_Percentage FLOAT
);


CREATE TABLE NOTES_TABLE_7(
    note_Id INT,
    note_Title VARCHAR(100),
    note_Description VARCHAR(1000)
);
-- Executing the trigger for the aadhar details Table to trigger if the user tries to add more than one details
-- delimiter used to inform that all the code belongs to same query

-- DELIMITER //
-- CREATE TRIGGER check_personal_Details_limit
-- BEFORE INSERT ON PERSONAL_DETAILS_TABLE_2
-- FOR EACH ROW
-- BEGIN 
--     DECLARE num_Rows INT;
--     SELECT COUNT(*) INTO num_Rows FROM PERSONAL_DETAILS_TABLE_2;
    
--     IF num_Rows >= 1 THEN
--         SIGNAL SQLSTATE '01000'
--         SET MESSAGE_TEXT = 'WARNING: ONLY ONE PERSON DETAILS NEEDED TO BE STORED';
--     END IF;
-- END;
-- //


        
			
    
-- INSERTING INTO TABLES
INSERT INTO ADMINISTRATOR_TABLE_1 VALUES(1,'KODIDELA AJAY KUMAR REDDY','ajay0304');
INSERT INTO ADMINISTRATOR_TABLE_1 VALUES(2,'KODIDELA CHAITANYA KUMAR REDDY','chai0304');