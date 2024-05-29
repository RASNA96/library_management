# import frappe
# from frappe.model.document import Document
#
# class LibraryTransaction(Document):
#     def before_submit(self):
#         if self.type == "Issue":
#             self.validate_issue()
#             self.check_damage_fine()
#             # Set the article status to be Issued
#             article = frappe.get_doc("Article", self.article)
#             article.status = "Issued"
#             article.save()
#
#         elif self.type == "Return":
#             self.validate_return()
#             # Set the article status to be Available
#             article = frappe.get_doc("Article", self.article)
#             article.status = "Available"
#             article.save()
#
#     def before_save(self):
#         self.check_overdue_fine()
#         self.check_damage_fine()
#
#
#     def validate_issue(self):
#         self.validate_membership()
#         article = frappe.get_doc("Article", self.article)
#         # Article cannot be issued if it is already issued
#         if article.status == "Issued":
#             frappe.throw("Article is already issued by another member")
#
#     def validate_return(self):
#         article = frappe.get_doc("Article", self.article)
#         # Article cannot be returned if it is not issued first
#         if article.status == "Available":
#             frappe.throw("Article cannot be returned without being issued first")
#
#     def validate_membership(self):
#         # Check if a valid membership exists for this library member
#         valid_membership = frappe.db.exists(
#             "Library Membership",
#             {
#                 "library_member": self.library_member,
#                 "docstatus": 1,
#                 "from_date": ("<", self.date),
#                 "to_date": (">", self.date),
#             },
#         )
#         if not valid_membership:
#             frappe.throw("The member does not have a valid membership")
#
#     def check_overdue_fine(self):
#         # Get loan period and single day fine from Library Settings
#         loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
#         fine_per_day = frappe.db.get_single_value("Library Settings", "fine_per_day")
#
#         # Assuming the issue date and return date are tracked
#         id=frappe.db.exists("Library Transaction", {"type":"Issue", "article":self.article, "library_member":self.library_member})
#
#         issue_date = frappe.db.get_value("Library Transaction",id, "date")
#         days_overdue = frappe.utils.date_diff(self.date, issue_date)
#
#         if days_overdue > loan_period:
#             overdue_days = days_overdue - loan_period
#             total_fine = self.total_fine or 0
#             self.delay_fine = overdue_days * fine_per_day
#             self.total_fine = total_fine + self.delay_fine
#         else:
#             self.total_fine = 0
#
#     def check_damage_fine(self):
#         """
#         Adds the damage fine to the total fine if the item is damaged.
#
#         Assumes that `self.is_damaged` is a boolean indicating if the item is damaged,
#         and `self.damage_fine` is the fine amount for the damage, selected from predefined options.
#         """
#         if self.is_damaged:
#             # Convert the damage fine to float
#             damage_fine = float(self.damage_fine)
#
#             # Initialize total_fine to 0 if it does not exist
#             if not hasattr(self, 'total_fine'):
#                 self.total_fine = 0
#
#             # Add the damage fine to the total fine
#             self.total_fine += damage_fine
#











