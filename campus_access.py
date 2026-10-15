# def approve_request():, is legal only if the records current status is requested for that operation.
# def issue_card():, is legal only if the records current status is approved for that operation.
# def return_card():, is legal only if the records current status is issued for that operation.
# requested → approved → issued → returned

FAKE_RECORDS = {
    "A001": {"id": "A001", "fellow_id": "F001", "card_type": "visitor", "status": "requested", "approved_by": None},
}

def get_record(request_id):
    if request_id not in FAKE_RECORDS:
        raise ValueError(f"Unknown record ID: {request_id}")
    return FAKE_RECORDS[request_id]

def approve_request(request_id, approved_by): 
    record = get_record(request_id)

    if record["status"] != "requested": 
        raise ValueError(f"Cannot approve: status must be 'requested', but it is '{record['status']}'.") 
    if approved_by is None or approved_by.strip() == "": 
        raise ValueError("Approved_by is required")

    record["status"] = "approved"
    record["approved_by"] = approved_by.strip()

TEST CASE.

"""Engineer B tests: approve / issue / return workflow.

Run from the PROJECT ROOT (the folder that contains your .py file and tests/):
    python -m unittest discover -s tests -v

Before running:
  1. Change the import below to match YOUR file name and function names.
  2. Make your functions get records from something the tests can control
     (a fake lookup, or A's real store pointed at a temporary file).
Each test starts as a deliberate FAIL ("TODO") so nothing looks like it
passed before you have written and run it.
"""
#import approve-request
import unittest

from campusaccess import (
    approve_request,
    issue_card,
    return_card,
)

# TODO: replace "workflow" with the name of your module (file without .py)
# from workflow import approve_request, issue_card, return_card


class TestApproveRequest(unittest.TestCase):

    def setUp(self):
        # A fresh record before EVERY test, so tests cannot affect each other.
        self.record = {
            "id": "A001",
            "fellow_id": "F001",
            "card_type": "visitor",
            "status": "requested",
            "approved_by": None,
        }
        # TODO: make your functions use self.record for "A001"
        # (e.g. point your fake lookup at it).

    # ---- CASE 2 / checkpoint B2 ------------------------------------------
    def test_issue_before_approval_is_rejected_and_record_unchanged(self):
        # Arrange: take a SNAPSHOT of the record. Use copy.deepcopy(...)
        #          so it is a real copy, not the same object.
        # Act:     call issue_card("A001") inside self.assertRaises(ValueError)
        # Assert:  self.record == snapshot (nothing changed)
        self.fail("TODO: write this test")

    # ---- CASE 3 / checkpoint B3 ------------------------------------------
    def test_blank_approver_is_rejected_and_record_unchanged(self):
        # Try approving with "   " (spaces only). Also think: None, "".
        # The record must still be status "requested", approved_by None.
        self.fail("TODO: write this test")

    # ---- CASE 4 / checkpoint B4 ------------------------------------------
    def test_full_workflow_requested_to_returned(self):
        # approve with "M01" -> check status "approved" and approved_by "M01"
        # issue              -> check status "issued"
        # return             -> check status "returned"
        self.fail("TODO: write this test")

    # ---- CASE 5 / checkpoint B5 ------------------------------------------
    def test_double_return_is_rejected(self):
        # Run the full workflow, then call return_card again inside
        # assertRaises. Check the status is STILL "returned".
        self.fail("TODO: write this test")

    def test_issue_after_return_is_rejected(self):
        # Same setup as above, but try issue_card on the returned record.
        self.fail("TODO: write this test")

    def test_approve_twice_is_rejected(self):
        # After a good approval, approving again must fail and keep the
        # first approver's name unchanged.
        self.fail("TODO: write this test")


if __name__ == "__main__":
    unittest.main()

MAIN MENU

from campusaccess.create_request import (
    create_card,
)

from campusaccess.storage import (
    load_requests,
    save_requests,
)

from campusaccess.workflow import (
    approve_request,
    issue_card,
    return_card,
)

DATA_FILE = Path(__file__).resolve().parent / "data" / "cards.json"

def load_application_data():
    try:
        return load_requests(DATA_FILE)
    except FileNotFoundError:
        return {}


def save_application_data(cards):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    save_requests(cards, DATA_FILE)


def display_cards(cards):
    if not cards:
        print("cards not found.")
        return

    for field, value in cards.items():
        print(f"{field.replace('_', ' ').title()}: {value}")
    
def handle_view(cards):
    card_id = input("Enter ticket ID: ").strip().upper()
    display_ticket(get_ticket(cards, card_id))


def run_menu():
    cards = load_application_data()

    while True:
        print("1. Create cards")
        print("2. Approve request")
        print("3. Issue card")
        print("4. Return card")
        print("5. Display Cards")
        print("6. save and Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            fellow_id = input("Fellow ID: ").strip()
            card_type = input("Card type (visitor/student/staff): ").strip()
            try:
                new_request = create_card(fellow_id, card_type, current_cards)
                print("new_request")
                print()
            except ValueError as e:
                print("Error:", e)
                print()

        elif choice == "2":
            request_id = input("Request ID: ").strip()
            approved_by = input("Approved by: ")
            try:
                approve_request(request_id, approved_by)
                print("Request Approved!")
                print()
            except ValueError as e:
                print("Error:", e)
                print()

        elif choice == "3":
            request_id = input("Request ID: ").strip()
            try:
                issue_card(request_id)
                print("Card Issued!")
                print()
            except ValueError as e:
                print("Error:", e)
                print()

        elif choice == "4":
            request_id = input("Request ID: ").strip()
            try:
                return_card(request_id)
                print("Card Returned!")
                print()
            except ValueError as e:
                print("Error:", e)
                print()

        elif choice == "5":
            available_cards = handle_view(cards)
            print(available_cards)
        elif choice == "6":
            try:
                save_application_data(cards)
                print("Cards Saved!")
                print("Exiting...")
                break
            except (ValueError, OSError) as e:
                print("Error:", e)
                print()
           
        else:
            print(f"\n'{choice}' is not a valid option. Please enter 1, 2, 3, 4 or 5.")
            print()

if __name__ == "__main__":
    run_menu()    
