"""This module provide analysis tools to apply on a parse file."""

class Analyzer:

    def __init__(self, logs: list[dict[str, str]]) -> None:
        """Initilisation of class attributes"""
        self.logs = logs

    def requests_number(self) -> int:
        """Method to return the numbers of requests"""
        return len(self.logs)

    
        