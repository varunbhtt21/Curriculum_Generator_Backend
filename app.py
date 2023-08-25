from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import openai
import os
from dotenv import load_dotenv
from prompts import ulp,udp
from SystemPrompt import systemPrompt
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

def savingToFile(fileName,fileContent):
    # Open file in write mode
    with open(fileName, "w") as file:
        file.write(fileContent)

@app.route('/lessonplanquery', methods=['POST'])
def lessonPlanQuery():
    data = request.get_json()
    userMessage = data['output']
    messages[0]["content"] = systemPrompt   # ulp

    userMessage += "\n" + "Before giving the final output, ask any clarification question in pointers that you might need to improve the quality of the output."
    messages.append(
        {"role": "user", "content": userMessage},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", messages=messages
    )
    gptOutputResponse = chat.choices[0].message.content
    print(gptOutputResponse)
    
    messages.append({"role": "assistant", "content": gptOutputResponse})
    savingToFile("LessonPlan.md",gptOutputResponse)
    return {
        "GPT Output": gptOutputResponse
    }, 201


@app.route('/dayplanquery', methods=['POST'])
def dayPlanQuery():
    data = request.get_json()
    userMessage = data['output']
    messages[0]["content"] =  systemPrompt   # udp

    # userMessage += "\n" + "If Required, Before giving the final output, ask any clarification question in sequence pointers that you might need to improve the quality of the output."
    messages.append(
        {"role": "user", "content": userMessage},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    gptOutputResponse = chat.choices[0].message.content
    print(gptOutputResponse)
    
    messages.append({"role": "assistant", "content": gptOutputResponse})
    savingToFile("LessonPlan.md",gptOutputResponse)
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
        messages[0]["content"] =  systemPrompt  # ulp
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

        Design the Course Plan: 

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
        savingToFile("LessonPlan.md",gptOutputResponse)
        return {
            "GPT Output": gptOutputResponse
        }, 201


api.add_resource(LessonPlan, '/lessonplan')


# Argument parser
day_plan_parser = reqparse.RequestParser()
day_plan_parser.add_argument('CourseType', type=str, required=True)
day_plan_parser.add_argument('LearningObjectives', type=str, required=True)
day_plan_parser.add_argument('CoursePlan', type=str)
day_plan_parser.add_argument('SessionDuration', type=str, required=True)
day_plan_parser.add_argument('TeachingMode', type=str, required=True)
day_plan_parser.add_argument('LearnerProfile', type=str, required=True)
day_plan_parser.add_argument('RealWorldContexts', type=str)
day_plan_parser.add_argument('CourseComplexityLevel', type=str, required=True)


class DayPlan(Resource):
    messages[0]["content"] =  systemPrompt  # udp
    def post(self):
        args = day_plan_parser.parse_args()
        course_type = args['CourseType']
        learning_objectives = args['LearningObjectives']
        course_plan = args['CoursePlan']
        session_duration = args['SessionDuration']
        teaching_mode = args['TeachingMode']
        learner_profile = args['LearnerProfile']
        real_world_contexts = args['RealWorldContexts']
        course_complexity_level = args['CourseComplexityLevel']

        # Process the data with OpenAI API.
        userMessage = '''

        Design the Lesson Plan: 

            Course Type : {course_type}
            Learning Objectives : {learning_objectives}
            Course Plan : {course_plan}
            Session Duration : {session_duration}
            Teaching Mode : {teaching_mode}
            Learner Profile : {learner_profile}
            Real World Contexts : {real_world_contexts}
            Course Complexity Level : {course_complexity_level}

        '''.format(course_type=course_type, learning_objectives=learning_objectives, course_plan=course_plan, session_duration=session_duration, teaching_mode=teaching_mode, learner_profile=learner_profile, real_world_contexts=real_world_contexts, course_complexity_level=course_complexity_level)

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "user", "content": userMessage}
            ]
        )
        gptOutputResponse = chat.choices[0].message.content
        savingToFile("dayplan.md",gptOutputResponse)
        return {
            "GPT Output": gptOutputResponse
        }, 201

api.add_resource(DayPlan, '/dayplan')



if __name__ == '__main__':
    app.run(debug=True,port=11000)
