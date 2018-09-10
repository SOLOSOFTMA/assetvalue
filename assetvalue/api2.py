# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import json
import frappe
import frappe.handler
import frappe.client
from frappe.utils.response import build_response
from frappe import _
from six.moves.urllib.parse import urlparse, urlencode

def sal_slip_checker(doc, methode):
	payroll_list = frappe.get_all('Payroll Entry',
								 filters={'docstatus':1,'posting_date':doc.posting_date},
								 fields=['name'])
	for payroll in payroll_list:
		jva = frappe.get_all('Journal Entry Account',
									 filters={'docstatus':1,'reference_type':"Payroll Entry",'reference_name':payroll.name},
									 fields=['name','parent'])
		if len(jva) and len(jva)>0:
			parents = [jv.parent for jv in jva]
			frappe.throw("Salary slip: {} is linked with Journal Entry: {}".format(doc.name, parents))

