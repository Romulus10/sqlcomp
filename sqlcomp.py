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

    Examples:
        >>> from sqlcomp import SQLCompressor
        >>> sql = "INSERT INTO `Test` (`table`) VALUES ('value');"
        >>> config = './example.conf'
        >>> SQLCompressor(config).compress(sql)
        'I T t v'
    """
    def __init__(self, config_filename: str):
        super().__init__(config_filename)

    def __parse_sql(self, sql_string: str) -> str:
        return compress_sql(self.config, sql_string)

    def compress(self, sql_string: str) -> str:
        """
        Compress given SQL down to a shortened form.

        :param sql_string: A string of SQL to compress down to shorthand.
        :return: A shorthand, reduced SQL blob.
        """
        return self.__parse_sql(sql_string)


class SQLExpander(__SQLHandler):
    """
    Used to generate SQL from shorthand strings.

    Examples:
        >>> from sqlcomp import SQLExpander
        >>> sql = 'I T t v'
        >>> config = './example.conf'
        >>> SQLExpander(config).expand(sql)
        "INSERT INTO `Test` (`table`) VALUES ('value');"
    """
    def __init__(self, config_filename: str):
        super().__init__(config_filename)

    def __parse_blob(self, blob_string: str) -> str:
        return expand_sql(self.config, blob_string)

    def expand(self, blob_string: str) -> str:
        """
        Expand a shorthand blob string out to valid SQL.

        :param blob_string: A shorthand blob that needs to be expanded out to SQL.
        :return: A valid SQL string.
        """
        return self.__parse_blob(blob_string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
