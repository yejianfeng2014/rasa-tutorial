

# 服务器使用的版本是 rasa 版本 1.2.7  和以前的命令不一致 需要注意下
测试环境的存储路径： /usr/local/python3/rasa-tutorial

可以直接进入mysever 目录直接执行 ，
rasa train 训练模型，生成的是一个压缩包

rasa shell 启动测试环境命令行，然后就可以进行简单的测试


# 如果自己定义action 需要自己手动启动起来 
rasa run actions --actions actions&


# 实时测试效果 ，启动后可以看到所有的story 的图形 ，非常直观，最终还可以修改流程图
rasa interactive \
  -m models/20190515-135859.tar.gz \
  --endpoints endpoints.yml
  
  
  


This example contains some training data and the main files needed to build an assistant on your local machine. The concertbot consists of the following files:

data/stories.md contains training stories for the Core model
actions.py contains some custom actions
config.yml contains the model configuration
domain.yml contains the domain of the assistant
endpoints.yml contains the webhook configuration for the custom actions
How to use this example?
To train a model, run
# 训练模型 
rasa train core -d domain.yml -s data/stories.md --out models -c config.yml
To create new training data using interactive learning, execute

rasa interactive core -d domain.yml -m models -c config.yml --stories data
To visualize your story data, run

# 这个会把对话的流程图生成一个流程图，然后可以直接访问 
rasa visualize
To run a Rasa server, execute

rasa run actions&
rasa run -m models --endpoints endpoints.yml
To chat with your bot on the command line, run

rasa run actions&
rasa shell -m models
For more information about the individual commands, please check out our documentation.

Encountered any issues?
Let us know about it by posting on Rasa Community Forum!  


# todo 在线上需要创建新的聊天环境 


从数据库导出的数据然后生成nlu 的数据，训练时候发现有一个意图的存在，发出了警告，需要处理一下。

