from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity  import DataIngestionConfig
# src/mlProject/config/configuration.py

from pathlib import Path

# ======= MUTLAK YOLU BURADA TANIMLA =======
CONFIG_FILE_PATH = Path(r"C:/Users/dunlu/End-to-end-Machine-Learning-Project-with-MLflow/config/config.yaml")
PARAMS_FILE_PATH = Path(r"C:/Users/dunlu/End-to-end-Machine-Learning-Project-with-MLflow/params.yaml")
SCHEMA_FILE_PATH = Path(r"C:/Users/dunlu/End-to-end-Machine-Learning-Project-with-MLflow/schema.yaml")

from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity  import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
