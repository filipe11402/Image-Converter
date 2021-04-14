from flask import Flask
from flask_restful import Api, Resource, abort


app = Flask(__name__)
api = Api(app)


names = {'Filipe': {'idade': 19},
        'Rui': {'idade': 30},
        }


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, '/teste/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)