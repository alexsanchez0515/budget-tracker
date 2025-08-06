from datetime import datetime
import random


class Utilities:

    def add(self, x: float, y: float):
        return x + y

    def sub(self, x: float, y: float):
        return x - y

    def format_date(date):
        return datetime.strptime(date, "%m/%d/%Y")

    def get_date(self):
        return datetime.now()

    def random_id(min, max):
        return random.randint(min, max)
