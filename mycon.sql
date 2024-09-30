DROP TABLE BILLING; 

CREATE TABLE BILLING(
    curr_date DATE,
    Item_ID VARCHAR2(50),
    Item_Name VARCHAR2(50),
    Karat NUMBER,
    Today_Gold_Price NUMBER,
    Weight NUMBER,
    Price NUMBER
    )
    
SELECT * FROM BILLING;