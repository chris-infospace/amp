from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

bingdata = {
   "HelloWorld": "true"
}

class GetBingData(Resource):
    def get(self):
        return bingdata

api.add_resource(GetBingData, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
