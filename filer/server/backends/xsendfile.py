#-*- coding: utf-8 -*-
from django.http import HttpResponse
from filer.server.backends.base import ServerBase


class ApacheXSendfileServer(ServerBase):
    def serve(self, request, file, **kwargs):
        response = HttpResponse()
        response['X-Sendfile'] = file.path

	# This is needed for lighttpd, hopefully this will 
        # not be needed after this is fixed:
	# http://redmine.lighttpd.net/issues/2076
        response['Content-Type'] = self.get_mimetype(file.path)

        self.default_headers(request=request, response=response, file=file, **kwargs)
        return response

