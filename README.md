# Smart Routing MVP Scaffold

This archive contains a starter scaffold for the routing MVP:
- FastAPI planner API
- Celery optimizer worker (OR-Tools ready)
- Alembic migrations
- Dev docker-compose (Postgres + Redis + services)
- Makefile targets

## Quick start (dev)

```bash
# 1) Start services
docker compose -f ops/docker/docker-compose.dev.yml up --build -d

# 2) Apply DB migration
docker compose -f ops/docker/docker-compose.dev.yml exec planner-api   bash -lc 'alembic -c /app/db/alembic.ini upgrade head'

# 3) Hit health check
curl http://localhost:8080/healthz
```

## Services
- planner-api: FastAPI, route import/optimize endpoints (stubs)
- optimizer-worker: Celery worker with tasks for matrix build & optimization (stubs)

You will need HERE/TomTom credentials when implementing matrix/route calls.
