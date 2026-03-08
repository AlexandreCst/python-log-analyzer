"""Module to shape the statitics apply on a log file"""

import json

from pathlib import Path
from log_analyzer_package.analyzer import Analyzer

class Reporter:

    def __init__(self, analyzer: Analyzer) -> None:
        """Initilisation of class attributes"""
        self.analyzer = analyzer # Analyzer instance

    
    # Module method
    def print_report(self):
        """Display visual statistics in consol"""
        
        print("LOG FILE STATISTICS".center(80, "="))
        print(self._build_report()) # Display log file statistics
        print("END".center(80, "="))

    def save_report(self, path="report", format="txt"):
        """Method to savec the report in a text file or in a JSON"""
        path = Path(f"{path}.{format}")
        if format.lower().strip() == "txt": # Create a text file
            with path.open(mode="w") as file_txt:
                file_txt.write(self._build_report())
        elif format.lower().strip() == "json":
            with path.open(mode="w") as file_json: # creat a JSON file
                json.dump(self._build_json_report(), file_json, indent=2)

    # Private method
    def _build_report(self) -> str:
        """Private method to build a string with stats on file log"""
    
        # Get statistic from Analyzer
        numb_requests = self.analyzer.requests_number()
        date_range = self.analyzer.date_range()
        top_ip = self.analyzer.top_ip(n=5)
        counter_status = self.analyzer.counter_status()
        top_endpoint = self.analyzer.top_endpoint(n=3)
        traffic = self.analyzer.traffic_by_hour()
        server_load = self.analyzer.server_load()
        top_agent = self.analyzer.top_agent()
        ip_errors = self.analyzer.errors_ip()

        # Get start and end date of log plus duration
        start = date_range.get("start", "__UNKNOWN__")
        end = date_range.get("end", "__UNKNOWN__")
        duration = date_range.get("duration", "__UNKNOWN__")

        # Add the whole statistics in report list
        report = []
        report.append(f"Number of requests in log file: {numb_requests}")
        report.append(f"\nFirst log date: {start}")
        report.append(f"Last log date: {end}")
        report.append(f"Date log range: {duration}")

        report.append("\nIPs top 5:") # Add top IPs to report
        for ip, _ in top_ip:
            report.append(f"\t- {ip}")
        
        report.append("\nStatus code appearance in the log file:") # Add number appearance in report for each status code
        for status in counter_status:
            code, count = status
            report.append(f"\t- {code} status code -> {count}")

        report.append("\nEndpoint top 3:") # Add top 3 endpoints in log file to report
        for endpoint, _ in top_endpoint:
            report.append(f"\t- {endpoint}")

        report.append(f"\nServer traffic by hour:") # Add server traffic by hour to report
        for t in traffic:
            hour, count = t
            report.append(f"\t- {hour} -> {count} requests")

        report.append(f"\nServer load: {server_load}") # Add server load to report

        report.append(f"\nUser-agent top 3:") # Add top user-agent to report
        for agent in top_agent:
            user_agent, _ = agent
            report.append(f"\t- {user_agent}")

        report.append(f"\nErrors by IPs:") # Add the count of errors for each IPs to report
        for error in ip_errors:
            ip_code, count = error
            ip, code = ip_code
            report.append(f"\t- {count} {code} errors status for IP {ip}")

        return "\n".join(report) # Return a single string separate by underligne
    
    def _build_json_report(self) -> dict:
        """Construct a dict with statistics on log file"""

        # Get the statistics
        numb_requests = self.analyzer.requests_number()
        date_range = self.analyzer.date_range()
        top_ip = self.analyzer.top_ip(n=5)
        counter_status = self.analyzer.counter_status()
        top_endpoint = self.analyzer.top_endpoint(n=3)
        traffic = self.analyzer.traffic_by_hour()
        server_load = self.analyzer.server_load()
        top_agent = self.analyzer.top_agent()
        ip_errors = self.analyzer.errors_ip()

        start = date_range.get("start", "__UNKNOWN__").strftime("%d/%b/%Y:%H:%M:%S %z") # Conversion because datetime isn't a basic type
        end = date_range.get("end", "__UNKNOWN__").strftime("%d/%b/%Y:%H:%M:%S %z") # Conversion because datetime isn't a basic type
        duration = str(date_range.get("duration", "__UNKNOWN__")) # Conversion because timedelta isn't a basic type

        # Construct the statistics dict
        report = {}

        report["first_log"] = start # First log in the file
        report["last_log"] = end # Last log in the file
        report["date_range"] = duration # Date log range in the file
        report["requests_volume"] = numb_requests # Request volume in the file
        report["server_load"] = server_load # Server load (request size sum)
        report["status_counter"] = counter_status # Counter for each status code
        report["ip_errors"] = ip_errors # Counter for each IP by status code
        report["traffic"] = traffic # Server traffic by hour
        report["top_ip"] = top_ip # Top IP request in the file
        report["top_endpoint"] = top_endpoint # Top endpoint request in the file
        report["top_agent"] = top_agent # Top user-agent request in the file

        return report # Dict of statistics about the log file





    
        

        




