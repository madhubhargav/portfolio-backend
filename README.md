# portfolio-backend

## Linting

```
prospector portfolio_backend/
```

## Docker
Run server using the following command:
```
docker-compose up
```

Run the following command on a separate shell to stop docker server:
```
docker-compose down
```

Run the following commands to generate and run migrations:
```
docker-compose exec web pipenv run python manage.py makemigrations
docker-compose exec web pipenv run python manage.py migrate
```

Run django shell using the following command:
```
docker-compose exec web pipenv python manage.py shell
```

Install a new pip package by running this command:
```
docker-compose exec web pipenv install <package_name> [--dev]
```
