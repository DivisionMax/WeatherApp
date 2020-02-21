# Weather Application

Developed with Python 3.7

## Setup

- Developed with SQLite (Postgres is ideal)

### Requirements

**Environment Variables**
- `SECRET_KEY`
- `DATABASE_URL` e.g. `sqlite:///weather_app.sql`

Usually email verification during signup is enforced but in this case it was excluded to simplify

Admin endpoint is moved to `/control`

## Assumptions

Assumed that forecasts can change, unsure if one per day should exist or allow multiple (may update to only allow one per day)

## API

API requires Basic Authentication, the user's email and password.
API documenation is available at `/api/swagger-ui`. Documentation is also protected.

## Services

Running the function to fetch the forecast information from News24 can be run as an admin command

`python manage.py fetch_news24_forecasts <city_id>`

E.g. Cape Town has a city id of `77107`.
