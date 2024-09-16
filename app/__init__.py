from flask import Flask
from . import routes, config

app = Flask(__name__)
# app.config.update({"SECRET_KEY": os.environ.get("SECRET_KEY")})
app.config.from_object(config.Config)
app.register_blueprint(routes.bp)
