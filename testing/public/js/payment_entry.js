frappe.ui.form.on('Payment Entry Reference', {
	reference_name(doc, cdt, cdn){
        debugger;
        var d = frappe.get_doc(cdt, cdn);
        if (d.reference_doctype == "Journal Entry"){
            spno = frappe.db.get_value("Journal Entry",d.reference_name,"Custom_supplier_number")
            frm.set_value("Custom_supplier_number", spno)

        }

    }
})


