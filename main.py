from tracker import BudgetTracker
from util import Utilities


def main():
    my_tracker = BudgetTracker("Alex")

    my_tracker.add_transaction("income", "Test", "Test", 500.00)
    my_tracker.add_transaction("income", "Test", "Test", 500.00)
    my_tracker.add_transaction("income", "Test", "Test", 500.00)

    my_tracker.view_transactions()
    my_tracker.delete_transaction()
    my_tracker.view_transactions()


if __name__ == "__main__":
    main()
