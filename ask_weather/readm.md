# 添加了询问天气的对话

并不只有这一种定义方法，在Rasa Core中有三种类型的actions，分别为

default actions ，系统默认提供的action
utter actions，以 utter_作为开头, 该action只能用于给用户返回信息
custom actions ，自定义的action，该action可执行任何的操作



# 修改了路径所以训练变成下面的方式了：
这个在ask_weather的路径下执行 
训练core
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue -c policy_config.yml

训练nlu
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose


