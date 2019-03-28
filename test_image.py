from odoo.tools import image, base64
from odoo.modules import get_module_resource

image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
img = image.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))


resized_image = image.image_resize_image(base64_source=img, size=(500, 500))
'''
@api.depends('partner_id', 'partner_id.image')
def _compute_logo_web(self):
    for company in self:
        company.logo_web = tools.image_resize_image(company.partner_id.image, (180, None))
'''

image.image_resize_images(vals={'some_fields': 1234}, sizes={'image': (1024, None)})
'''
    Update ``vals`` with image fields resized as expected.

@api.model_create_multi
def create(self, vals_list):
    for vals in vals_list:
        tools.image_resize_images(vals)
    return super(FleetVehicleModelBrand, self).create(vals_list)
'''
image.image_resize_and_sharpen(image=img, size=(500, 500))

image.image_get_resized_images(base64_source=img)

image.image_data_uri(base64_source=img)
#   <img t-if="company.logo" t-att-src="image_data_uri(company.logo)" style="max-height: 45px;" alt="Logo"/>

image.image_save_for_web(img)
""" Save image optimized for web usage. """
