from src.utils.all_utils import read_yaml, create_directory
from src.utils.models import get_VGG_16_model
import argparse
import pandas as pd
import os
import shutil
from tqdm import tqdm
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def prepare_base_model(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]

    base_model_dir = artifacts["BASE_MODEL_DIR"]
    base_model_name = artifacts["BASE_MODEL_NAME"]

    base_model_dir_path = os.path.join(artifacts_dir, base_model_dir)

    create_directory([base_model_dir_path])

    base_model_path = os.path.join(base_model_dir_path, base_model_name)

    model = get_VGG_16_model(input_shape=params["IMAGE_SIZE"], model_path=base_model_path)


    


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>> stage two started")
        prepare_base_model(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("stage two completed! base model is created >>>>>")
    except Exception as e:
        logging.exception(e)
        raise e