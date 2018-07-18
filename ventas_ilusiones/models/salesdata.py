# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SalesData(models.Model):
    _name = 'mysales.maindata'
    _inherit = 'mail.thread'

    name = fields.Char(
        string="Sale Number",
        default=lambda self: 'MS000X',
    )

    customer = fields.Many2one(
        'res.partner',
        string="Customer",
        required=True,
    )

    contract_number = fields.Char(
        string="Contract number",
        required=True,
    )

    price = fields.Float(
        string="Price",
        required=True,
    )

    sales_lines_ids = fields.One2many(
        'mysales.typesofsales_products',
        'mysale_id',
        string="Sale lines",
        required=True,
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('quotation', 'Quotation'),
            ('confirm', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
        string="State",
        default='draft',
        required=True
    )

    @api.model
    def create(self, vals):
        if vals.get('name', 'MS000X') == 'MS000X':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'mysales_maindata'
            ) or 'MS000X'
        return super(SalesData, self).create(vals)
