# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "my.pet"
    _description = "My pet model"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
    dob = fields.Date('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image") #1 model nhiều hình ảnh
    owner_id = fields.Many2one('res.partner', string='Owner') #Nhiều người sở hữu 1 model
    product_ids = fields.Many2many(comodel_name='product.product', 
                                string="Related Products", 
                                relation='pet_product_rel',
                                column1='col_pet_id',
                                column2='col_product_id')
