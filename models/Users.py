from odoo import models, fields



class Users(models.Model):
    _name = "food_reservation.users"
    _rec_name = "name_id"

    name_id = fields.Many2one("res.users",string= "نام کاربری", required=True)


