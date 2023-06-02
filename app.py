from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import openai
import os
from dotenv import load_dotenv
from prompts import lessonPlan, weekPlan, dayPlan, systemPrompt,sp,xy,gf,ulp
import markdown
from flask_cors import CORS   
import requests

load_dotenv()

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)
api = Api(app)

messages = [
        {"role": "system", "content": ulp},
    ]


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/lessonplanquery', methods=['POST'])
def get_string():
    data = request.get_json()
    userMessage = data['output']
    messages[0]["content"] = ulp
    messages.append(
        {"role": "user", "content": userMessage},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    gptOutputResponse = chat.choices[0].message.content
    print(gptOutputResponse)
    
    messages.append({"role": "assistant", "content": gptOutputResponse})
    return {
        "GPT Output": gptOutputResponse
    }, 201


# Argument parser
lesson_parser = reqparse.RequestParser()
lesson_parser.add_argument('CourseSubject', type=str, required=True)
lesson_parser.add_argument('CourseDuration', type=str, required=True)
lesson_parser.add_argument('CourseType', type=str, required=True)
lesson_parser.add_argument('SpecificCourseGoals', type=str, required=True)
lesson_parser.add_argument('TargetAudience', type=str, required=True)
lesson_parser.add_argument('CurrentSkillLevel', type=str, required=True)
lesson_parser.add_argument('PriorKnowledge', type=str, required=True)


class LessonPlan(Resource):
    def post(self):
        messages[0]["content"] = ulp
        args = lesson_parser.parse_args()
        course_subject = args['CourseSubject']
        course_duration = args['CourseDuration']
        course_type = args['CourseType']
        specific_course_goals = args['SpecificCourseGoals']
        target_audience = args['TargetAudience']
        current_skill_level = args['CurrentSkillLevel']
        prior_knowledge = args['PriorKnowledge']

        # Here is where you can process the data with OpenAI API.
        userMessage = '''
            Course Subject : {course_subject}
            Course Duration : {course_duration}
            Course Type : {course_type}
            Specific Course Goals : {specific_course_goals}
            Target Audience : {target_audience}
            Current Skill Level : {current_skill_level}
            Prior Knowledge : {prior_knowledge}

            Before giving the final output, ask any clarification question in pointers that you might need to improve the quality of the output.
        '''.format(course_subject=course_subject, course_duration=course_duration, course_type=course_type, specific_course_goals=specific_course_goals, target_audience=target_audience, current_skill_level=current_skill_level, prior_knowledge=prior_knowledge)
        
        messages[0]["content"] = ulp
        messages.append(
            {"role": "user", "content": userMessage},
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        gptOutputResponse = chat.choices[0].message.content
        print(gptOutputResponse)
       
        messages.append({"role": "assistant", "content": gptOutputResponse})
        return {
            "GPT Output": gptOutputResponse
        }, 201


api.add_resource(LessonPlan, '/lessonplan')


# Argument parser
lesson_plan_parser = reqparse.RequestParser()
lesson_plan_parser.add_argument('1', type=str, required=True, help="1 cannot be blank!")
lesson_plan_parser.add_argument('2', type=str, required=True, help="2 cannot be blank!")
lesson_plan_parser.add_argument('3', type=str, required=True, help="3 cannot be blank!")

class LessonPlanQuery(Resource):
    def post(self):
        args = lesson_plan_parser.parse_args()
        param_1 = args['1']
        param_2 = args['2']
        param_3 = args['3']
        
        # Add your logic here
        userMessage = '''
            1 : {param_1}
            2 : {param_2}
            3 : {param_3}

            Before giving the final output, ask any clarification question in pointers that you might need to improve the quality of the output.
        '''.format(param_1=param_1, param_2=param_2, param_3=param_3)

        messages[0]["content"] = ulp
        messages.append(
            {"role": "user", "content": userMessage},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        gptOutputResponse = chat.choices[0].message.content
        print(gptOutputResponse)
       
        messages.append({"role": "assistant", "content": gptOutputResponse})
        return {
            "GPT Output": gptOutputResponse
        }, 201

api.add_resource(LessonPlanQuery, '/lessonplanquer')

if __name__ == '__main__':
    app.run(debug=True,port=11000)
