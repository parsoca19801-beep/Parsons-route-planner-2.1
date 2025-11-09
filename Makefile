dev-up:
	docker compose -f ops/docker/docker-compose.dev.yml up --build -d

dev-down:
	docker compose -f ops/docker/docker-compose.dev.yml down -v

db-migrate:
	docker compose -f ops/docker/docker-compose.dev.yml exec planner-api bash -lc 'alembic -c /app/db/alembic.ini upgrade head'

test:
	echo "No tests yet"
