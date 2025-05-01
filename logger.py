import datetime

from config import GRWConfig


class GRWLogger:
    def __init__(self, logfile=GRWConfig.LOG_FILE):
        self.logfile = logfile

    def _log(self, status, message):
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        logmessage = f"{timestamp} {status}: {message}"

        if GRWConfig.DEBUG or GRWConfig.LOG_LEVEL == "DEBUG":
            print(logmessage)
        with open(self.logfile, "a") as f:
            f.write(logmessage + "\n")

    def log_info(self, message):
        self._log("INFO", message)

    def log_error(self, message):
        self._log("ERROR", message)

    def log_warning(self, message):
        self._log("WARNING", message)

    def log_debug(self, message):
        if GRWConfig.DEBUG or GRWConfig.LOG_LEVEL == "DEBUG":
            self._log("DEBUG", message)

    def log_critical(self, message):
        self._log("CRITICAL", message)

    def log_exception(self, message):
        self._log("EXCEPTION", message)
