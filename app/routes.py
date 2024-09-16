from os import environ
import psycopg2
from flask import Blueprint, render_template

CONNECTION_PARAMETERS = {
    "user": environ.get("DB_USER"),
    "password": environ.get("DB_PASS"),
    "dbname": environ.get("DB_NAME"),
    "host": environ.get("DB_HOST"),
}
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def main():
    """
    docstring to clear this error
    """

    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
                """
                    SELECT id, name, start_datetime, end_datetime FROM appointments
                    ORDER BY start_datetime
                """
            )

            rows = curs.fetchall()
    return render_template("main.html", rows=rows)
