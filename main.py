from tracker import BudgetTracker
from util import Utilities


def main():
    my_tracker = BudgetTracker("Alex")
    my_tracker.add_transaction("income", "Test", "Test", 500.00)
    my_tracker.add_transaction(
        "expense", "Test2", "Test2", 237.00, "25-07-2025 10:00:00")
    my_tracker.view_transactions()
    my_tracker.get_balance()


if __name__ == "__main__":
    main()
