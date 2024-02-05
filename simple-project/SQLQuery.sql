USE inventory_mangament_system
Go


CREATE SCHEMA product_schema
Go

CREATE SCHEMA Employee_schema

GO

CREATE TABLE product_schema.categories (
category_id int not null ,
category_name varchar(30) not null ,

CONSTRAINT category_pk PRIMARY KEY (category_id) 
)

CREATE TABLE product_schema.products (
product_id int not null ,
product_name varchar(30) not null , 
price float not null ,
category_id int not null, 

CONSTRAINT id_pk PRIMARY KEY (product_id) ,
CONSTRAINT category_id_fk FOREIGN KEY (category_id)
REFERENCES product_schema.categories (category_id)
)


CREATE TABLE Employee_schema.employee (
First_name varchar(30) not null,
last_name varchar(30) not null ,
id int not null ,
salary float not null ,
date date not null ,


CONSTRAINT ID_pk PRIMARY KEY (id) 

)

ALTER TABLE Employee_schema.employee
ADD CONSTRAINT salary_CH CHECK (salary between 3000 and 50000)

CREATE TABLE Reports(
report_name varchar(30) not null ,
report_Date date not null 
)









