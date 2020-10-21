"""
A library for converting SQL into shorthand that takes up less space.
"""

import pathlib

from lib.config.parse_config import parse_config
from lib.compress.compress_sql import compress_sql
from lib.expand.expand_sql import expand_sql


class __SQLHandler(object):
    def __init__(self, config_filename: str) -> None:
        self.config = self.__parse_config(config_filename=config_filename)

    @staticmethod
    def __parse_config(config_filename: str) -> dict:
        return parse_config(pathlib.Path(config_filename).read_text())


class SQLCompressor(__SQLHandler):
    """
    Used to compress SQL strings down to specialized shorthand.
    """
    def __init__(self, config_filename: str):
        super().__init__(config_filename)

    def __parse_sql(self, sql_string: str) -> str:
        return compress_sql(self.config, sql_string)

    def compress(self, sql_string: str) -> str:
        """

        :param sql_string:
        :return:
        """
        return self.__parse_sql(sql_string)


class SQLExpander(__SQLHandler):
    """
    Used to generate SQL from shorthand strings.
    """
    def __init__(self, config_filename: str):
        super().__init__(config_filename)

    def __parse_blob(self, blob_string: str) -> str:
        return expand_sql(self.config, blob_string)

    def expand(self, blob_string: str) -> str:
        """

        :param blob_string:
        :return:
        """
        return self.__parse_blob(blob_string)
