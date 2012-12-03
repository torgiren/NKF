# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import redirect
def back(request):
	if request.session['return_page']:
		ret=redirect(request.session['return_page'])
		del request.session['return_page']
		return ret
	else:
		return redirect('/')
