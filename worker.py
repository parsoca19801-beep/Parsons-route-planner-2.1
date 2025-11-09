from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
app = Celery("optimizer", broker=REDIS_URL, backend=REDIS_URL)

from tasks.matrices import build_matrices  # noqa: F401
from tasks.optimize import solve_route     # noqa: F401
