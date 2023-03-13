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
- While the image is running, using pgAdmin for see the database and test the connection