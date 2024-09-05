from odoo import models, fields



class DateFoods(models.Model):
    _name = "food_reservation.date_foods"
    _rec_name = "date"

    date = fields.Date(string="تاریخ", required=True)
    poloyi_id = fields.Many2one("food_reservation.foods",string="پولویی", required=True,
                                domain=[('food_type', '=', 'poloyi')])
    # poloyiSelect = fields.Boolean(string="انتخاب")
    khorack_id = fields.Many2one("food_reservation.foods",string="خوراک", required=True,
                                 domain=[('food_type', '=', 'khorack')])
    # khorakSelect = fields.Boolean(string="انتخاب")

    _sql_constraints = [('unique_date', 'unique (date)', 'قبلا برای امروز برنامه غذایی مشخص کرده اید')]







