from odoo import models, fields
from datetime import date



class Select(models.Model):
    _name = "food_reservation.select"
    _rec_name = "create_uid"



    # user_id نشان دهنده کس است که در حال حاضر لاگین است
    user_id = fields.Many2one('res.users','Current User', default=lambda self: self.env.user.id, readonly=True)
    date_id = fields.Many2one("food_reservation.date_foods", string="تاریخ", required=True)
    poloyiSelect_id = fields.Many2one(related="date_id.poloyi_id", string="پولویی", )
    poloyiCheck = fields.Boolean(string="انتخاب پولویی")
    khorackSelect_id = fields.Many2one(related="date_id.khorack_id", string="خوراک")
    khorackCheck = fields.Boolean(string="انتخاب خوراک")






