# Copyright (c) 2024, rasna and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        {
            "fieldname": "article",
            "label": _("Article"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "library_member",
            "label": _("Library Member"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "type",
            "label": _("Type"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "date",
            "label": _("Date of Transaction"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "delay_fine",
            "label": _("Delay fine"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "is_damaged",
            "label": _("Is damaged?"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "damage_fine",
            "label": _("Damage fine"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "total_fine",
            "label": _("Total fine"),
            "fieldtype": "Data",
            "width": 150
        }
    ]
    return columns

def get_data(filters):
    filter_dict = {}

    if filters.article:
        filter_dict["article"] = ["like", f"%{filters.article}%"]

    if filters.library_member:
        filter_dict["library_member"] = ["like", f"%{filters.library_member}%"]

    if filters.type:
        filter_dict["type"] = ["like", f"%{filters.type}%"]

    if filters.date:
        filter_dict["date"] = ["like", f"%{filters.date}%"]

    if filters.delay_fine:
        filter_dict["delay_fine"] = ["like", f"%{filters.delay_fine}%"]

    if filters.is_damaged:
        filter_dict["is_damaged"] = ["like", f"%{filters.is_damaged}%"]

    if filters.damage_fine:
        filter_dict["damage_fine"] = ["like", f"%{filters.damage_fine}%"]

    if filters.total_fine:
        filter_dict["total_fine"] = ["like", f"%{filters.total_fine}%"]

    Transaction_list = frappe.db.get_all(
        "Library Transaction",
        filters=filter_dict,
        fields=["article", "library_member", "type", "date", "delay_fine", "is_damaged", "damage_fine", "total_fine"]
    )

    return Transaction_list
