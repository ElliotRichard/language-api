from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import scraping

app = Flask(__name__)
api = Api (app)
CORS(app)

class LanguageCode(Resource):
  def get(self, language):
    print("Request for code: " + language)
    code = scraping.getLanguageCode(language)
    return code

class LanguageFromCode(Resource):
  def get(self, code):
    print("Request for language:" + code)
    language = scraping.getLanguageFromCode(code)
    return language
  
api.add_resource(LanguageCode, '/','/language/<string:language>')
api.add_resource(LanguageFromCode, '/', '/code/<string:code>')

if __name__ == '__main__':
  print("Starting the language code API")
  app.run()
  # Development Mode
  # app.run(debug=True)