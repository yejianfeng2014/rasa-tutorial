from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
import os


def train(data_path):
    # 示例数据

    getcwd = os.getcwd()

    print(getcwd)

    training_data = load_data(data_path)
    # pipeline配置指定了配置文件地址
    trainer = Trainer(config.load("./../nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('./../models_center/intent/fb')

    print(model_directory)


if __name__ == '__main__':
    path = "./../data/nlu.md"

    getcwd = os.getcwd()
    print(getcwd)

    train(path)
