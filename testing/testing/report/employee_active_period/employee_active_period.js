// Copyright (c) 2024, abdulbasit and contributors
// For license information, please see license.txt
/* eslint-disable */



// this.page.add_menu_item(__("Email"), function() {
// 	me.frm.email_doc();
// }, true, {
// 	shortcut: 'Ctrl+E',
// 	condition: () => !this.frm.is_new()
// });


frappe.query_reports["Employee Active Period"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
		},
		{
			"fieldname":"number_of_employee",
			"label": __("Number Of Employee"),
			"fieldtype": "Int",
			"width": "30",
			// "reqd": 1,
		},



	]
};


	
