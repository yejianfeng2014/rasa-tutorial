import argparse
import asyncio
import logging
from typing import Text

import os
import rasa.utils.io
import rasa.train
from examples.restaurantbot.policy import RestaurantPolicy
from rasa.core.agent import Agent
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.policies.mapping_policy import MappingPolicy

logger = logging.getLogger(__name__)


# async def parse(text: Text, model_path: Text):
#     agent = Agent.load(model_path)
#
#     response = await agent.handle_text(text)
#
#     logger.info("Text: '{}'".format(text))
#     logger.info("Response:")
#     logger.info(response)
#
#     return response


async def train_core(
    domain_file: Text = "domain.yml",
    model_directory: Text = "models",
    model_name: Text = "current",
    training_data_file: Text = "data/stories.md",
):
    agent = Agent(
        domain_file,
        policies=[
            MemoizationPolicy(max_history=3),
            MappingPolicy(),
            RestaurantPolicy(batch_size=100, epochs=100, validation_split=0.2),
        ],
    )

    training_data = await  agent.load_data(training_data_file, augmentation_factor=10)
    agent.train(training_data)

    # Attention: agent.persist stores the model and all meta data into a folder.
    # The folder itself is not zipped. 未打包的的模型文件
    model_path = os.path.join(model_directory, model_name, "core")
    agent.persist(model_path)

    logger.info("Model trained. Stored in '{}'.".format(model_path))

    return model_path




if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(train_core())

