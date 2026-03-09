"""Module to define custom exceptions"""

class LogAnalyzerError(Exception):
    pass
    
class LogFileNotFoundError(LogAnalyzerError):
    """Exception whether file doesn't exist"""
    pass

class EmptyFileError(LogAnalyzerError):
    """Exception whether file is empty"""
    pass

class FileWrittingError(LogAnalyzerError):
    """Exception whether file cannot be writting"""
    pass

class AnalyzerMissingError(LogAnalyzerError):
    """Exception whether statistic(s) is/are missing"""
    pass