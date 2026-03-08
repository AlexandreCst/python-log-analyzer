"""Module to shape the statitics apply on a log file"""

from log_analyzer_package.analyzer import Analyzer
class Reporter:

    def __init__(self, analyzer: Analyzer) -> None:
        """Initilisation of class attributes"""
        self.analyzer = analyzer # Analyzer instance

    