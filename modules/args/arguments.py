from argparse import ArgumentParser
import json


class Arguments:
    JOB_TYPE_CUSTOM_NOTE = 'custom_note'
    JOB_TYPE_MAILING = 'mailing'

    def __init__(self):
        self._argparser = ArgumentParser()
        self._params = None

        self.add_arguments()
        self.process_arguments()

    def process_arguments(self):
        self._params = self._argparser.parse_args()

    def add_arguments(self):
        self._argparser.add_argument('-e', dest='environment', type=str,
                                     default='production',
                                     help='The environment value used for configuration')
        self._argparser.add_argument('-a', dest='action', type=str,
                                     default='pull', options=,
                                     help='Set the limit of the cache warming query')
        self._argparser.add_argument('-o', dest='offset', type=int,
                                     default=0,
                                     help='Set the offset of the cache warming query')
        self._argparser.add_argument('-t', dest='is_test', type=bool,
                                     default=False,
                                     help='Rotate the card image')

    def get_value(self, key: str):
        if key in self._params.__dict__:
            return self._params.__dict__[key]
        elif key in self.__dict__:
            return self.__dict__[key]
        else:
            return None

    def set_value(self, key: str, value):
        self.__dict__[key] = value

    def to_logging_str(self):
        return json.dumps(self._params.__dict__, indent=2)