#
# import frappe
# from frappe.model.document import Document
#
# class LibraryTransaction(Document):
#     def before_submit(self):
#         if self.type == "Issue":
#             self.validate_issue()
#             self.check_damage_fine()
#             # Set the article status to be Issued
#             article = frappe.get_doc("Article", self.article)
#             article.status = "Issued"
#             article.save()
#
#         elif self.type == "Return":
#             self.validate_return()
#             # Set the article status to be Available
#             article = frappe.get_doc("Article", self.article)
#             article.status = "Available"
#             article.save()
#
#     def before_save(self):
#         self.check_overdue_fine()
#         self.check_damage_fine()
#
#     def validate_issue(self):
#         self.validate_membership()
#         article = frappe.get_doc("Article", self.article)
#         # Article cannot be issued if it is already issued
#         if article.status == "Issued":
#             frappe.throw("Article is already issued by another member")
#
#     def validate_return(self):
#         article = frappe.get_doc("Article", self.article)
#         # Article cannot be returned if it is not issued first
#         if article.status == "Available":
#             frappe.throw("Article cannot be returned without being issued first")
#
#     def validate_membership(self):
#         # Check if a valid membership exists for this library member
#         valid_membership = frappe.db.exists(
#             "Library Membership",
#             {
#                 "library_member": self.library_member,
#                 "docstatus": 1,
#                 "from_date": ("<", self.date),
#                 "to_date": (">", self.date),
#             },
#         )
#         if not valid_membership:
#             frappe.throw("The member does not have a valid membership")
#
#     def check_overdue_fine(self):
#         # Get loan period and single day fine from Library Settings
#         loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
#         fine_per_day = frappe.db.get_single_value("Library Settings", "fine_per_day")
#
#         # Assuming the issue date and return date are tracked
#         id=frappe.db.exists("Library Transaction", {"type":"Issue", "article":self.article, "library_member":self.library_member})
#
#         issue_date = frappe.db.get_value("Library Transaction",id, "date")
#         days_overdue = frappe.utils.date_diff(self.date, issue_date)
#
#         if days_overdue > loan_period:
#             overdue_days = days_overdue - loan_period
#             total_fine = self.total_fine or 0
#             self.delay_fine = overdue_days * fine_per_day
#             self.total_fine = total_fine + self.delay_fine
#         else:
#             self.total_fine = 0
#
#     def check_damage_fine(self):
#         """
#         Adds the damage fine to the total fine if the item is damaged.
#
#         Assumes that `self.is_damaged` is a boolean indicating if the item is damaged,
#         and `self.damage_fine` is the fine amount for the damage, selected from predefined options.
#         """
#         if self.is_damaged:
#             # Convert the damage fine to float
#             damage_fine = float(self.damage_fine)
#
#             # Initialize total_fine to 0 if it does not exist
#             if not hasattr(self, 'total_fine'):
#                 self.total_fine = 0
#
#             # Add the damage fine to the total fine
#             self.total_fine += damage_fine
#
#     @frappe.whitelist()
#     def has_pending_fine(self):
#         """
#         Check if the library member has any pending fines.
#         """
#         # Get the total fine for the library member
#         total_fine = frappe.db.get_value("Library Transaction",
#                                          {"library_member": self.library_member, "docstatus": 1},
#                                          "sum(total_fine)")
#
#         return total_fine or 0
#
#
#
#
# import frappe
# from frappe.model.document import Document
#
# class LibraryTransaction(Document):
#     def before_submit(self):
#         if self.type == "Issue":
#             self.validate_issue()
#             self.check_damage_fine()
#             # Set the article status to be Issued for all articles in the child table
#             for item in self.get("article_list"):
#                 article = frappe.get_doc("Article", item.article)
#                 article.status = "Issued"
#                 article.save()
#
#         elif self.type == "Return":
#             self.validate_return()
#             # Set the article status to be Available for all articles in the child table
#             for item in self.get("article_list"):
#                 article = frappe.get_doc("Article", item.article)
#                 article.status = "Available"
#                 article.save()
#
#     def before_save(self):
#         self.check_overdue_fine()
#         self.check_damage_fine()
#
#     def validate_issue(self):
#         self.validate_membership()
#         for item in self.get("article_list"):
#             article = frappe.get_doc("Article", item.article)
#             # Article cannot be issued if it is already issued
#             if article.status == "Issued":
#                 frappe.throw(f"Article {article.name} is already issued by another member")
#
#     def validate_return(self):
#         for item in self.get("article_list"):
#             article = frappe.get_doc("Article", item.article)
#             # Article cannot be returned if it is not issued first
#             if article.status == "Available":
#                 frappe.throw(f"Article {article.name} cannot be returned without being issued first")
#
#     def validate_membership(self):
#         # Check if a valid membership exists for this library member
#         valid_membership = frappe.db.exists(
#             "Library Membership",
#             {
#                 "library_member": self.library_member,
#                 "docstatus": 1,
#                 "from_date": ("<", self.date),
#                 "to_date": (">", self.date),
#             },
#         )
#         if not valid_membership:
#             frappe.throw("The member does not have a valid membership")
#
#     def check_overdue_fine(self):
#         # Get loan period and single day fine from Library Settings
#         loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
#         fine_per_day = frappe.db.get_single_value("Library Settings", "fine_per_day")
#
#         # Assuming the issue date and return date are tracked
#         for item in self.get("article_list"):
#             id = frappe.db.exists("Library Transaction", {"type": "Issue", "article": item.article, "library_member": self.library_member})
#             issue_date = frappe.db.get_value("Library Transaction", id, "date")
#             days_overdue = frappe.utils.date_diff(self.date, issue_date)
#
#             if days_overdue > loan_period:
#                 overdue_days = days_overdue - loan_period
#                 total_fine = self.total_fine or 0
#                 self.delay_fine = overdue_days * fine_per_day
#                 self.total_fine = total_fine + self.delay_fine
#             else:
#                 self.total_fine = 0
#
#     def check_damage_fine(self):
#         """
#         Adds the damage fine to the total fine if the item is damaged.
#         """
#         if self.is_damaged:
#             # Convert the damage fine to float
#             damage_fine = float(self.damage_fine)
#
#             # Initialize total_fine to 0 if it does not exist
#             if not hasattr(self, 'total_fine'):
#                 self.total_fine = 0
#
#             # Add the damage fine to the total fine
#             self.total_fine += damage_fine
#
#     @frappe.whitelist()
#     def has_pending_fine(self):
#         """
#         Check if the library member has any pending fines.
#         """
#         # Get the total fine for the library member
#         total_fine = frappe.db.get_value("Library Transaction",
#                                          {"library_member": self.library_member, "docstatus": 1},
#                                          "sum(total_fine)")
#
#         return total_fine or 0
#





