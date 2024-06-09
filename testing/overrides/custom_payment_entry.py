import frappe
from erpnext.accounts.doctype.payment_entry.payment_entry import PaymentEntry


class CustomPaymentEntry(PaymentEntry):
    def validate(self):
        self.update_supplier_numbers() 
        
 
    def getting_supplier_number(self):
        spno = {}
        for i in self.references:
            if i.get("reference_doctype") == 'Journal Entry':
                reference_name = i.get("reference_name")
                supplier_data = frappe.db.get_all("Journal Entry Account", filters={
                    "parenttype": i.get("reference_doctype"),
                    "parent": reference_name,
                    "docstatus": 1,
                    "party_type": "Supplier"
                }, fields=["custom_supplier_number"])
                # Assuming there's only one supplier number per reference
                if supplier_data:
                    spno[reference_name] = supplier_data[0].get("custom_supplier_number")
        return spno
    
    def update_supplier_numbers(self):
        spno = self.getting_supplier_number()  # Call validate_supplier_number
        for reference in self.references:
            if reference.get("reference_doctype") == 'Journal Entry':
                reference_name = reference.get("reference_name")
            # Check for existence in spno and update if found
            if reference_name in spno:
                self.append("references",{"custom_supplier_number":spno[reference_name]}) 
        return None  # This function doesn't need to return anything

            
        