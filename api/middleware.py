from typing import Any


class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('one time initilization')
    def __call__(self,request):
        print('before view called')
        resp = self.get_response(request)
        print('after view called')
        return resp