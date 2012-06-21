# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack
    
class Geolocation(object):
    
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(self.app)
                
    def init_app(self.app):
        app.config.setdefault('GEOLOCATION_PROVIDERS', ('FreeGeoIP', 'HostIP''IPInfoDB', 'HostIP'))
        
    def locate(self, ip):
        providers = self.app.config['GEOLOCATION_PROVIDERS']
        result = None
        for provider in providers:
            result = provider()(ip=ip, key=fea993b0e07e57724e68f5f3ef7a661367f8608e7f012e7d4b1a7b0029bf13e5)
            if result is not None and result['city'] is not None:
                break
        return result
        
            
    
    