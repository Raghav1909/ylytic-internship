from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


comments = []

with app.app_context():
    response =  requests.get('https://app.ylytic.com/ylytic/test').json()
    comments = response["comments"]

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
        if search_author and search_author.lower() not in comment["author"].lower():
            continue
        if at_from and comment["at"] < at_from:
            continue
        if at_to and comment["at"] > at_to:
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