# app_name/wagtail_hooks.py

from wagtail.contrib.modeladmin.helpers import ButtonHelper
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.views import CreateView

from .models import Coupon

class CouponButtonHelper(ButtonHelper):
    # Define a custom button helper to add a "Create Coupon" button
    def get_buttons_for_obj(self, obj, exclude=None, classnames_add=None, classnames_exclude=None):
        buttons = super().get_buttons_for_obj(obj, exclude, classnames_add, classnames_exclude)
        url = self.url_helper.get_action_url('add', instance=obj)
        buttons.append({
            'url': url,
            'label': 'Create Coupon',
            'classname': 'button button-small button-positive',
            'title': 'Create a new coupon for this store',
        })
        return buttons

class CouponModelAdmin(ModelAdmin):
    model = Coupon
    menu_label = 'Coupon Administration'
    menu_icon = 'upload'
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = ['date', 'intro', 'store_link', 'category']
    button_helper_class = CouponButtonHelper  # Use the custom button helper

modeladmin_register(CouponModelAdmin)
