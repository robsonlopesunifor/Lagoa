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