# import frappe
# from frappe.model.document import Document
#
# class LibraryTransaction(Document):
#     def before_submit(self):
#         if self.type == "Issue":
#             self.validate_issue()
#             self.check_damage_fine()
#             # Set the article status to be Issued for all articles in the child table
#             for item in self.get("article_list"):
#                 article = frappe.get_doc("Article", item.article)
#                 article.status = "Issued"
#                 article.save()
#
#         elif self.type == "Return":
#             self.validate_return()
#             # Set the article status to be Available for all articles in the child table
#             for item in self.get("article_list"):
#                 article = frappe.get_doc("Article", item.article)
#                 article.status = "Available"
#                 article.save()
#
#     def before_save(self):
#         self.check_overdue_fine()
#         self.check_damage_fine()
#
#     def validate_issue(self):
#         self.validate_membership()
#         self.check_issue_limit()
#         for item in self.get("article_list"):
#             article = frappe.get_doc("Article", item.article)
#             # Article cannot be issued if it is already issued
#             if article.status == "Issued":
#                 frappe.throw(f"Article {article.name} is already issued by another member")
#
#     def validate_return(self):
#         for item in self.get("article_list"):
#             article = frappe.get_doc("Article", item.article)
#             # Article cannot be returned if it is not issued first
#             if article.status == "Available":
#                 frappe.throw(f"Article {article.name} cannot be returned without being issued first")
#
#     def validate_membership(self):
#         # Check if a valid membership exists for this library member
#         valid_membership = frappe.db.exists(
#             "Library Membership",
#             {
#                 "library_member": self.library_member,
#                 "docstatus": 1,
#                 "from_date": ("<", self.date),
#                 "to_date": (">", self.date),
#             },
#         )
#         if not valid_membership:
#             frappe.throw("The member does not have a valid membership")
#
#     def check_issue_limit(self):
#         # Get the maximum number of articles that can be issued from Library Settings
#         maximum_number_of_issued_articles = frappe.db.get_single_value("Library Settings", "maximum_number_of_issued_articles")
#
#         # Count the number of currently issued articles for this member
#         current_issued_articles = frappe.db.count("Library Transaction",
#                                                   filters={
#                                                       "library_member": self.library_member,
#                                                       "type": "Issue",
#                                                       "docstatus": 1
#                                                   })
#
#         # Add the number of articles being issued in this transaction
#         articles_being_issued = len(self.get("article_list"))
#
#         if current_issued_articles + articles_being_issued > maximum_number_of_issued_articles:
#             frappe.throw(f"You have reached the maximum limit of {maximum_number_of_issued_articles} issued articles.")
#
#
#
#     def check_overdue_fine(self):
#         # Get loan period and single day fine from Library Settings
#         loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
#         fine_per_day = frappe.db.get_single_value("Library Settings", "fine_per_day")
#
#         # Assuming the issue date and return date are tracked
#         for item in self.get("article_list"):
#             id = frappe.db.exists("Library Transaction", {"type": "Issue", "article": item.article, "library_member": self.library_member})
#             issue_date = frappe.db.get_value("Library Transaction", id, "date")
#             days_overdue = frappe.utils.date_diff(self.date, issue_date)
#
#             if days_overdue > loan_period:
#                 overdue_days = days_overdue - loan_period
#                 total_fine = self.total_fine or 0
#                 self.delay_fine = overdue_days * fine_per_day
#                 self.total_fine = total_fine + self.delay_fine
#             else:
#                 self.total_fine = 0
#
#     def check_damage_fine(self):
#         """
#         Adds the damage fine to the total fine if the item is damaged.
#         """
#         if self.is_damaged:
#             # Convert the damage fine to float
#             damage_fine = float(self.damage_fine)
#
#             # Initialize total_fine to 0 if it does not exist
#             if not hasattr(self, 'total_fine'):
#                 self.total_fine = 0
#
#             # Add the damage fine to the total fine
#             self.total_fine += damage_fine
#
#     @frappe.whitelist()
#     def has_pending_fine(self):
#         """
#         Check if the library member has any pending fines.
#         """
#         # Get the total fine for the library member
#         total_fine = frappe.db.get_value("Library Transaction",
#                                          {"library_member": self.library_member, "docstatus": 1},
#                                          "sum(total_fine)")
#
#         return total_fine or 0










