import argparse
import asyncio
import logging
from typing import Text

import rasa.train
from rasa.core.agent import Agent

logger = logging.getLogger(__name__)


async def parse(text: Text, model_path: Text):
    agent = Agent.load(model_path)

    response = await agent.handle_text(text)

    logger.info("Text: '{}'".format(text))
    logger.info("Response:")
    logger.info(response)

    return response


if __name__ == "__main__":
    # train_core()
    rasa.utils.io.configure_colored_logging(loglevel="INFO")

    loop = asyncio.get_event_loop()


    text = "my test"
    model_path = ""
    loop.run_until_complete(parse(text, model_path))
