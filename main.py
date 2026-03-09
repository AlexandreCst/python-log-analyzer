from log_analyzer_package import Parser, Analyzer, Reporter

def main():
    """Orchestrate the pipeline"""

    path = "docs/apache.log" # Log file path to analyze

    log_file_parsed = Parser(path=path).parser() # Parse log file
    log_analyzer = Analyzer(log_file_parsed) # Analyze on parse log file

    report = Reporter(log_analyzer) # Shape the statistics apply on log file
    
    report.print_report() # Get statistics in terminal
    report.save_report("docs/report", "txt") # Save report in text file
    report.save_report("docs/report", "json") # Save report in JSON file


if __name__ == "__main__":
    main()
