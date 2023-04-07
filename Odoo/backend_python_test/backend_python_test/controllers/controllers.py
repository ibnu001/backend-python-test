# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
import json

class BackendPythonTest(http.Controller):

    @http.route('/en/update-material', auth='public', type='json', methods=['POST'])
    def api_update_material(self, **post):
        data = json.loads(request.httprequest.data.decode('utf-8'))

        m_code = data["m_code"]
        update_material = request.env['register.material'].sudo().search([("m_code", "=", m_code)])

        m_name = data["m_name"]
        m_type = data["m_type"]
        m_buy_price = data["m_buy_price"]
        m_supplier_id = data["m_supplier_id"]
        search_code_m_suplier = request.env['res.partner'].sudo().search([("name", "=", m_supplier_id)]).id

        update_data = {
            "m_name" : m_name,
            "m_type" : m_type,
            "m_buy_price" : m_buy_price,
            "m_supplier_id" : search_code_m_suplier
        }

        update_material.write(update_data)

        if update_material:
            data = { 
                "Success" : "Data Successfully updated"
            }
        else:
            data = {
                "Failed" : "Data Update Failed"
            }

        return data
    

    @http.route('/en/delete-material', auth='public', type='json', methods=['POST'])
    def api_delete_material(self, **post):
        data = json.loads(request.httprequest.data.decode('utf-8'))

        m_code = data["m_code"]
        delete_material = request.env['register.material'].sudo().search([("m_code", "=", m_code)])

        delete_material.unlink()

        if delete_material:
            data = { 
                "Success" : "Data successfully deleted"
            }
        else:
            data = {
                "Failed" : "Failed to delete data"
            }

        return data