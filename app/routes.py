from os import environ
import psycopg2
from flask import Blueprint, render_template, redirect, request, flash
from .forms import AppointmentForm
from datetime import datetime

CONNECTION_PARAMETERS = {
    "user": environ.get("DB_USER"),
    "password": environ.get("DB_PASS"),
    "dbname": environ.get("DB_NAME"),
    "host": environ.get("DB_HOST"),
}

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def main():
    """
    docstring to clear this error
    """
    form = AppointmentForm()

    if form.validate_on_submit():
        print(
            {
                "name": form.name.data,
                "start_datetime": datetime.combine(
                    form.start_date.data, form.start_time.data
                ),
                "end_datetime": datetime.combine(
                    form.end_date.data, form.end_time.data
                ),
                "description": form.description.data,
                "private": form.private.data,
            }
        )

        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                    """
                        INSERT into appointments(
                        name, start_datetime, end_datetime, description, private
                        )
                        VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s)
                    """,
                    {
                        "name": form.name.data,
                        "start_datetime": datetime.combine(
                            form.start_date.data, form.start_time.data
                        ),
                        "end_datetime": datetime.combine(
                            form.end_date.data, form.end_time.data
                        ),
                        "description": form.description.data,
                        "private": form.private.data,
                    },
                )
                
                return redirect("/")

    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
                """
                    SELECT id, name, start_datetime, end_datetime FROM appointments
                    ORDER BY start_datetime
                """
            )

            rows = curs.fetchall()
            return render_template("main.html", rows=rows, form=form)
