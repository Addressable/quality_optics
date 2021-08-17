import os

from modules.args.arguments import Arguments
from modules.config.config import Config
from modules.aws.s3_utils import S3Utils


class Main:
    def __init__(self):
        self._arguments = Arguments()
        self._config = Config(os.path.dirname(os.path.abspath(__file__)), self._arguments.get_value('environment'))
        self._s3_utils = S3Utils(self._config.get('aws_destination_bucket'))

    def run(self):



if __name__ == '__main__':
    main = Main()
    main.run()
