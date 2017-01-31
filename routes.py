import requests
from flask import Flask, request, jsonify
from app import app

@app.route("/", methods = ['Get','Post'])
def user_handler():
    print()
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(ip)
    print(type(ip))
    print("printed ip")
    url = 'http://ip-api.com/json/'
    url += ip
    print(url)
    req = requests.get(url)

    data = req.text
    print(data)

    return data