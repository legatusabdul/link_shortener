from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_restful_swagger import swagger

from infra.database import init_db


app = Flask(__name__)
app.url_map.strict_slashes = False
api = swagger.docs(Api(app), apiVersion='0.1')

# enable CORS (allow cross-site requests)
CORS(app, resources={r"/*": {"origins": "*"}})


class HelloWorld(Resource):
    def get(self):
        return "URL shorter"


api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    
    # # Init DB in multiple ways based on DB_MODE environment variable
    init_db(app)
    
    from api.url_api import Url
    api.add_resource(Url, "/urls")
    api.add_resource(Url, "/urls/<int:url_id>")


    app.run(debug=False)
