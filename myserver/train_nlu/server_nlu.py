'''
启动nlu 的server 提供web 服务端，占用8081 端口
'''


import flask
from flask import Flask, render_template
import logging

from myserver.train_nlu.predict import get_intent_v1

app = Flask(__name__)


@app.route("/api/nlp/nlu/fb/msg/v1", methods=["GET", "POST"])
def predict_similar_v2():
    data = {"success": False}

    params = flask.request.json

    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
        # x = pd.DataFrame.from_dict(params, orient='index').transpose()
        # with graph.as_default():
        logging.info('/api/nlp/nlu/fb/msg/v1')
        logging.info(params)

        sentence_1 = params.get("msg", type=str).lower()

        # print('a',sentence_1)
        # print('b',sentence_2)

        # simliar = getSimliar_v2(sentence_1, sentence_2)

        result = get_intent_v1(sentence_1)

        logging.info(result)

        # print(params)

        # data["prediction"] = str(model.predict(x)[0][0])
        data["success"] = True
        data['predict'] = result

    # return a response in json format
    return flask.jsonify(data)

@app.errorhandler(404)
def internal_error(error):
    logging.info(error)
    data = {"success": False}
    return flask.jsonify(data)

@app.errorhandler(500)
def internal_error(error):
    logging.info(error)
    data = {"success": False}
    return flask.jsonify(data)


if __name__ == '__main__':
    # load_model()
    # app.run()
    # app.run(debug=False, host="0.0.0.0", port=8080)
    # 添加多线程和多进程，当前支持多个线程，1进程。
    app.run(debug=False, host="0.0.0.0", port=8081, threaded=True)

