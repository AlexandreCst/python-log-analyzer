"""Module to shape the statitics apply on a log file"""

from log_analyzer_package.analyzer import Analyzer

class Reporter:

    def __init__(self, analyzer: Analyzer) -> None:
        """Initilisation of class attributes"""
        self.analyzer = analyzer # Analyzer instance

    
    # Module method
    def print_report(self):
        """Display visual statistics in consol"""
        
        print("LOG FILE STATISTICS".center(80, "="))
        print(self._build_report())
        print("END".center(80, "="))
        
    

    # Private method
    def _build_report(self) -> str:
        """Private method to build a string with stats on file log"""
    
        numb_requests = self.analyzer.requests_number()
        date_range = self.analyzer.date_range()
        top_ip = self.analyzer.top_ip(n=5)
        counter_status = self.analyzer.counter_status()
        top_endpoint = self.analyzer.top_endpoint(n=3)
        traffic = self.analyzer.traffic_by_hour()
        server_load = self.analyzer.server_load()
        top_agent = self.analyzer.top_agent()
        ip_errors = self.analyzer.errors_ip()

        start = date_range.get("start", "__UNKNOWN__")
        end = date_range.get("end", "__UNKNOWN__")
        duration = date_range.get("duration", "__UNKNOWN__")

        report = []
        report.append(f"Number of requests in log file: {numb_requests}")
        report.append(f"\nFirst log date: {start}")
        report.append(f"Last log date: {end}")
        report.append(f"Date log range: {duration}")

        report.append("\nIPs top 5:")
        for ip, _ in top_ip:
            report.append(f"\t- {ip}")
        
        report.append("\nStatus code appearance in the log file:")
        for status in counter_status:
            code, count = status
            report.append(f"\t- {code} status code -> {count}")

        report.append("\nEndpoint top 3:")
        for endpoint, _ in top_endpoint:
            report.append(f"\t- {endpoint}")

        report.append(f"\nServer traffic by hour:")
        for t in traffic:
            hour, count = t
            report.append(f"\t- {hour} -> {count} requests")

        report.append(f"\nServer load: {server_load}")

        report.append(f"\nUser-agent top 3:")
        for agent in top_agent:
            user_agent, _ = agent
            report.append(f"\t- {user_agent}")

        report.append(f"\nErrors by IPs:")
        for error in ip_errors:
            ip_code, count = error
            ip, code = ip_code
            report.append(f"\t- {count} {code} errors status for IP {ip}")

        return "\n".join(report)

    
        

        




