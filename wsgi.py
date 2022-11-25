from app import create_app
import os

server_software = os.environ.get('SERVER_SOFTWARE', '')
is_gunicorn = "gunicorn" in server_software

app = create_app()

print(
     "SERVER_SOFTWARE: "
    f"{server_software}"
)


if __name__ != "__main__":
    if is_gunicorn:
        print("Setting up Gunicorn logging.")
        import logging
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

