# Copyright (c) 2024, rasna and contributors
# For license information, please see license.txt

# import frappe
# import frappe
# from frappe.model.document import Document
#
#
# class LibraryMembership(Document):
# 	# check before submitting this document
# 	def before_submit(self):
# 		exists = frappe.db.exists(
# 		"Library Membership",
# 		{
# 		"library_member": self.library_member,
# 		"docstatus": 1,
# 		# check if the membership's end date is later than this membership's start date
# 		"to_date": (">", self.from_date),
# 		},
# 		)
# 		if exists:
# 			frappe.throw("There is an active membership for this member")
#
# 		# get loan period and compute to_date by adding loan_period to from_date
# 		loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
# 		self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
#
# 	def validate(self):
# 		if self.from_date > self.to_date :
# 			frappe.throw("From date should not be after the To date")


import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
    # Check before submitting this document
    def before_save(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                # Check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")
        # Calculate to_date based on selected duration (if not manually specified)
        if not self.cutomise_to_date and self.duration:
            duration_days = int(self.duration.split()[0])  # Extracting the number of days
            self.to_date = frappe.utils.add_days(self.from_date, duration_days)

    def validate(self):
        if self.from_date and self.to_date and self.from_date > self.to_date:
            frappe.throw(
                msg='The start date cannot be later than the end date.',
                title='Date Validation Error',
            )
