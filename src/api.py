from flask import Flask, request
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)

@api.route('/gencourse')
class GenCourse(Resource):
    def post(self):
        if 'file' not in request.files:
            return {"message": "No file part in the request"}, 400

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return {"message": "No selected file"}, 400

        uploaded_file.save("temp.pdf")



        return {"message": f"File '{uploaded_file.filename}' received successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)
