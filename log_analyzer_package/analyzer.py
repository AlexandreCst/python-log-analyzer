"""This module provide analysis tools to apply on a parse file."""

from datetime import datetime, timedelta

class Analyzer:

    def __init__(self, logs: list[dict[str, str]]) -> None:
        """Initilisation of class attributes"""
        self.logs = logs

    def requests_number(self) -> int:
        """Method to return the numbers of requests"""
        return len(self.logs)
    
    def date_range(self) -> dict[str, datetime | timedelta]:
        """Method to return the date range of the log file"""
        format = "%d/%b/%Y:%H:%M:%S %z" # Define date format
        dates = [log.get("date", "").strip('[]') for log in self.logs] # Put the dates without the []
        dates_formatted = [datetime.strptime(date, format) for date in dates] # String dates to datetime type
        return {
            "start": min(dates_formatted),
            "end": max(dates_formatted),
            "duration": max(dates_formatted) - min(dates_formatted),
        }
    