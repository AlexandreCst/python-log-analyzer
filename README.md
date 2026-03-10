# Python log analyzer project

## Description
Python ETL like project to analyze a log file (apache log access server) and
apply some statistics like top IPs appearance, number of requests and so on. 

## Features
- Log analyzer package
- OOP architecture
- Modules like parser, analyzer, reporter and exceptions
- Custom exceptions : LogFileNotFoundError, EmptyFileError, FileWrittingError and
AnalyzerMissingError
- Statistics in analyzer : top_ip(), requests_number(), date_range(), etc.
- Report in consol and text or JSON file
- Orchestration in main.py
- Try/except to handle exceptions
- Logging in console and in file (pipeline.log)

## Installation
Clone the repository:
```bash
git https://github.com/AlexandreCst/python-log-analyzer.git
cd python-log-analyzer
```

No additional dependencies required (uses Python standard library only).

## How to Use
Run the program:
```bash
python main.py
```

- Enter the file log path to analyze in the path variable inside main.py

## Requirements
- Python 3.10 or above

## License
MIT license

## Author
Alexandre COSTE