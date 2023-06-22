FROM postgres:15-alpine

copy ./db /docker-entrypoint-initdb.d/