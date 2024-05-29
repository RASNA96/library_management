// Copyright (c) 2024, rasna and contributors
// For license information, please see license.txt

frappe.query_reports["article1 report"] = {
    "filters": [
        {
					  "fieldname": "article_name",
						"label": __("Article Name"),
						"fieldtype": "Link",
						"options": "Article",
						"width": 150
        },
        {
            "fieldname": "author",
            "label": __("Author"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "publisher",
            "label": __("Publisher"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "isbn",
            "label": __("ISBN"),
            "fieldtype": "Data",
            "width": 150
        }
    ]
};
