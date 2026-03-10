import logging

from log_analyzer_package.parser import Parser
from log_analyzer_package.analyzer import Analyzer
from log_analyzer_package.reporter import Reporter

from log_analyzer_package.exceptions import LogFileNotFoundError
from log_analyzer_package.exceptions import EmptyFileError
from log_analyzer_package.exceptions import FileWrittingError
from log_analyzer_package.exceptions import AnalyzerMissingError

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
console_handler.setLevel("WARNING")

file_handler = logging.FileHandler("docs/pipeline.log", mode="a", encoding="utf-8")
file_handler.setLevel("DEBUG")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)