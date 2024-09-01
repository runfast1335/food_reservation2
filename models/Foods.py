from odoo import models, fields

class Foods(models.Model):
    _name = "food_reservation.foods"

    name = fields.Char(string="نام غذا", required=True)
    food_type = fields.Selection([("poloyi", "پلویی"), ("khorack", "خوراک")], string="نوع غذا", required=True)



