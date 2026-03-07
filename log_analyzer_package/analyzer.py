"""This module provide analysis tools to apply on a parse file."""

import re

from datetime import datetime, timedelta
from collections import Counter

class Analyzer:

    def __init__(self, logs: list[dict[str, str]]) -> None:
        """Initilisation of class attributes"""
        self.logs = logs

    def requests_number(self) -> int:
        """Method to return the numbers of requests"""
        return len(self.logs)
    
    def date_range(self) -> dict[str, datetime | timedelta]:
        """Method to return the date range of the log file"""
        dates = self._parse_dates()
        return {
            "start": min(dates),
            "end": max(dates),
            "duration": max(dates) - min(dates),
        }
    
    def top_ip(self, n: int=10) -> list[tuple[str | None, int]]:
        """Method to obtain top n IP in the log file"""
        ip = [log.get("ip") for log in self.logs] # Extract IP of list of logs
        counter = Counter(ip) # Define an IP counter
        return counter.most_common(n) # Return the n most common IP
    
    def counter_status(self) -> list[tuple[str | None, int]]:
        """Method to count status code distribution"""
        status = [log.get("status") for log in self.logs] # Extract status code
        counter = Counter(status) # Define a status code counter
        return counter.most_common() # Return the counter
    
    def top_endpoint(self, n: int=10) -> list[tuple[str | None, int]]:
        """Method to obtain top n endpoints in the log file"""
        regex = r'/\S+' # Define regex to match endpoint in request
        endpoints = []
        for log in self.logs:
            endpoint = re.search(regex, log.get("req", ""))
            if endpoint:
                endpoints.append(endpoint.group())

        counter = Counter(endpoints) # Define endpoints counter
        return counter.most_common(n) # Return top n endpoints
    
    def traffic_by_hour(self) -> list[tuple]:
        """Method to get traffic by hour"""
        hours = [date.hour for date in self._parse_dates()] # String dates to datetime type
        counter = Counter(hours) # Traffic counter by hour
        return counter.most_common()
    
    def server_load(self) -> int:
        """Method to get the server load"""
        size = [int(log.get("size", 0)) for log in self.logs] # Get log size
        return sum(size)
    
    def top_agent(self, n: int=3) -> list[tuple[str | None, int]]:
        """Method to get the top n user_agent"""
        user_agent = [log.get("agent") for log in self.logs] # Get user agent
        counter = Counter(user_agent) # user agent counter
        return counter.most_common(n)



    def _parse_dates(self):
        format = format = "%d/%b/%Y:%H:%M:%S %z" # Define date format
        dates = [log.get("date", "").strip('[]') for log in self.logs] # Get the dates without the []
        dates_formatted = [datetime.strptime(date, format) for date in dates] # String dates to datetime type
        return dates_formatted