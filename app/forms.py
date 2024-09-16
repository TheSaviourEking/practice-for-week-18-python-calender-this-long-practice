from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    TimeField,
    TextAreaField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired, ValidationError


class AppointmentForm(FlaskForm):
    """The Appointment Form class"""

    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[DataRequired()])
    start_time = TimeField("Start Time", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    end_time = TimeField("End Time", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private Event ?")
    submit = SubmitField("Create an appointment")

    def validate_end_date(self, field):
        """Validating end time"""
        start = datetime.combine(self.start_date.data, self.start_time.data)
        end = datetime.combine(field.data, self.end_time.data)
        if start >= end:
            msg = "End date/time must come after start date/time"
            raise ValidationError(msg)

        if self.start_date.data != self.end_date.data:
            raise ValidationError("Start and end date must be the same day")
