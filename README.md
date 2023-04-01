# ECOMIO CRUD API

This is the containerised backend API needed for ecomio plugin to work.

## Instructions

* Clone the repo.

* Make sure docker is installed on the machine

* Run

```
docker-compose up
```

## Add a bunch of dummy entries to Destinations using. The average score determines the leaf color so try some variation ;D

```
curl --location --request POST 'http://localhost:8080/api/destination?format=json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "content": "Keep your masks handy! The air quality may not be great as the city gets most of its energy from coal",
    "air_quality": 20,
    "water_quality": 90,
    "energy_sources": 5
}'
```