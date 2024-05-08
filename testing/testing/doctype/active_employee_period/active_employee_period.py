# Copyright (c) 2024, abdulbasit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ActiveEmployeePeriod(Document):
    @frappe.whitelist()
    def employee_detail(self):
        try:
            # Retrieve input dates
            from_date = self.from_date
            to_date = self.to_date

            # Query active employees within the specified date range
            employee_table = frappe.db.sql(f"""
                SELECT
                    employee,
                    employee_name,
                    date_of_joining
                FROM 
                    `tabEmployee`
                WHERE
                    status = "Active" AND date_of_joining BETWEEN '{from_date}' AND '{to_date}'
                """, as_dict=True, debug=True)

            # Append retrieved employees to the Employee_table field
            for employee in employee_table:
                self.append("employee_table", {
                    "employee": employee.get("employee"),
                    "employee_name": employee.get("employee_name"),
                    "date_of_joining": employee.get("date_of_joining")
                })
        except Exception as e:
            frappe.log_error(f"Error in employee_detail: {e}", "Employee Active Period")
