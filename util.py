from datetime import datetime


class Utilities:

    def add(self, x: float, y: float):
        return x + y

    def sub(self, x: float, y: float):
        return x - y

    def format_date(self, date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def get_date(self):
        return datetime.now()
