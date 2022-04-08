from flask_restful import Api, Resource
from flask import Flask,request
import json

app = Flask(__name__)
api = Api(app)


class UserView(Resource):
    """
    通过继承 Resource 来实现调用 GET/POST 等动作方法
    """

    def get(self):
        """
        GET 请求
        :return:
        """

        code = request.form.get("code")

        if code == '+':
            num1 = request.form.get("num1")
            num2 = request.form.get("num2")
            datas = int(num1) + int(num2)
            return {'code': 200, 'msg': 'success', 'answer': datas}

        if code == '-':
            num1 = request.form.get("num1")
            num2 = request.form.get("num2")
            datas = int(num1) - int(num2)
            return {'code': 200, 'msg': 'success', 'answer': datas}

        if code == '*':
            num1 = request.form.get("num1")
            num2 = request.form.get("num2")
            datas = int(num1) * int(num2)
            return {'code': 200, 'msg': 'success', 'answer': datas}

        if code == '/':
            num1 = request.form.get("num1")
            num2 = request.form.get("num2")
            datas = int(num1) / int(num2)
            return {'code': 200, 'msg': 'success', 'answer': datas}

        else:
            return{"error":"0"}


api.add_resource(UserView, '/')

app.run(host="0.0.0.0", port=80)
