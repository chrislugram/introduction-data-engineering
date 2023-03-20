# Description

This folder contains a process for create in local a docker image with postgres and fill the database with a specific .csv

# Requirements

- Docker
- pipenv
- pgAdmin

## Prepare database

- Download the docker image with postgres
```
docker pull postgress
```
- Run the image 
```
docker run --name base-postgres -p 5455:5432 -e POSTGRES_USER=postgresUser -e POSTGRES_PASSWORD=postgresPW -e POSTGRES_DB=postgresDB -d postgres
```
- While the image is running, using pgAdmin for see the database and test the connection.

If it's the first time that create the images, use this for table creation:

```
CREATE TABLE CARSALESTABLE (
	price int NOT NULL,
	mileage int NOT NULL,
	engType VARCHAR ( 20 ) NOT NULL,
	year int NOT NULL,
	model VARCHAR ( 30 ) NOT NULL
);
```
  