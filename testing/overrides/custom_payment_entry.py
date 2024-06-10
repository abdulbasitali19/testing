import frappe
from erpnext.accounts.doctype.payment_entry.payment_entry import PaymentEntry

class CustomPaymentEntry(PaymentEntry):
    def validate(self):
        self.update_supplier_numbers() 

    def getting_supplier_number(self):
        query = """
            SELECT 
                jea.custom_supplier_number,
                je.name
            FROM                
                `tabJournal Entry Account` jea
            INNER JOIN 
                `tabJournal Entry` je ON je.name = jea.parent
            WHERE
                jea.party_type = 'Supplier'
                AND je.docstatus = 1
        """
        spno = frappe.db.sql(query, as_dict=1)
        return spno



    def update_supplier_numbers(self):
        spno = self.getting_supplier_number()
        spno_dict = {item['name']: item['custom_supplier_number'] for item in spno}
        
        # Create a list of existing reference names for quick lookup
        existing_reference_names = {reference.get("reference_name"): reference for reference in self.references}

        for name, custom_supplier_number in spno_dict.items():
            if name in existing_reference_names:
                self.reference = []
                reference = existing_reference_names[name]
                self.append("references", {
                    "reference_doctype": reference.get("reference_doctype"),
                    "reference_name": name,
                    "total_amount": reference.get("total_amount"),
                    "outstanding_amount": reference.get("outstanding_amout"),
                    "allocated_amount": reference.get("allocated_amount"),
                    "custom_supplier_number": custom_supplier_number
                })

        return None


    def update_supplier_numbers(self):
        spno = self.getting_supplier_number()
        spno_dict = {item['name']: item['custom_supplier_number'] for item in spno}
        for reference in self.references:
            if reference.get("reference_doctype") == 'Journal Entry':
                reference_doctype = reference.get("reference_doctype")
                reference_name = reference.get("reference_name")
                total_amount = reference.get("total_amount")
                outstanding_amout = reference.get("outstanding_amout")
                allocated_amount = reference.get("allocated_amount")
                if reference_name in spno_dict:
                    self.append("references",{
                        "reference_doctype":reference_doctype,
                        "reference_name":reference_name,
                        "total_amount":total_amount,
                        "outstanding_amount":outstanding_amout,
                        "allocated_amount":allocated_amount,
                        "custom_supplier_number": spno_dict[reference_name]})
                    
        return None

