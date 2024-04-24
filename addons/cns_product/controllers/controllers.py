from datetime import datetime
from odoo import http
from odoo.http import request
import odoo.exceptions
import base64

class LichAPI(http.Controller):

    @http.route('/get_lich_id', type="json", auth="none", methods=["GET"], csrf=False)
    def get_all_ids(self, **kwargs):
        lichs = request.env['lich'].sudo().search([])

        # Tạo danh sách chứa ID của tất cả các bản ghi
        lich_ids = [lich.id for lich in lichs]

        return {'lich_ids': lich_ids}

    @http.route('/create_lich', type='json', auth="none", cors="*")
    def create_lich(self, nhan_vien, buoi, gio_bat_dau, gio_ket_thuc, ghi_chu):
        try:
            lich = request.env['lich']

            new_lich = request.env['lich'].sudo().create({
                'nhan_vien': nhan_vien,  # Đảm bảo nhan_vien là một số hoặc ID của nhân viên
                'buoi': buoi,
                'gio_bat_dau': gio_bat_dau,
                'gio_ket_thuc': gio_ket_thuc,
                'ghi_chu': ghi_chu,
            })

            return {'message': 'Lịch đã được tạo thành công'}
        except Exception as e:
            return {'error': str(e)}

        # {
        #     "jsonpc": "2.0",
        #     "params": {
        #         "nhan_vien": "3",
        #         "buoi": "chieu",
        #         "gio_bat_dau": "2024-04-10 14:00:00",
        #         "gio_ket_thuc": "2024-04-15 14:00:00",
        #         "ghi_chu": "abc"
        #     }
        # }

    @http.route('/update_lich/<int:id>', type='json', auth="none", methods=['POST'], cors="*")
    def update_lich(self, id, nhan_vien=None, buoi=None, gio_bat_dau=None, gio_ket_thuc=None, ghi_chu=None):
        try:
            lich = request.env['lich'].sudo().search([('id', '=', id)], limit=1)
            if not lich:
                return {'error': 'Bản ghi không tồn tại'}

            values = {}
            if nhan_vien is not None:
                # Tìm bản ghi res.partner từ ID
                partner = request.env['res.partner'].sudo().browse(int(nhan_vien))
                if partner:
                    values['nhan_vien'] = partner.id
                else:
                    return {'error': 'Nhân viên không tồn tại'}

            if buoi is not None:
                values['buoi'] = buoi
            if gio_bat_dau is not None:
                values['gio_bat_dau'] = gio_bat_dau
            if gio_ket_thuc is not None:
                values['gio_ket_thuc'] = gio_ket_thuc
            if ghi_chu is not None:
                values['ghi_chu'] = ghi_chu

            lich.sudo().write(values)

            return {'message': 'Bản ghi lịch đã được cập nhật', 'id': lich.id}
        except Exception as e:
            return {'error': str(e)}

        # {
        #     "jsonpc": "2.0",
        #     "params": {
        #         "nhan_vien": "2",
        #         "buoi": "chieu",
        #         "gio_bat_dau": "2024-04-10 14:00:00",
        #         "gio_ket_thuc": "2024-04-15 14:00:00",
        #         "ghi_chu": "abc"
        #     }
        # }

    @http.route('/delete_lich/<int:id>', type='json', auth="none", methods=['DELETE'], cors="*")
    def delete_lich(self, id):
        try:
            lich = request.env['lich'].sudo().search([('id', '=', id)], limit=1)
            if not lich:
                return {'error': 'Bản ghi không tồn tại'}

            lich.sudo().unlink()

            return {'message': 'Bản ghi lịch đã được xóa thành công'}
        except Exception as e:
            return {'error': str(e)}

    # {
    #     "jsonrpc": "2.0",
    #     "params": {
    #         "ma_lich": "100007",
    #         "nhan_vien": "Nam",
    #         "buoi": "sang",
    #         "gio_bat_dau": "04/10/2024 14:00:00",
    #         "gio_ket_thuc": "04/15/2024 14:00:00",
    #         "ghi_chu": "abc"
    #     }
    # }

    @http.route('/get_lich/<int:id>', type='json', auth="none", methods=['GET'], cors="*")
    def get_lich(self, id):
        try:
            lich = request.env['lich'].sudo().search([('id', '=', id)], limit=1)
            if not lich:
                return {'error': 'Bản ghi không tồn tại'}

            lich_data = {
                'id': lich.id,
                'nhan_vien': lich.nhan_vien.name,
                'buoi': lich.buoi,
                'gio_bat_dau': lich.gio_bat_dau,
                'gio_ket_thuc': lich.gio_ket_thuc,
                'ghi_chu': lich.ghi_chu,
            }

            return {'lich': lich_data}
        except Exception as e:
            return {'error': str(e)}



