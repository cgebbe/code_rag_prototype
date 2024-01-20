from celery import Celery
from pathlib import Path

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def add(x, y):
    (Path(__file__).parent / "foo.txt").write_text("foo foo")
    return x + y
