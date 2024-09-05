from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Foods(models.Model):
    _name = "food_reservation.foods"


    name = fields.Char(string="نام غذا", required=True)
    food_type = fields.Selection([("poloyi", "پلویی"), ("khorack", "خوراک")], string="نوع غذا", required=True)

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if len(rec.name) < 3:
                raise ValidationError("نام نباید کمتر از 3 حرف داشته باشد")



