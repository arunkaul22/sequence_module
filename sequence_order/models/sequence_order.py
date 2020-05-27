from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class SequenceOrder(models.Model):
    _name = "sequence.order"
    _description = "Create Sequence in Custom Module"


    sequence = fields.Char('Order Reference', required=True, index=True, copy=False, default='New')
    name = fields.Char(string="Name")
    item_use = fields.Text(string="Use")
    item_id = fields.Integer(string="Item ID")
    item_images = fields.Binary(string="Image")
    registration_date = fields.Date(string="Registration Date")
    item_price = fields.Integer(string="Price")
    item_category = fields.Selection([('laptop', 'Laptops'), ('mobile', 'Mobiles'), (
        'household', 'HouseHolds'), ('accessory', 'Accessories'), ('toy', 'Toys')], string='Categories')

    item_type = fields.Boolean(string="Prime")
    item_garuntee = fields.Selection(
                    [('na', 'No Garuntee'), ('3', '3 Months'), ('6', '6 Months'), ('1', '1 Year')], string="Garuntee Period")
    color = fields.Integer(string="Color")
    discount = fields.Integer(string="Discount")
    final_price = fields.Integer(string="Final Price", compute='_final_price')
    country = fields.Many2one('res.country')


    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('sequence.order')
        return super(SequenceOrder, self).create(vals)

    @api.depends('item_price', 'discount')
    def _final_price(self):
        for r in self:
            if not r.item_price:
                r.final_price = 0.0
            else:
                r.final_price = r.item_price-r.discount

    @api.constrains('item_price', 'discount')
    def _check_valid_price(self):
        if self.item_price == self.discount:
            raise ValidationError("Item price & discount cannot be same")

    @api.onchange('final_price')
    def _verify_valid_price(self):
        if self.final_price < 0:
             raise UserError("final price cannot be negative")
   