在测试服务器上进入chat 的python 环境中

1,编写story
2,编写 domain.yaml 文件
3，运行story   python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
4，测试 python -m rasa_core.run -d models/dialogue

存在的bug 1,不能重复运行一个对话

