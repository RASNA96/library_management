# Copyright (c) 2024, rasna and contributors
# For license information, please see license.txt

# import frappe


#def execute(filters=None):
	#columns, data = [], []
	#return columns, data#message = "This is Report"


import frappe
from frappe import _

def execute(filters=None):
    columns, data= get_columns(filters), get_data(filters)
    return columns, data

def get_columns(filters):
    columns = [
        {
            "fieldname": "article_name",
            "label": "Article Name",
            "fieldtype": "Link",
	        "options": "Article",
            "width": 150
        },
        {
            "fieldname": "author",
            "label": "Author",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "publisher",
            "label": "Publisher",
            "fieldtype": "Data",
            "width": 300
        },
        {
            "fieldname": "isbn",
            "label": "ISBN",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "image",
            "label": "Image",
            "fieldtype": "Data",
            "width": 300
        },

    ]
    return columns

def get_data(filters):
    filter_dict = {}

    if filters.name:
        filter_dict["article_name"] = ["like", f"%{filters.article_name}%"]

    if filters.author:
        filter_dict["author"] = ["like", f"%{filters.author}%"]

    if filters.publisher:
        filter_dict["publisher"] = ["like", f"%{filters.publisher}%"]

    if filters.isbn:
        filter_dict["isbn"] = ["like", f"%{filters.isbn}%"]

    if filters.status:
        filter_dict["status"] = ["like", f"%{filters.status}%"]

    if filters.get('image'):
        filter_dict["image"] = ["like", f"%{filters.image}%"]

    article_list = frappe.db.get_all("Article", filters=filter_dict, fields=["article_name", "author", "publisher", "isbn", "status", "image"])

    return article_list
