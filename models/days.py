from odoo import models, fields, api


class Days(models.Model):
    _name = "food_reservation.days"
    _rec_name = "date"

    date = fields.Date(string="تاریخ", required=True, help="تاریخی که میخواهید غذا سفارش دهید را انتخاب کنید")
    poloyi_id = fields.Many2one("food_reservation.foods", string="پولویی", required=True,
                                 domain=[('food_type', '=', 'poloyi')])
    khorack_id = fields.Many2one("food_reservation.foods", string="خوراک", required=True,
                                  domain=[('food_type', '=', 'khorack')])
    day_off = fields.Boolean()

    _sql_constraints = [('unique_date', 'unique (date)', 'قبلا برای امروز برنامه غذایی مشخص کرده اید')]

    def get_template(self):
        # فرض می‌کنیم که می‌خواهید فایل‌های پیوست شده به poloyi_id را دانلود کنید
        food_record = self.poloyi_id

        # اگر هیچ پیوستی وجود نداشته باشد
        if not food_record.record_file:
            return {
                'type': 'ir.actions.act_window_message',
                'title': 'خطا',
                'message': 'هیچ فایلی برای دانلود وجود ندارد.',
                'close_button_title': 'بستن',
            }

        # ایجاد لینک دانلود برای اولین پیوست
        attachment_ids = food_record.record_file.ids
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment_ids[0],  # برای دانلود اولین پیوست
            'target': 'self',
        }