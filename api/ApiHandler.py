from flask_restful import Api, Resource

class ApiHandler(Resource):
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'words': [
                {
                    "text": 'told',
                    "value": 64
                },
                {
                    "text": "hi", 
                    "value": 1
                }
            ]
      }

