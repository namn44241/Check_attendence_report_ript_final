from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Lich(models.Model):
    _name = 'lich'


    nhan_vien = fields.Many2one(comodel_name='res.partner', string='Nhân viên', required=True)
    buoi = fields.Selection(string='Buổi', selection=[('sang', 'Sáng'), ('chieu', 'Chiều')], required=True)
    gio_bat_dau = fields.Datetime('Giờ bắt đầu', required=True)
    gio_ket_thuc = fields.Datetime('Giờ kết thúc', required=True)
    # ma_lich = fields.Char('Mã lịch', readonly=True, default=lambda self: 'Sequence', copy=False)
    ghi_chu = fields.Text('Ghi chú:')

    @api.constrains('gio_ket_thuc')
    def _check_gio_ket_thuc(self):
        for record in self:
            if record.gio_bat_dau and record.gio_ket_thuc <= record.gio_bat_dau:
                raise ValidationError("Giờ kết thúc phải sau giờ bắt đầu!")

    # @api.model
    # def create(self, vals):
    #     sequence = self.env['ir.sequence'].next_by_code('lich.sequence') or '/'
    #     vals['ma_lich'] = sequence
    #     return super(Lich, self).create(vals)

    @api.constrains('ma_nhan_vien', 'ma_quan_li')
    def _check_ma_nhan_vien_quan_li(self):
        for record in self:
            if record.ma_nhan_vien == record.ma_quan_li:
                raise ValidationError("Nhân viên và Quản lí không được giống nhau!")




class donxin(models.Model):
    _name = 'donxin'
    _description = 'Đơn xin'

    tieu_de = fields.Char(string='Tiêu đề', required=True)
    # ma_donxin = fields.Char('Mã đơn', readonly=True, default=lambda self: 'Sequence', copy=False)
    ma_nhan_vien = fields.Many2one(comodel_name='res.partner', string='Nhân viên', required=True)
    ma_quan_li = fields.Many2one(comodel_name='res.partner', string='Quản lí', required=True)
    loai_don = fields.Selection(selection=[
        ('nghi_phep', 'Nghỉ phép'),
        ('nghi_benh', 'Nghỉ bệnh'),
        ('nghi_khac', 'Nghỉ khác'),
        ('khac', 'Khác')],
        string='Loại đơn', required=True)
    ngay_bat_dau = fields.Datetime('Ngày giờ bắt đầu', required=True)
    ngay_ket_thuc = fields.Datetime('Ngày giờ kết thúc', required=True)
    li_do = fields.Text(string='Lí do', required=True)


    @api.constrains('ngay_ket_thuc')
    def _check_gio_ket_thuc(self):
        for record in self:
            if record.ngay_bat_dau and record.ngay_ket_thuc <= record.ngay_bat_dau:
                raise ValidationError("Ngày kết thúc phải sau ngày bắt đầu!")


class ngươi_dung(models.Model):
    _name = 'nd'

    ten_nguoi_dung = fields.Many2one(comodel_name='res.partner', string='Tên người dùng', required=True)
    ngay_sinh = fields.Date('Ngày sinh', required=True)
    bo_phan = fields.Selection(selection=[
        ('san_pham', 'Team sản phẩm'),
        ('nghien_cuu', 'Team nghiên cứu'),
        ('hon_hop', 'Cả sản phẩm cả ngâm cứu')],
        string='Bộ phận', required=True)
    gioi_tinh = fields.Selection(selection=[
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')],
        string='Giới tính', required=True)
    anh = fields.Binary("Ảnh nhân viên", attachment=True, help="Ném bức ảnh đẹp nhất vào đây")
    sdt = fields.Char(string='Số điện thoại', required=True)
    email = fields.Char(string='Email', required=True)
    chuc_vu = fields.Selection(selection=[
        ('nhan_vien', 'Nhân Viên'),
        ('quan_li', 'Quản lí')],
        string='Chức vụ', required=True)

    # Các trường thông tin khác

    @api.constrains('email')
    def _check_valid_email(self):
        for record in self:
            if '@' not in record.email:
                raise ValidationError("Địa chỉ email không hợp lệ. Vui lòng nhập đúng định dạng email.")
    @api.constrains('sdt')
    def _check_valid_phone_number(self):
        for record in self:
            if len(record.sdt) != 10 or not record.sdt.startswith('0') or not record.sdt.isdigit():
                raise ValidationError(
                    "Số điện thoại không hợp lệ. Số điện thoại phải có 10 chữ số và bắt đầu bằng số 0.")

    @api.constrains('ngay_sinh')
    def _check_ngay_sinh(self):
        for record in self:
            if record.ngay_sinh:
                birth_date = datetime.strptime(str(record.ngay_sinh), "%Y-%m-%d").date()
                if birth_date.year > 2005:
                    raise ValidationError("Năm sinh phải nhỏ hơn 2005.")

class CongViec(models.Model):
    _name = 'congviec'
    _description = 'Công Việc'

    ten_cong_viec = fields.Text(string='Tên Công Việc', required=True)
    mota = fields.Text(string='Mô tả')
    thoi_han = fields.Datetime(string='Thời gian giao')
    trang_thai = fields.Selection([
        ('xong', 'Hoàn thành'),
        ('chua', 'Chưa hoàn thành')
    ], string='Trạng thái', default='chua')
    ma_quan_li = fields.Many2one(comodel_name='res.partner', string='Quản lí', required=True)