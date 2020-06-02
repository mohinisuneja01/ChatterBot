from django.shortcuts import render
from django.http import HttpResponse
#from django.conf.urls.static import static
import json
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvio')
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")



# Train based on the english corpus

#Already trained and it's supposed to be persistent

#trainer.export_for_training('/static/intents.json')


@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request):
	context = {'title': 'Chatbot Version 1.0'}
	return render(request,"home.html", context)

def home1(request):
	context = {'title': 'Chatbot Version 1.0'}
	return render(request,"home1.html")
