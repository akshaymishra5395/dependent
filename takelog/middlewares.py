
class CheckMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response= self.get_response(request)
        print('bbbyyyyyyyyyy')
        return response
    
    def process_view(self,request,view_func,*view_args,**view_kwargs):
        print('hii')
        pass

    def process_exception(self,request,exception):
        
        pass

    def process_template_response(self,request,response):
        print('bye')
        pass


