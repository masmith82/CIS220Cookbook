use cookbook;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / create user
CREATE PROCEDURE create_user (IN f_name Varchar(50), IN l_name Varchar(50), IN email Varchar(100), IN nikname Varchar(50) )
-- define the procedure body
BEGIN
	-- declare the user ID 
	DECLARE user_id INT
    SET user_id = 1;
    
    -- search the user id in the user table
	SELECT user_id = MAX(user_ID)
	FROM User;
	SET user_id = user_id + 1;
    
	-- insert the information in the table
    INSERT INTO User (user_ID, first_name, last_name, email_address, username)
VALUES
    (user_id,f_name,l_name,email,nikname);
    
SELECT 'User created!!';
END $$
DELIMITER ;

-- get all the specific information from USER

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return first name for a specific user
CREATE PROCEDURE get_firstName_user (IN userID int, OUT first_name VARCHAR(50))
-- define the procedure body
BEGIN
    SELECT	
		first_name
    FROM
		User
	WHERE	 
		user_id = userID;
    
                                   
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return last name for a specific user
CREATE PROCEDURE get_lastName_user (IN userID int, OUT last_name VARCHAR(50))
-- define the procedure body
BEGIN
    SELECT	
		last_name
    FROM
		User
	WHERE	 
		user_ID = userID;
    
                                   
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return emil for a specific user
CREATE PROCEDURE get_email_user (IN userID int, OUT email VARCHAR(100))
-- define the procedure body
BEGIN
    SELECT	
		email_address
    FROM
		User
	WHERE	 
		user_ID = userID;
    
                                   
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return nickname for a specific user
CREATE PROCEDURE get_email_user (IN userID int, OUT username VARCHAR(50))
-- define the procedure body
BEGIN
    SELECT	
		username
    FROM
		User
	WHERE	 
		user_ID = userID;
        
END $$
DELIMITER ;


-- set all the specific information from USER

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / set first name for a specific user
CREATE PROCEDURE set_firstName_user (IN userID int, IN newName VARCHAR(50))
-- define the procedure body
BEGIN
	-- update the user table and set a specific user
    UPDATE	User
    set firt_name = newName;
    WHERE user_ID = userID;
    
    SELECT 'First name update correctly!!';
                                   
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / set last name for a specific user
CREATE PROCEDURE set_lastName_user (IN userID int, IN new_last_name VARCHAR(50))
-- define the procedure body
BEGIN
    -- update the user table and set a specific user
    UPDATE	User
    set last_name = new_last_name;
    WHERE user_ID = userID;
    
    SELECT 'Last name update correctly!!';
                                   
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / set emil for a specific user
CREATE PROCEDURE set_email_user (IN userID int, IN email VARCHAR(100))
-- define the procedure body
BEGIN
    -- update the user table and set a specific user
    UPDATE	User
    set email_address = email;
    WHERE user_ID = userID;
    
    SELECT 'Email update correctly!!';
    
                                   
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return nickname for a specific user
CREATE PROCEDURE get_email_user (IN userID, IN userName VARCHAR(50))
-- define the procedure body
BEGIN
    -- update the user table and set a specific user
    UPDATE	User
    set username = userName;
    WHERE user_ID = userID;
    
    SELECT 'Nickname update correctly!!';
        
END $$
DELIMITER ;

