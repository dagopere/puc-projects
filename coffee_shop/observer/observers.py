import datetime

class ConsoleNotifier:
    def update(self, message: str):
        print(f"[NOTIFICAÇÃO] {message}")

class LoggerNotifier:
    def __init__(self, logfile='order_log.txt'):
        self.logfile = logfile

    def update(self, message: str):
        with open(self.logfile, 'a') as f:
            f.write(f"{datetime.datetime.now().isoformat()} - {message}\n")