class API(http.Controller):

    @http.route('/get_donxin_id', type="json", auth="none", methods=["GET"], csrf=False)
    def get_all_ids(self, **kwargs):
        donxins = request.env['donxin'].sudo().search([])

        # Tạo danh sách chứa ID của tất cả các bản ghi
        donxin_ids = [donxin.id for donxin in donxins]

        return {'CAC ID HIEN CO': donxin_ids}

    @http.route('/create_donxin', type='json', auth="none")
    def create_donxin(self, ma_nhan_vien, ma_quan_li, loai_don, ngay_bat_dau, ngay_ket_thuc, li_do, tieu_de):
        try:
            donxin = request.env['donxin']

            new_donxin = request.env['donxin'].sudo().create({
                'ma_nhan_vien': ma_nhan_vien,  # Đảm bảo nhan_vien là một số hoặc ID của nhân viên
                'ma_quan_li': ma_quan_li,
                'tieu_de': tieu_de,
                'loai_don': loai_don,
                'ngay_bat_dau': ngay_bat_dau,
                'ngay_ket_thuc': ngay_ket_thuc,
                'li_do': li_do
            })

            return {'message': 'DON XIN đã được tạo thành công'}
        except Exception as e:
            return {'error': str(e)}

    # {
    #     "jsonpc": "2.0",
    #     "params": {
    #         "tieu_de": "ĐƠN XIN",
    #         "ma_nhan_vien": "1",
    #         "ma_quan_li": "2",
    #         "loai_don": "nghi_benh",
    #         "ngay_bat_dau": "2024-04-10 14:00:00",
    #         "ngay_ket_thuc": "2024-04-15 14:00:00",
    #         "li_do": "abc"
    #     }
    # }

    @http.route('/update_donxin/<int:id>', type='json', auth="none", methods=['POST'])
    def update_donxin(self, id, ma_nhan_vien=None, ma_quan_li=None, loai_don=None, ngay_ket_thuc=None, ngay_bat_dau=None, li_do=None, tieu_de=None):
        try:
            donxin = request.env['donxin'].sudo().search([('id', '=', id)], limit=1)
            if not donxin:
                return {'error': 'Bản ghi không tồn tại'}

            values = {}
            if ma_nhan_vien is not None:
                # Tìm bản ghi res.partner từ ID
                partner = request.env['res.partner'].sudo().browse(int(ma_nhan_vien))
                if partner:
                    values['ma_nhan_vien'] = partner.id
                else:
                    return {'error': 'Nhân viên không tồn tại'}
            if ma_quan_li is not None:
                # Tìm bản ghi res.partner từ ID
                partner = request.env['res.partner'].sudo().browse(int(ma_quan_li))
                if partner:
                    values['ma_quan_li'] = partner.id
                else:
                    return {'error': 'Quản lí không tồn tại'}
            if tieu_de is not None:
                values['tieu_de'] = tieu_de
            if loai_don is not None:
                values['loai_don'] = loai_don
            if ngay_bat_dau is not None:
                values['ngay_bat_dau'] = ngay_bat_dau
            if ngay_ket_thuc is not None:
                values['ngay_ket_thuc'] = ngay_ket_thuc
            if li_do is not None:
                values['li_do'] = li_do

            donxin.sudo().write(values)

            return {'message': 'Bản ghi lịch đã được cập nhật', 'id': donxin.id}
        except Exception as e:
            return {'error': str(e)}

    # {
    #     "jsonpc": "2.0",
    #     "params": {
    #         "ma_nhan_vien": "1",
    #         "ma_quan_li": "2",
    #         "loai_don": "nghi_benh",
    #         "ngay_bat_dau": "2024-04-10 14:00:00",
    #         "ngay_ket_thuc": "2024-04-15 14:00:00",
    #         "li_do": "abc"
    #     }
    # }

    @http.route('/delete_donxin/<int:id>', type='json', auth="none", methods=['DELETE'])
    def delete_donxin(self, id):
        try:
            donxin = request.env['donxin'].sudo().search([('id', '=', id)], limit=1)
            if not donxin:
                return {'error': 'Bản ghi không tồn tại'}

            donxin.sudo().unlink()

            return {'message': 'Bản ghi lịch đã được xóa thành công'}
        except Exception as e:
            return {'error': str(e)}

    @http.route('/get_donxin/<int:id>', type='json', auth="none", methods=['GET'])
    def get_donxin(self, id):
        try:
            donxin = request.env['donxin'].sudo().search([('id', '=', id)], limit=1)
            if not donxin:
                return {'error': 'Bản ghi không tồn tại'}

            donxin_data = {
                'id': donxin.id,
                'ma_nhan_vien': donxin.ma_nhan_vien.name,
                'ma_quan_li': donxin.ma_quan_li,
                'loai_don': donxin.loai_don,
                'tieu_de': donxin.tieu_de,
                'ngay_bat_dau': donxin.ngay_bat_dau,
                'ngay_ket_thuc': donxin.ngay_ket_thuc,
                'li_do': donxin.li_do,
            }

            return {'donxin': donxin_data}
        except Exception as e:
            return {'error': str(e)}




