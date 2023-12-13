import awsgi
from flask import Flask, request, jsonify
import requests
from datetime import datetime, date


app = Flask(__name__)


comments = []

with app.app_context():
    response =  requests.get('https://app.ylytic.com/ylytic/test').json()
    comments = response["comments"]


@app.route('/')
def index():
    return jsonify(status=200, message='OK')


def convert_date(date_str):
    converted_datetime = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    return converted_datetime

@app.route('/search', methods=['GET'])
def search_comments():
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    result = []
    for comment in comments:
        at_from_date = datetime.strptime(at_from, '%d-%m-%Y') if at_from else None
        at_to_date = datetime.strptime(at_to, '%d-%m-%Y') if at_to else None
        converted_date = convert_date(comment["at"])

        if search_author and search_author.lower() not in comment["author"].lower():
            continue
        if at_from_date and converted_date < at_from_date:
            continue
        if at_to_date and converted_date > at_to_date:
            continue
        if like_from and comment["like"] < int(like_from):
            continue
        if like_to and comment["like"] > int(like_to):
            continue
        if reply_from and comment["reply"] < int(reply_from):
            continue
        if reply_to and comment["reply"] > int(reply_to):
            continue
        if search_text and search_text.lower() not in comment["text"].lower():
            continue

        result.append(comment)

    return jsonify(result)


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


if __name__ == "__main__":
    app.run()
