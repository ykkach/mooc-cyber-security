from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import questions

def find_topic(tid):
	for q in questions:
		if q['id'] == tid:
			return q
	return None


def quizView(request, tid):
	topic = find_topic(tid)

	if 'level' in request.session:
		return redirect('/cheater/')

	request.session['level'] = 0
	return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][0]})



def answerView(request, tid, aid):
		
	topic = find_topic(tid)

	if 'level' in request.session:
		return redirect('/cheater/')

	level = request.session['level']

	if level != request.session.get('current_question', 0):
		return redirect('/cheater/')

	if topic['questions'][level]['correct'] == aid:
		level += 1
		request.session['level'] = level
		request.session['current_question'] = level

		if level == len(topic['questions']):
			return redirect('/finish/')

		return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][level]})
	else:
		return redirect('/incorrect/')


def incorrectView(request):
	return render(request, 'pages/incorrect.html')


def finishView(request):
	if 'level' not in request.session:
		return redirect('/cheater/')

	questions = request.session.get('questions')
	if questions and len(questions) == request.session['level']:
		message = "Awesome! You beat the game!"
	else:
		message = ""
	return render(request, 'pages/finish.html', {'message': message})


def cheaterView(request):
	return render(request, 'pages/cheater.html')


@login_required
def thanksView(request):
	# Like we were going to pay anyone
	return render(request, 'pages/thanks.html')



def topicView(request, tid):
	topic = find_topic(tid)
	return render(request, 'pages/topic.html', {'topic' : topic})


def topicsView(request):
	return render(request, 'pages/topics.html', {'questions' : questions})
