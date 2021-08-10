from flask_restful import Api, Resource, request

class ApiHandler(Resource):
  def get(self):
    search_term = request.args.get("query")
    ## TODO: return err if query is invalid twitter handle
    ## TODO: use search_term to return proper array of words
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