import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            self.check_damage_fine()
            # Set the article status to be Issued for all articles in the child table
            for item in self.get("article_list"):
                article = frappe.get_doc("Article", item.article)
                article.status = "Issued"
                article.save()

        elif self.type == "Return":
            self.validate_return()
            # Set the article status to be Available for all articles in the child table
            for item in self.get("article_list"):
                article = frappe.get_doc("Article", item.article)
                article.status = "Available"
                article.save()

    def before_save(self):
        self.check_overdue_fine()
        self.check_damage_fine()

    def validate_issue(self):
        self.validate_membership()
        self.check_issue_limit()
        for item in self.get("article_list"):
            article = frappe.get_doc("Article", item.article)
            # Article cannot be issued if it is already issued
            if article.status == "Issued":
                frappe.throw(f"Article {article.name} is already issued by another member")

    def validate_return(self):
        for item in self.get("article_list"):
            article = frappe.get_doc("Article", item.article)
            # Article cannot be returned if it is not issued first
            if article.status == "Available":
                frappe.throw(f"Article {article.name} cannot be returned without being issued first")

    def validate_membership(self):
        # Check if a valid membership exists for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": 1,
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

    def check_issue_limit(self):
        # Get the maximum number of articles that can be issued from Library Settings
        maximum_number_of_issued_articles = frappe.db.get_single_value("Library Settings", "maximum_number_of_issued_articles")

        # Count the number of currently issued articles for this member
        current_issued_articles = frappe.db.count("Library Transaction",
                                                  filters={
                                                      "library_member": self.library_member,
                                                      "type": "Issue",
                                                      "docstatus": 1
                                                  })

        # Add the number of articles being issued in this transaction
        articles_being_issued = len(self.get("article_list"))

        if current_issued_articles + articles_being_issued > maximum_number_of_issued_articles:
            frappe.throw(f"You have reached the maximum limit of {maximum_number_of_issued_articles} issued articles.")

    def check_overdue_fine(self):
        # Get loan period and single day fine from Library Settings
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        fine_per_day = frappe.db.get_single_value("Library Settings", "fine_per_day")

        # Assuming the issue date and return date are tracked
        for item in self.get("issued_articles"):
            id = frappe.db.exists("Library Transaction", {"type": "Issue", "article": item.article, "library_member": self.library_member})
            if id:
                issue_date = frappe.db.get_value("Issued Articles", id, "issue_date")
                print(issue_date, id)
                date_diff = frappe.utils.date_diff(self.date, issue_date)
            else:
                frappe.throw("Issue Transaction not found")

            if date_diff > loan_period:
                overdue_days = date_diff - loan_period
                total_fine = self.total_fine or 0
                self.delay_fine = overdue_days * fine_per_day
                print(overdue_days, fine_per_day)
                self.total_fine = total_fine + self.delay_fine
            else:
                self.total_fine = 0

    def check_damage_fine(self):
        """
        Adds the damage fine to the total fine if the item is damaged.
        """
        if self.is_damaged:
            # Convert the damage fine to float
            damage_fine = float(self.damage_fine)

            # Initialize total_fine to 0 if it does not exist
            if not hasattr(self, 'total_fine'):
                self.total_fine = 0

            # Add the damage fine to the total fine
            self.total_fine += damage_fine

    @frappe.whitelist()
    def has_pending_fine(self):
        """
        Check if the library member has any pending fines.
        """
        # Get the total fine for the library member
        total_fine = frappe.db.get_value("Library Transaction",
                                         {"library_member": self.library_member, "docstatus": 1},
                                         "sum(total_fine)")

        return total_fine or 0
