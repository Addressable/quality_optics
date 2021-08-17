import os
from datetime import datetime

from configparser import ConfigParser


class Config:
    ANALYTICS_S3_KEY_TEMPLATE = "{environment}/{component_name}/{year}/{month}/{day}/{file}"

    def __init__(self, root_path: str, environment: str = 'production'):
        self._config_parser = ConfigParser()
        self._root_path = root_path
        self._environment = environment
        config_file = f"{self._root_path}/environments/{self._environment}.ini"

        if '~' in config_file:
            config_file = os.path.expanduser(config_file)
        if os.path.exists(config_file):
            self._config_parser.read(config_file)
        else:
            raise FileNotFoundError(f"Could not find file: {config_file}")

        self.check_environment(self._environment)

    def get(self, name):
        try:
            return self._config_parser.get(self._environment, name)
        except KeyError:
            return None
        except Exception:
            return None

    def check_environment(self, environment):
        if environment not in self._config_parser.sections():
            raise AttributeError(f"Could not find section: {self._environment}")

    def environment(self):
        return self._environment

    def data_path(self):
        return f"{self._root_path}/data"

    def get_analytics_s3_key(self, component_name):
        current_time = datetime.now()

        return Config.ANALYTICS_S3_KEY_TEMPLATE.format_map({
            'environment': self.environment(),
            'component_name': component_name,
            'year': current_time.year,
            'month': '%02d' % current_time.month,
            'day': '%02d' % current_time.day,
            'file': f"{current_time.hour}_{current_time.minute}_{current_time.second}.json"
        })