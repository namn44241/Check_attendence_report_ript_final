import odoo
import json
import logging
from odoo import http
from odoo.http import request

class GetIdPet(http.Controller):
    @http.route('/api/get_all_pet_ids/', type="json", auth="none", methods=["GET"], csrf=False)
    def get_all_pet_ids(self, **kwargs):
        # Lấy tất cả các pet từ hệ thống Odoo
        pets = request.env['my.pet'].sudo().search([])

        # Tạo danh sách chứa ID của tất cả các pet
        pet_ids = [pet.id for pet in pets]

        return {'pet_ids': pet_ids}
class MyPetPart(http.Controller):
    @http.route('/api/auth1/', type="json", auth="none", methods=["GET"], csrf=False)
    def get_session(self, *args, **kwargs):
        # your auth code here
        data = json.loads(request.httprequest.data)

        # Kiểm tra xem pet_id đã được truyền hay chưa
        if 'pet_id' not in data:
            return {'error': 'Pet ID is missing'}
            # Lấy pet dựa trên pet_id
        pet = request.env['my.pet'].sudo().browse(int(data['pet_id']))
        list_key = ['name', 'nickname', 'description']
        #cần thuộc tính gì thì nhập vào list_key
        list_json = []
        for hop_dong in pet:
            json_data = {}
            for key in list_key:
                json_data[key] = hop_dong[key]
            list_json.append(json_data)
        return list_json

class MyNewPet(http.Controller):
    @http.route('/api/create_pet/', type="json", auth="none", methods=["POST"], csrf=False)
    def create_pet(self, **post):
        try:
            # Lấy thông tin từ yêu cầu POST
            pet_info = json.loads(request.httprequest.data)
            if not pet_info:
                return {'error': 'Pet information is missing'}

            # Tạo một con pet mới
            new_pet = request.env['my.pet'].sudo().create({
                # 'pet_id': pet_info.get('id'),
                'name': pet_info.get('name'),
                'nickname': pet_info.get('nickname'),
                'description': pet_info.get('description')
            })

            # Trả về thông tin về con pet mới
            return {
                'success': True,
                # 'pet_id': new_pet.id,
                'name': new_pet.name,
                'nickname': new_pet.nickname,
                'description': new_pet.description
            }
        except Exception as e:
            return {'error': str(e)}

class MyPetDeletion(http.Controller):
    @http.route('/api/delete_pet/', type="json", auth="none", methods=["DELETE"], csrf=False)
    def xoa_pet(self, **kwargs):
        # Lấy thông tin từ yêu cầu POST
        data = json.loads(request.httprequest.data)

        # Kiểm tra xem pet_id đã được truyền hay chưa
        if 'pet_id' not in data:
            return {'error': 'Pet ID is missing'}
        # Lấy pet dựa trên pet_id
        pet = request.env['my.pet'].sudo().browse(int(data['pet_id']))
        pet.unlink()
        return {"success": "Pet has been deleted"}

class MyPetUpdateFull(http.Controller):
    @http.route('/api/update_all_pets/', type="json", auth="none", methods=["POST"], csrf=False)
    def update_all_pets(self, *args, **kwargs):
        # Lấy tất cả các bản ghi từ mô hình 'my.pet'
        pets = request.env['my.pet'].sudo().search([])

        # Cập nhật trường 'weight' của tất cả các bản ghi thành 200kg
        for pet in pets:
            pet.write({'weight': 200})  # Thay đổi giá trị 'weight' thành 200kg
        return {'message': 'All pets updated successfully'}

    class MyPetPart(http.Controller):
        @http.route('/api/update_pet_info/', type="json", auth="none", methods=["POST"], csrf=False)
        def update_pet_info(self, **kwargs):
            # Lấy thông tin từ yêu cầu POST
            data = json.loads(request.httprequest.data)

            # Kiểm tra xem pet_id đã được truyền hay chưa
            if 'pet_id' not in data:
                return {'error': 'Pet ID is missing'}

            # Lấy pet dựa trên pet_id
            pet = request.env['my.pet'].sudo().browse(int(data['pet_id']))
            if not pet:
                return {'error': 'Pet not found'}

            # Tạo một từ điển chứa thông tin mới muốn cập nhật
            new_data = {}
            if 'name' in data:
                new_data['name'] = data['name']
            if 'nickname' in data:
                new_data['nickname'] = data['nickname']
            if 'description' in data:
                new_data['description'] = data['description']

            # Cập nhật thông tin của pet
            pet.write(new_data)

            return {'message': 'Pet information updated successfully'}


class MyPetFull(http.Controller):
    @http.route('/api/auth/', type="json", auth="none", methods=["POST"], csrf=False)
    def get_session(self, *args, **kwargs):
        # your auth code here
        hop_dong_ids = request.env['my.pet'].sudo().search([])
        list_key = ['name', 'nickname', 'description', 'age', 'weight', 'dob', 'gender']

        list_json = []
        for hop_dong in hop_dong_ids:
            json_data = {}
            for key in list_key:
                json_data[key] = hop_dong[key]
            list_json.append(json_data)
        return list_json

_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return "Welcome to 'foo' API!"

    @odoo.http.route('/bar', auth='public')
    def bar_handler(self):
        return json.dumps({
            "content": "Welcome to 'bar' API!"
        })
    # @odoo.http.route(['/pet/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    # # @odoo.http.route(['/pet'], type='json, auth="none", sitemap=False, cors='*', csrf=False)
    # def pet_handler(self, dbname, id, **kw):
    #     model_name = "my.pet"
    #     try:
    #         registry = odoo.modules.registry.Registry(dbname)
    #         with odoo.api.Environment.manage(), registry.cursor() as cr:
    #             env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
    #             rec = env[model_name].search([('id', '=', int(id))], limit=1)
    #             response = {
    #                 "status": "ok",
    #                 "content": {
    #                     "name": rec.name,
    #                     "nickname": rec.nickname,
    #                     "description": rec.description,
    #                     "age": rec.age,
    #                     "weight": rec.weight,
    #                     "dob": rec.dob.strftime('%d/%m/%Y'),
    #                     "gender": rec.gender,
    #                 }
    #             }
    #     except Exception:
    #         response = {
    #             "status": "error",
    #             "content": "not found"
    #         }
    #     print(response)
    #     return json.dumps(response)

