from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from mafia.models import Candidate
from django.utils import timezone
import random
from django.utils.safestring import mark_safe
import json

checkVic_cnt = 0
select = 5
cnt = 0 # 버튼 클릭 했을 때 사용
comein_cnt = 0 # 직업 나눠줄 때 사용
mafia_num = random.randint(1,5)

# Create your views here.
def register(request):
	global comein_cnt
	comein_cnt = comein_cnt + 1
	if comein_cnt == mafia_num:
		job = "mafia"
	else:
		job = "citizen"
	print(comein_cnt, mafia_num)

	candidates = Candidate.objects.all()
	context = {'candidates':candidates, 'job':job}
	return render(request, 'mafia/register.html', context)


def regConMafia(request):
	name = request.POST['name']
	job_post = request.POST['job']
	votes = request.POST['votes']
	life = request.POST['life']
	img = request.POST['img']
	qs = Candidate(name=name, job=job_post, votes=votes, life=life, img=img)
	qs.save()
	return HttpResponseRedirect(reverse('mafia:room'))

#게임 대기 화면
def waitingRoom(request):

	candidates = Candidate.objects.all()
	context = {'candidates':candidates}

	return render(request, 'mafia/waitingRoom.html', context)
	#context안에 있는 후보 정보를 waitingRoom.html로 전달

#게임 화면
def game(request):
	candidates = Candidate.objects.all()
	context = {'candidates':candidates}

	# 득표수 초기화
	for i in candidates:
		i.votes = 0
		i.life = True
		i.save()

	return render(request, 'mafia/gameRoom.html', context)

# 투표 버튼 누를때 마다 이벤트 발생
def polls(request):
	global checkVic_cnt
	flag = 0
	global cnt
	global select
	cnt = cnt + 1
	# poll = Poll.objects.get(pk = poll_id)#Poll객체를 구분하는 녀석은 poll_id이므로 PK지정
	selection = request.POST['choice']
	candi = Candidate.objects.get(pk = selection)

	candi.votes += 1 #투표수 증가
	candi.save()

	#다시 첫 화면으로 돌아옴
	candidates = Candidate.objects.all()
	context = {'candidates':candidates}
	#context에 모든 어린이 정보를 저장
	print("!!!", cnt, select)
	if cnt == select:
		max = 0
		who = 'name'
		for i in candidates:
			if i.life == True:
				if max < i.votes:
					max = i.votes
					who = i.name
				while True:
					if(who == i.name):
						i.life = False
						i.save()
						print(cnt, select)
						select = select - 1
						cnt = 0
						flag = 1
						break
				if flag == 1:
					flag = 0
					break;
			else:
				continue
	for i in candidates:
		if i.job == 'mafia' and i.life == False:
			return render(request, 'mafia/vic_citizen.html', context)
	if select == 2:
		return render(request, 'mafia/vic_mafia.html', context)

	context = {'candidates': candidates, 'checkVic_cnt': checkVic_cnt}
	return render(request, 'mafia/gameRoom.html', context)
# return을 하지 않으면 화면이 바뀌지 않고, 득표수만 증가한다
# return HttpResponse("finish")


def index(request):
	return render(request, 'mafia/index.html', {})


def chat(request, room_name):
	return render(request, 'mafia/chat.html', {
		'room_name_json': mark_safe(json.dumps(room_name))
	})

def vic_mafia(request):
	return render(request, 'mafia/vic_mafia.html')

def vic_citizen(request):
	return render(request, 'mafia/vic_citizen.html')