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
