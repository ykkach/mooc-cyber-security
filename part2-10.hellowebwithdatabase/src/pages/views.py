from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):

	message_id = request.GET.get('id')
	message = Message.objects.get(id=message_id)
	content = message.content
	return HttpResponse(content)
