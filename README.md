# ECOMIO CRUD API

This is the containerised backend API needed for ecomio plugin to work.

## Add dummy entries to Destinations using

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