## Requirements
- Python 3.9
- Docker
- Docker Compose
- Redis
- Celery

## Installation
The `Dockerfile` will create a superuser when the build command is executed. It will also pre-install the test data into the database.

#### Clone the repository
    git clone git@github.com:tawanike/4sure-drones.git

#### Navigate into the `4sure-drones` directory
    cd 4sure-drones

#### Build the project using `docker-compose`
    docker-compose build

#### Run the project using `docker-compose`
    docker-compose up
Optionally you can run the project in daemon mode by add the -D flag to the command

#### Run the project using `docker-compose`
    docker-compose up -D

#### Demo credentials:
    username: admin
    password: querty
