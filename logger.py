from .config import GRWConfig
from datetime import datetime

class GRWLogger:
    def __init__(self, logfile=GRWConfig.LOG_FILE):
        self.logfile = logfile

    def log_error(self, message):
        with open(self.logfile, 'a') as f:
            f.write(f"{datetime.now().strptime("%Y/%m/%d %H:%M:%S")}: {message}\n")