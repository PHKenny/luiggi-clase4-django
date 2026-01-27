.PHONY: up
up: pull
	docker compose up -d --build

.PHONY: down
down:
	docker compose down --remove-orphans --volumes

.PHONY: pull
pull:
	docker compose pull

.PHONY: psql
psql:
	docker exec -it luiggi-pg psql -U luiggi -d luiggi