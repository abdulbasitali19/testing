# Copyright (c) 2024, abdulbasit and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns() 
	data = get_data(filters) 
	return columns, data


def get_data(filters):
    if filters:
        data = []
        from_date = filters.get("from_date")
        to_date = filters.get("to_date")
        number_of_employee = filters.get("number_of_employee") or 10
        employee_detail = frappe.db.sql(f"""
			SELECT
				employee,
				employee_name,
				date_of_joining
			FROM 
				`tabEmployee`
			Where
				status = "Active" and date_of_joining between '{from_date}' and '{to_date}'
			LIMIT {number_of_employee}""", as_dict=1,debug = True)
        for i in employee_detail:
            employee_dict = {}
            employee_dict["employee"] = i.get("employee")
            employee_dict["employee_name"] = i.get("employee_name")
            employee_dict["date_of_joining"] = i.get("date_of_joining")
            data.append(employee_dict)
        return data
    else:
        frappe.throw("Please select appropriate date in filters")


def get_columns():
    columns = [
	 {
            "label": _("Employee"),
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 90,
        },
		{
            "label": _("Employee Name"),
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 90,
        },
        {
            "label": _("Date Of Joininig"),
            "fieldname": "date_of_joining",
            "fieldtype": "Date",
            "width": 90,
        },		
  
  
	]
    return columns