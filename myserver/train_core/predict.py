import asyncio
import logging
from typing import Text

import rasa.train
from rasa.core.agent import Agent

logger = logging.getLogger(__name__)

model_path = "/usr/local/python3/rasa-tutorial/myserver/models/core-20190905-144528.tar.gz"

agent = Agent.load(model_path)
async def parse(text: Text, model_path: Text):



    response = await agent.handle_text(text,sender_id="123")

    logger.info("Text: '{}'".format(text))
    logger.info("Response:")
    logger.info(response)

    return response


if __name__ == "__main__":
    # train_core()
    rasa.utils.io.configure_colored_logging(loglevel="INFO")

    loop = asyncio.get_event_loop()

    text = "/greet"
    text2 = "/ask_website"
    text3 = "/thank"


    loop.run_until_complete(parse(text, model_path))

    loop.run_until_complete(parse(text2, model_path))
    loop.run_until_complete(parse(text3, model_path))


# 使用同一个 agent 就可以聊下去了。





