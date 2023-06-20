# docker run -dp 5000:5000 -w /app -v ${PWD}:/app flask-api
from flask import Flask
from flask_smorest import Api
from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stori"
app.config["API_VERSION"] = "V1.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app=app)
api.register_blueprint(blp=StoreBlueprint)
api.register_blueprint(blp=ItemBlueprint)