from odoo import models, fields, api




class Select(models.Model):
    _name = "food_reservation.select"
    _rec_name = "create_uid"




    # user_id نشان دهنده کس است که در حال حاضر لاگین است
    user_id = fields.Many2one('res.users','Current User', default=lambda self: self.env.user.id, readonly=True)
    date_id = fields.Many2one("food_reservation.days", string="تاریخ", required=True)
    poloyiSelect_id = fields.Many2one(related="date_id.poloyi_id", string="پولویی", )
    poloyiCheck = fields.Boolean(string="انتخاب پولویی")
    khorackSelect_id = fields.Many2one(related="date_id.khorack_id", string="خوراک")
    khorackCheck = fields.Boolean(string="انتخاب خوراک")

    def get_template(self):
        # فرض می‌کنیم که می‌خواهید فایل باینری مرتبط با poloyiSelect_id را دانلود کنید
        food_record = self.poloyiSelect_id

        # اگر هیچ فایل باینری وجود نداشته باشد
        if not food_record.record_fileb:
            return {
                'type': 'ir.actions.act_window_message',
                'title': 'خطا',
                'message': 'هیچ فایلی برای دانلود وجود ندارد.',
                'close_button_title': 'بستن',
            }

        # نام فایل را از فیلد record_fileb_name دریافت می‌کنیم
        file_data = food_record
        file_name = food_record.record_fileb_name or "downloaded_file"

        # ایجاد یک فایل باینری برای دانلود
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/?model=food_reservation.foods&field=record_fileb&id=%s&filename=%s&download=true' % (food_record.id, file_name),
            'target': 'self',
        }









