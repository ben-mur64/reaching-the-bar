CREATE TABLE schools( 
    short_name VARCHAR(64) NOT NULL PRIMARY KEY, 
    full_name VARCHAR(64) NOT NULL, 
    emp_percent FLOAT NOT NULL, 
    big_law FLOAT NOT NULL,
    small_law FLOAT NOT NULL,
    public_service FLOAT NOT NULL,
    clerkships FLOAT NOT NULL,
    unemp_percent FLOAT NOT NULL,
    debt FLOAT NOT NULL,
    attrition FLOAT NOT NULL,
    prestige FLOAT NOT NULL,
    gpa FLOAT NOT NULL,
    lsat FLOAT NOT NULL
);