# Create your views here.
from django.http import HttpResponse
from books.models import Books
#from django.template import Context, loader     
def index(request):
	books_list = Books.objects.all()
	output = ','.join([b.title for b in books_list])
	return HttpResponse(output)
    

	
      

     
    