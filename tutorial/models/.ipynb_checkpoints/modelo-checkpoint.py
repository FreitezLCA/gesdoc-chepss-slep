# -*- coding: utf-8 -*-
from odoo import api, fields, models#, _, tools
#from odoo.osv import expression
#from odoo.exceptions import UserError, ValidationError
#from bisect import bisect_left
#from collections import defaultdict
#import re

#ACCOUNT_REGEX = re.compile(r'(?:(\S*\d+\S*))?(.*)')
#ACCOUNT_CODE_REGEX = re.compile(r'^[A-Za-z0-9.]+$')

class Modelo(models.Model):
    _name = "modelo.modelo"
    _description = "Este es un Modelo"
    #_order = "is_off_balance, code, company_id"
    #_check_company_auto = True
