<div align="center">

<h1>VideoHub</h1>

</div>

### Technology Stack

* **Django** — High-level Python web framework for rapid development.
* **Django REST Framework (DRF)** — Toolkit for building Web APIs in Django.
* **drf-spectacular** — Generates OpenAPI 3 schema and Swagger documentation for DRF.
* **PostgreSQL** — Robust open-source relational database used for storing application data.
* **psycopg2-binary** — PostgreSQL adapter for Python, used by Django to connect to the database.
* **Faker** — Library for generating fake data for testing and development.

### Installation

Clone the project and navigate to the project directory:

```shell
git clone git@github.com:ESergievich/videohub.git && cd videohub && cp .env.template .env
```

Then run the application using Docker Compose:

```shell
docker-compose up
```

The backend server will be available at:
http://localhost:8000

Interactive API documentation will be available at:
http://localhost:8000/v1/docs/

#### Generating Test Data

To populate the database with fake users, ads, and proposals for testing:

```shell
python manage.py seed
```

Available flags:

* --users — Number of users to create (default is 10)
* --videos — Number of videos to create (default is 10)
* --cleardb — Clear the database before seeding

Example:

```shell
python manage.py seed --users=15  --videos=50 --cleardb
```
