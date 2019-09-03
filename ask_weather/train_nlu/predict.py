'''

载入模型，然后返回预测的结果

'''

import os

from rasa_nlu.model import  Interpreter

interpreter = None

tmppath = ""
# 最大语言长度

import logging

# todo 测试的临时目录
tempPath= "D:/python_workspace/rasa-my/ask_weather/models_center/intent/fb/default/model_20190903-175709/"
def get_intent_v1(text):
    path = os.getcwd()
    # 获取当前路径
    # d = path.dirname(__file__)

    # split = d.split(os.sep)



    # logging.info("current path "+ d)
    logging.info(path)

    global interpreter

    print(path)

    global tmppath

    if interpreter is None:

        # 获取最新的模型
        # todo fix tempPath
        # listdir = os.listdir(tempPath)
        #
        # for var_path in listdir:
        #     print(var_path)
        #
        #     if var_path > tmppath:
        #         tmppath = var_path
        #
        # model_path = path + "/models_center/intent/paypal/default/" + tmppath

        print(tempPath)
        interpreter = Interpreter.load(tempPath)

    # 使用加载的interpreter处理文本

    parse = interpreter.parse(text)

    parse["version"] = tmppath

    return parse


v_ = get_intent_v1("你好")

print(v_)

