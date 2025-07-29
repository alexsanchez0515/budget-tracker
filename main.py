from tracker import BudgetTracker
from util import Utilities


def main():
    my_tracker = BudgetTracker("Alex")

    my_tracker.add_transaction("income", "Test1", "Test1", 528.37)
    my_tracker.add_transaction("expense", "Test2", "Test2", 180.81)
    my_tracker.add_transaction("income", "Test3", "Test3", 344.45)

    my_tracker.edit_transaction()


if __name__ == "__main__":
    main()