class nguoiDung(http.Controller):

    @http.route('/get_nd_id', type="json", auth="none", methods=["GET"], csrf=False)
    def get_all_ids(self, **kwargs):
        nds = request.env['nd'].sudo().search([])

        # Tạo danh sách chứa ID của tất cả các bản ghi
        nd_ids = [nd.id for nd in nds]

        return {'CAC ID HIEN CO': nd_ids}

    @http.route('/create_nd', type='json', auth="none")
    def create_nd(self, ten_nguoi_dung, chuc_vu, bo_phan, ngay_sinh, gioi_tinh, email, sdt, anh):
        try:
            nd = request.env['nd']
            new_nd = request.env['nd'].sudo().create({
                'ten_nguoi_dung': ten_nguoi_dung,  # Đảm bảo nhan_vien là một số hoặc ID của nhân viên
                'chuc_vu': chuc_vu,
                'bo_phan': bo_phan,
                'ngay_sinh': ngay_sinh,
                'gioi_tinh': gioi_tinh,
                'email': email,
                'sdt': sdt,
                # 'anh': anh
            })

            return {'message': 'NGƯỜI DÙNG đã được tạo thành công'}
        except Exception as e:
            return {'error': str(e)}

        # {
        #     "jsonpc": "2.0",
        #     "params": {
        #         "ten_nguoi_dung": "1",
        #         "chuc_vu": "nhan_vien",
        #         "bo_phan": "san_pham",
        #         "ngay_sinh": "2002-04-10",
        #         "gioi_tinh": "nam",
        #         "email": "namn44241@gmail.com",
        #         "sdt": "0966828682"
        #     }
        # }

    @http.route('/update_nd/<int:id>', type='json', auth="none", methods=['POST'])
    def update_nd(self, id, ten_nguoi_dung=None, chuc_vu=None, bo_phan=None, ngay_sinh=None, gioi_tinh=None, email=None, sdt=None, anh=None):
        try:
            nd = request.env['nd'].sudo().search([('id', '=', id)], limit=1)
            if not nd:
                return {'error': 'Bản ghi không tồn tại'}

            values = {}
            if ten_nguoi_dung is not None:
                # Tìm bản ghi res.partner từ ID
                partner = request.env['res.partner'].sudo().browse(int(ten_nguoi_dung))
                if partner:
                    values['ten_nguoi_dung'] = partner.id
                else:
                    return {'error': 'Người dùng không tồn tại'}
            if chuc_vu is not None:
                values['chuc_vu'] = chuc_vu
            if bo_phan is not None:
                values['bo_phan'] = bo_phan
            if ngay_sinh is not None:
                values['ngay_sinh'] = ngay_sinh
            if gioi_tinh is not None:
                values['gioi_tinh'] = gioi_tinh
            if email is not None:
                values['email'] = email
            if sdt is not None:
                values['sdt'] = sdt
            if anh is not None:
                if hasattr(anh, 'read'):
                    # Xử lý ảnh và chuyển đổi thành base64
                    image_base64 = base64.b64encode(anh.read()).decode('utf-8')
                    values['anh'] = image_base64
                else:
                    return {'error': 'Dữ liệu ảnh không hợp lệ'}

            nd.sudo().write(values)

            return {'message': 'Bản ghi đã được cập nhật', 'id': nd.id}
        except Exception as e:
            return {'error': str(e)}

    @http.route('/delete_nd/<int:id>', type='json', auth="none", methods=['DELETE'])
    def delete_nd(self, id):
        try:
            nd = request.env['nd'].sudo().search([('id', '=', id)], limit=1)
            if not nd:
                return {'error': 'Bản ghi không tồn tại'}

            nd.sudo().unlink()

            return {'message': 'Bản ghi đã được xóa thành công'}
        except Exception as e:
            return {'error': str(e)}

    @http.route('/get_nd/<int:id>', type='json', auth="none", methods=['GET'])
    def get_nd(self, id):
        try:
            nd = request.env['nd'].sudo().search([('id', '=', id)], limit=1)
            if not nd:
                return {'error': 'Bản ghi không tồn tại'}

            nd_data = {
                'id': nd.id,
                'ten_nguoi_dung': nd.ten_nguoi_dung.name,
                'chuc_vu': nd.chuc_vu,
                'bo_phan': nd.bo_phan,
                'ngay_sinh': nd.ngay_sinh,
                'gioi_tinh': nd.gioi_tinh,
                'email': nd.email,
                'sdt': nd.sdt,
            }

            return {'nd': nd_data}
        except Exception as e:
            return {'error': str(e)}


