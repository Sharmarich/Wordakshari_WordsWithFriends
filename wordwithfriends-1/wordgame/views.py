from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import UserInfoForm

#import enchant

# Create your views here.


def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username').lower()
		password = request.POST.get('password')

		# Check if user exists
		try:
			user = User.objects.get(username=username)
		except Exception:
			messages.error(request,'user not found')

		user = authenticate(request,username=username,password=password)

		if user:
			login(request,user)
			return redirect('home')
		else:
			messages.error(request,'username or password is incorrect')

	context = {}
	return render(request,'wordgame/login.html',context)

def logout_user(request):
	logout(request)
	return redirect('home')

def signup_user(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()

			info = UserInfo(host=user)
			info.save()
			
			login(request,user)
			return redirect('home')

		else:
			messages.error(request,'Error occurred during registration')

	context = {'form':form}
	return render(request,'wordgame/signup.html',context)

def edit_user(request):
	form = UserInfoForm()
	if request.method == 'POST':
		pass
	context = {'form':form}
	return render(request,'/base/user_edit.html',context)

def home_page(request):
	context = {"title":"home"}
	return render(request,"wordgame/home.html",context)

def create_room(request):
	room = Room(host=request.user)
	room.save()
	roomId = room.id
	return redirect(f'/room/{roomId}')

def get_room_info(request,roomId):
	room = Room.objects.filter(id = roomId).first()
	data = {
		'roomId':roomId,
		'turn':room.turn,
		'host':room.host.username,
		'opponent':room.opponent,
		'lastChar':room.word[-1],
		'is_over':room.is_over
	}
	return JsonResponse(data)

def room_page(request,roomId):
	user = request.user
	context = {"title":"room","roomId":roomId,"round_number":5}	
	room = Room.objects.filter(id = roomId).first()
	context.update({'host':room.host})

	if request.method == 'POST':
		ans = request.POST.get('answer').upper()
		# d = enchant.Dict("en_US")
		# ansValid = d.check(ans)
		ansValid = True
		if ansValid:
			info =  UserInfo.objects.filter(host=user).first()
			info.words_solved += 1
			info.level = (info.words_solved // 50) or info.level
			info.save()

		room.turn = room.host.username if (room.turn == room.opponent) else room.opponent
		room.word = ans
		room.save()
		
	if room is None:
		messages.success(request,'request')
		return redirect('home')

	if room.is_over:
		messages.success(request , "Game is over")
		return redirect('home')

	if room.host != user:
		if room.opponent is None:
			room.opponent = user.username
			room.turn = user.username
			room.save(force_update=True)
		else:
			print('you are a visitor')
			
	context.update({
		'opponent':room.opponent,
		'turn':room.turn,
		'roomId':roomId,
		})

	return render(request,"wordgame/room.html",context)

def receive_answer(request):
	
	return redirect('room')

def giveup(request,roomId):
	room = Room.objects.filter(id = roomId).first()

	if room is not None:
		if (request.user.username == room.host.username) or (request.user.username == room.opponent):
			room.is_over = True
			room.save()
			return redirect('home')
	return redirect(f"room/{{roomId}}")

def user_page(request,username):
	# Check if user exists
	try:
		user = User.objects.get(username=username)
		info = UserInfo.objects.filter(host=user).first()
	except Exception:
		messages.error(request,'user not found')
	context = {"user":user,"info":info}
	return render(request,'wordgame/user.html',context)

def available_rooms(request):
	# Check if user exist
	rooms = Room.objects.filter(opponent=None)
	context = {"rooms":rooms}
	return render(request,'wordgame/rooms.html',context)

def get_leaderboards(request):
	# Check if user exist
	users = UserInfo.objects.order_by('words_solved')[:10:-1]
	context = {"users":users}
	return render(request,'wordgame/leaderboards.html',context)