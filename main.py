from tracker import BudgetTracker
from util import Utilities


def main():
    my_tracker = BudgetTracker("Alex")
    my_tracker.add_transaction("income", "Test", "Test", 500.00, "01-01-1970")
    my_tracker.view_transactions()


if __name__ == "__main__":
    main()
