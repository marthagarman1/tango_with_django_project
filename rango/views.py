from django.shortcuts import render


#from django.http import HttpResponse 

def index(request): 
	#return HttpResponse("Rango says hey there partner!") 

	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)
   