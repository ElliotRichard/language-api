from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import scraping

app = Flask(__name__)
api = Api (app)
CORS(app)

class LanguageCode(Resource):
  def get(self, language):
    print("Request for language: " + language)
    object = scraping.getLanguageCode(language)
    return object['code']
  
api.add_resource(LanguageCode, '/','/language/<string:language>')
  
if __name__ == '__main__':
  print("Starting the language code API")
  app.run()
  # Development Mode
  # app.run(debug=True)