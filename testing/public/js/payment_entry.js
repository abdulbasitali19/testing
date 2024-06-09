frappe.ui.form.on('Payment Entry Reference', {
	reference_name(doc, cdt, cdn){
        debugger;
        var d = frappe.get_doc(cdt, cdn);
        if (d.reference_doctype == "Journal Entry"){
            let spno = frappe.db.get_all("Journal Entry Account",filters={"reference_type": d.reference_doctype, "reference_name": d.reference_name, "docstatus": 1},fields=["custom_supplier_number"])
            d.custom_supplier_number = spno

        }

    }
})





