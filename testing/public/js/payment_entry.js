frappe.ui.form.on('Payment Entry',{
    validate: function(frm) {
        frappe.call({
            method: "testing.overrides.payment_entry.updating_supllier_number_in_references",
            callback: function(r, rt) {
                if (r.message) {
                    frm.doc.references.forEach(function(reference) {
                        if (reference.reference_name in r.message) {
                            // Assuming you want to update custom_supplier_number in the same reference object
                            reference.custom_supplier_number = r.message[reference.reference_name];
                            // Optionally, if you want to update the form immediately
                            frappe.model.set_value(reference.doctype, reference.name, "custom_supplier_number", r.message[reference.reference_name]);
                        }
                    });
                }
            }
        });
    }
    


})




    // frappe.ui.form.on('Payment Entry Reference', {
    //     reference_name(doc, cdt, cdn) {
    //         debugger;
    //         var d = frappe.get_doc(cdt, cdn);
    //         if (d.reference_doctype == "Journal Entry") {
    //             let spno = frappe.db.get_all("Journal Entry Account", filters = { "reference_type": d.reference_doctype, "reference_name": d.reference_name, "docstatus": 1 }, fields = ["custom_supplier_number"])
    //             d.custom_supplier_number = spno

    //         }

    //     }
    // })





