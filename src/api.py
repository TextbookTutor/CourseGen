import os
import tqdm

from flask import Flask, request
from flask_restx import Resource, Api

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from parse import parse_outlines
from gencourse import generate_problems
from models import ProblemSet

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

        outlines = parse_outlines("temp.pdf")

        print("Parsed outlines")

        course = {}

        course["course_title"] = uploaded_file.filename.split(".")[0]
        course["chapters"] = []

        num_sections = sum(len(chapter_sections) for _, chapter_sections in outlines) + len(outlines)

        outlines = tqdm.tqdm(outlines, total=num_sections, desc="Generating course")
        
        for chapter_title, chapter_sections in outlines:
            chapter = {}
            chapter["chapter_title"] = chapter_title
            chapter["sections"] = []

            for section_title, section_body in chapter_sections:
                section = {}
                section["section_title"] = section_title

                problemset: ProblemSet = generate_problems(section_body, 6, 2)
                problemset = problemset.model_dump()

                section["mcqs"] = problemset["mcqs"]
                section["frqs"] = problemset["frqs"]

                chapter["sections"].append(section)

                outlines.update(1)

            outlines.set_postfix_str(chapter_title)

            course["chapters"].append(chapter)

        outlines.close()

        client.get_database("TextbookTutor").get_collection("Courses").insert_one(course)

        return {"message": "Course generated successfully", "course": course}, 200

if __name__ == '__main__':
    client = MongoClient(os.getenv("MONGODB_URI"), server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    app.run(debug=True)
