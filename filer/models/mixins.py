#-*- coding: utf-8 -*-
from filer.settings import FILER_ADMIN_ICON_SIZES, FILER_STATICMEDIA_PREFIX, FILER_EXTENSION_BASED_ICONS


class IconsMixin(object):
    """
    Can be used on any model that has a _icon attribute. will return a dict
    containing urls for icons of different sizes with that name.
    """
    @property
    def icons(self):
        r = {}
        if getattr(self, '_icon', False):
            for size in FILER_ADMIN_ICON_SIZES:
                icon = self.extension if FILER_EXTENSION_BASED_ICONS else self._icon
                r[size] = "%sicons/%s_%sx%s.png" % (
                            FILER_STATICMEDIA_PREFIX, icon, size, size)
        return r
