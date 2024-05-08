// Copyright (c) 2024, abdulbasit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Active Employee Period', {
	// refresh: function(frm) {

	// }
	fetch_detail:function(frm){
		frm.call({
			doc: frm.doc,
			method: "employee_detail",
			freeze: true,
			callback: function(r) {
				console.log(r)
			}
		});

	}
});
