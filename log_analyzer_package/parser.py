"""Parser module."""

import re

from pathlib import Path


class Parser():
    """Definition of class to parse a log file."""

    def __init__(self, path) -> None:
        """Class attributes initialization."""
        self.path = path

    def parser(self) -> list[dict[str, str]]:
        """Parse log file ()"""
        regex = r'''^                                                      # Start of string
            (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s                   # IP adress
            (?P<id>\S+)\s                                                  # id
            (?P<username>\S+)\s                                            # Username
            (?P<date>\[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s[+-]\d{4}\])\s # Date & timezone
            (?P<req>"[^"]+")\s                                             # Request
            (?P<status>\d{3})\s                                            # Status code
            (?P<size>\d+)\s                                                # Size
            (?P<referer>"[^"]+")\s                                         # Referer
            (?P<agent>"[^"]+")\s                                           # User agent
            (?P<dash>"-")                                                  # Dash
            $                                                              # End of string
            '''
        
        path = Path(self.path)

        with path.open(mode='r') as log_file:
            logs = []
            for line in log_file:
                item = {}
                log = re.search(regex, line, re.VERBOSE)
                if log:
                    item["ip"] = log.group("ip")
                    item["id"] = log.group("id")
                    item["username"] = log.group("username")
                    item["date"] = log.group("date")
                    item["request"] = log.group("req")
                    item["status"] = log.group("status")
                    item["size"] = log.group("size")
                    item["referer"] = log.group("referer")
                    item["agent"] = log.group("agent")
                    logs.append(item)
            return logs

