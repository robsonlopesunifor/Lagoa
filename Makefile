build:
	docker-compose build

bash:
	@echo "--> Bash."
	docker-compose run lagoa-app bash

up:
	@echo "--> Up."
	docker-compose up

down:
	@echo "--> Down."
	docker-compose down

test:
	docker-compose run lagoa-app pytest

lint:
	@echo "--> Lint"
	docker-compose run lagoa-app bash -c "./scripts/start-lint.sh"

create-revisions:
	@echo "--> Alembic autogenerate revisions"
	docker-compose run lagoa-app bash -c "./scripts/create-revision.sh"

downgrade:
	docker-compose run lagoa-app bash -c "alembic downgrade -1"

upgrade:
	docker-compose run lagoa-app bash -c "alembic upgrade +1"

run-revisions:
	@echo "--> Alembic run revisions"
	docker-compose run lagoa-app bash -c "alembic upgrade head"

history:
	@echo "--> Alembic run history"
	docker-compose run lagoa-app bash -c "alembic history"

atual:
	@echo "--> Alembic run history"
	docker-compose run lagoa-app bash -c "alembic history -i"