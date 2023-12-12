use cookbook;

DROP PROCEDURE IF EXISTS create_user;
DROP PROCEDURE IF EXISTS get_firstName_user;
DROP PROCEDURE IF EXISTS get_lastName_user;
DROP PROCEDURE IF EXISTS get_email_user;
DROP PROCEDURE IF EXISTS get_user_name;

DROP PROCEDURE IF EXISTS set_lastName_user;
DROP PROCEDURE IF EXISTS set_firstName_user;
DROP PROCEDURE IF EXISTS set_email_user;
DROP PROCEDURE IF EXISTS set_nickname;
DROP PROCEDURE IF EXISTS set_firstName_user;
DROP PROCEDURE IF EXISTS check_password;
DROP PROCEDURE IF EXISTS search_user;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / create user
CREATE PROCEDURE create_user (IN f_name VARCHAR(50), IN l_name VARCHAR(50), IN email VARCHAR(100), IN nickname VARCHAR(50) )
-- define the procedure body
BEGIN
	-- declare the user ID 
	DECLARE user_id INT;
   
  -- search the user id in the user table
  SELECT MAX(user_id) + 1 INTO user_id
  FROM user;
    
	-- insert the information in the table
  INSERT INTO user (user_id, first_name, last_name, email_address, username)
  VALUES
    (user_id,f_name,l_name,email,nickname);
    
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
		user
	WHERE	 
		user_id = userID;
    
                                   
END $$
DELIMITER ;

-- get user's last name
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return last name for a specific user
CREATE PROCEDURE get_lastName_user (IN userID int, OUT last_name VARCHAR(50))
-- define the procedure body
BEGIN
    SELECT	
		last_name
    FROM
		user
	WHERE	 
		user_id = userID;                                   
END $$
DELIMITER ;

-- get user's email
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$
-- Input parameters and output parameters / return emil for a specific user
CREATE PROCEDURE get_email_user (IN userID int, OUT email_address VARCHAR(100))
-- define the procedure body
BEGIN
    SELECT email_address
    FROM user
    WHERE user_id = userID;
END $$

DELIMITER ;
    
-- get user's nickname
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return nickname for a specific user
CREATE PROCEDURE get_user_name (IN userID int, OUT username VARCHAR(50))
-- define the procedure body
BEGIN
    SELECT	
		username
    FROM
		user
	WHERE	 
		user_id = userID;
        
END $$
DELIMITER ;

----
-- set all the specific information from USER
----

DROP PROCEDURE IF EXISTS set_firstName_user;
DELIMITER $$
USE cookbook$$

CREATE PROCEDURE set_firstName_user(IN userID INT, IN newName VARCHAR(50))
BEGIN
    -- update the user table and set a specific user
    UPDATE user
    SET first_name = newName
    WHERE user_id = userID;
    
    SELECT 'First name updated correctly!' AS Result; 

END $$
DELIMITER ;

-- set user's last name
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / set last name for a specific user
CREATE PROCEDURE set_lastName_user (IN userID int, IN new_last_name VARCHAR(50))
-- define the procedure body
BEGIN
    -- update the user table and set a specific user
    UPDATE	user
    set last_name = new_last_name
    WHERE user_id = userID;
    
    SELECT 'Last name update correctly!!';
                                   
END $$
DELIMITER ;

-- set user's email
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / set email for a specific user
CREATE PROCEDURE set_nickname (IN userID int, IN new_nickname VARCHAR(50))
-- define the procedure body
BEGIN
    -- update the user table and set a specific user
    UPDATE	user
    set nickname = new_nickname
    WHERE user_id = userID;
    
    SELECT 'Nickname updated!';
    
                                   
END $$
DELIMITER ;

-- set user's nickname
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return nickname for a specific user
CREATE PROCEDURE set_email_user (IN userID INT, IN new_email VARCHAR(50))
-- define the procedure body
BEGIN
    -- update the user table and set a specific user
    UPDATE	user
    SET email_address = email
    WHERE user_id = userID;

    SELECT 'Email updated!';
            
END $$
DELIMITER ;

-- search user by name, returns user-ID, or -1 if user not found
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$
-- Input parameters and output parameters / return nickname for a specific user
CREATE PROCEDURE search_user(IN userName VARCHAR(50), OUT found_user INT)

BEGIN
    SELECT user_id INTO found_user FROM user WHERE username = userName;
END $$

DELIMITER ;

-- check password
DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$
-- Input parameters and output parameters / return nickname for a specific user
CREATE PROCEDURE check_password (IN pword VARCHAR(50), OUT valid TINYINT)

BEGIN
    SET valid = 0;

    -- check password, returns 1 if password matches, else returns 0
    IF (password = pword) THEN
        SET valid = 1;
    END IF;
END $$
DELIMITER ;