class CongViecAPI(http.Controller):

    @http.route('/get_congviec_id', type="json", auth="none", methods=["GET"], csrf=False)
    def get_all_ids(self, **kwargs):
        congviecs = request.env['congviec'].sudo().search([])

        # Tạo danh sách chứa ID của tất cả các bản ghi
        congviec_ids = [congviec.id for congviec in congviecs]

        return {'congviec_ids': congviec_ids}

    @http.route('/create_congviec', type='json', auth="none", methods=["POST"])
    def create_congviec(self, **post):
        try:
            # Tạo mới một bản ghi Công Việc từ dữ liệu gửi qua POST
            new_congviec = request.env['congviec'].sudo().create(post)
            return {'message': 'Công việc đã được tạo thành công'}
        except ValidationError as e:
            return {'error': str(e)}

    @http.route('/update_congviec/<int:id>', type='json', auth="none", methods=['POST'])
    def update_congviec(self, id, **post):
        try:
            # Tìm và cập nhật bản ghi Công Việc từ dữ liệu gửi qua POST
            congviec = request.env['congviec'].sudo().search([('id', '=', id)], limit=1)
            if not congviec:
                return {'error': 'Bản ghi không tồn tại'}
            congviec.sudo().write(post)
            return {'message': 'Bản ghi công việc đã được cập nhật', 'id': congviec.id}
        except ValidationError as e:
            return {'error': str(e)}

    @http.route('/delete_congviec/<int:id>', type='json', auth="none", methods=['DELETE'])
    def delete_congviec(self, id):
        try:
            # Xóa bản ghi Công Việc
            congviec = request.env['congviec'].sudo().search([('id', '=', id)], limit=1)
            if not congviec:
                return {'error': 'Bản ghi không tồn tại'}
            congviec.sudo().unlink()
            return {'message': 'Bản ghi công việc đã được xóa thành công'}
        except ValidationError as e:
            return {'error': str(e)}

    @http.route('/get_congviec/<int:id>', type='json', auth="none", methods=['GET'])
    def get_congviec(self, id):
        try:
            # Lấy thông tin chi tiết của một bản ghi Công Việc dựa trên ID
            congviec = request.env['congviec'].sudo().search([('id', '=', id)], limit=1)
            if not congviec:
                return {'error': 'Bản ghi không tồn tại'}
            congviec_data = {
                'id': congviec.id,
                'ten_cong_viec': congviec.ten_cong_viec,
                'mota': congviec.mota,
                'thoi_han': congviec.thoi_han,
                'trang_thai': congviec.trang_thai,
                'ma_quan_li': congviec.ma_quan_li.name,
            }
            return {'congviec': congviec_data}
        except ValidationError as e:
            return {'error': str(e)}
