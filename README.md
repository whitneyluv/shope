# install pre-commit
    create - .pre-commit-config.yaml
    pip install pre-commit
    pre-commit install(устанавливаем нашу настройку)

# desk for draw
    https://drive.google.com/file/d/1s06_sEs2wcnUmzBtt7tXKW_LBjFh4Jkk/view?usp=sharing

# file for url
    https://docs.google.com/spreadsheets/d/1J1eEcKVVjWlhMkDP26PAb5baP4Opq_MPgAApUw9dK-Q/edit?usp=sharing

# trello
    https://trello.com/b/G4pjuvLQ/pythondjangoteam38

# rule for commit
    origin/fixbugs/задача или номер задачи
    origin/feature/задача или номер задачи

# rule for dump data
    python fixtures_dumper.py

# rule for load data
    python manage.py migrate
    python manage.py import_fixtures (-f filename -e email (не обязательные аргументы))

# running Celery
    pip install -r requirements.txt
    celery -A shope worker --loglevel=info

# Running docker
    docker compose up -d --build - сборка перед стартом контейнеров
    docker compose up -d - запуск контейнеров (-d для запуска в фоне)
    docker compose down - остановка контейнеров
