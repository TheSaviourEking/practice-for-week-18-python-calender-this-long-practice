from os import environ
from datetime import datetime, timedelta
import psycopg2
from flask import Blueprint, render_template, redirect, url_for
from .forms import AppointmentForm

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
    date = datetime.now()
    return redirect(url_for(".daily", year=date.year, month=date.month, day=date.day))


# @bp.route("/<int:year>/<int:month>/<int:day>/", methods=["GET", "POST"])
# def daily(year, month, day):
#     """Get daily appointment"""
#     form = AppointmentForm()

#     if form.validate_on_submit():
#         print(
#             {
#                 "name": form.name.data,
#                 "start_datetime": datetime.combine(
#                     form.start_date.data, form.start_time.data
#                 ),
#                 "end_datetime": datetime.combine(
#                     form.end_date.data, form.end_time.data
#                 ),
#                 "description": form.description.data,
#                 "private": form.private.data,
#             }
#         )

#         with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#             with conn.cursor() as curs:
#                 curs.execute(
#                     """
#                         INSERT into appointments(
#                         name, start_datetime, end_datetime, description, private
#                         )
#                         VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s)
#                     """,
#                     {
#                         "name": form.name.data,
#                         "start_datetime": datetime.combine(
#                             form.start_date.data, form.start_time.data
#                         ),
#                         "end_datetime": datetime.combine(
#                             form.end_date.data, form.end_time.data
#                         ),
#                         "description": form.description.data,
#                         "private": form.private.data,
#                     },
#                 )

#                 return redirect("/")

#     with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:

#         day = datetime(year, month, day)
#         next_day = day + timedelta(days=1)

#         with conn.cursor() as curs:
#             curs.execute(
#                 """
#                     SELECT id, name, start_datetime, end_datetime
#                     FROM appointments
#                     WHERE start_datetime BETWEEN %(day)s AND %(next_day)s
#                     ORDER BY start_datetime;
#                 """,
#                 {
#                     "day": day,
#                     "next_day": next_day,
#                 },
#             )

#             rows = curs.fetchall()
#             return render_template("main2.html", rows=rows, form=form)


@bp.route("/<int:year>/<int:month>/<int:day>/", methods=["GET", "POST"])
def daily(year, month, day):
    """Get daily appointment"""
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

        day = datetime(year, month, day)
        next_day = day + timedelta(days=1)

        with conn.cursor() as curs:
            curs.execute(
                """
                    SELECT id, name, start_datetime, end_datetime
                    FROM appointments
                    WHERE start_datetime BETWEEN %(day)s AND %(next_day)s
                    ORDER BY start_datetime;
                """,
                {
                    "day": day,
                    "next_day": next_day,
                },
            )

            rows = curs.fetchall()
            # rows = [
            #     (id, title, (end - start).seconds / 60 // 15, start)
            #     for (id, title, start, end) in rows
            # ]

            rows = [
                (
                    id,
                    title,
                    (end - start).seconds / 60 // 15,
                    datetime.strftime(start, "%I:%M %p").lstrip('0'),
                )
                for (id, title, start, end) in rows
            ]

            print(rows)
            return render_template("main.html", rows=rows, form=form)
