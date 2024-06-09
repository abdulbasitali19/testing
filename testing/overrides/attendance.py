import frappe
from frappe.utils import (
	add_days,
	cint,
	cstr,
	format_date,
	get_datetime,
	get_link_to_form,
	getdate,
	nowdate,
)

@frappe.whitelist()
def mark_bulk_attendance(data):
    import json

    if isinstance(data, str):
        data = json.loads(data)
    data = frappe._dict(data)
    if not data.unmarked_days:
        frappe.throw(_("Please select a date."))

    for date in data.unmarked_days:
        doc_dict = {
            "doctype": "Attendance",
            "employee": data.employee,
            "attendance_date": get_datetime(date),
            "status": data.status,
        }
        attendance = frappe.get_doc(doc_dict).insert()
        attendance.submit()
    count = frappe.db.count("Attendance", {"employee": data.employee})
    if count == len(data.unmarked_days):
        # create a new document
        doc = frappe.get_doc({
            'doctype': 'Salary Slip',
            'employee': data.employee
        }).insert()
        doc.submit()
        salary_doc = frappe.new_doc("Salary Slip According To Date period")
        salary_doc.employee = data.employee
        salary_doc.from_date = get_datetime(data.from_date)
        salary_doc.to_date = get_datetime(data.to_date)
        salary_doc.amount_to_paid = frappe.db.get_value("Salary Slip", {"employee":data.employee}, "net_pay")
        salary_doc.insert(ignore_permissions = True)
        salary_doc.submit()



        
        
        