from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    if request.session.get('user') != None:
        del request.session['user']
    return render(request,'home.html')


def room(request, pk):
    rooms = Room.objects.get(name=pk)
    username = request.GET.get('username')
    request.session.get('user')
    object_user =  Dict_user.objects.filter(container__name=rooms.name)
    if username == '':
        return redirect('home')

    if request.session.get('user') == None:
        return HttpResponse('SSS')

    if request.session.get('user') != username:
        return redirect('home')



    context = {'rooms':rooms,'username':username,}
    return render(request, 'room.html',context)


def checkview(request):
    if request.method == 'POST':
        room = request.POST.get('room_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        flag_register = 0
        request.session['user'] = username
        if room == '' or username == '':
            return HttpResponse('You didnt send anything')


        object_user = Dict_user.objects.filter(container__name=room)
        if object_user.count() > 0:

            for i in object_user:

                if i.key == username:
                    if i.value == password:
                        return redirect('/' + room + '/?username=' + username)

                    else:
                        return HttpResponse('YOR pass not correct')
                else:
                    flag_register = 1
        else:
            try:
                Dict_user.objects.create(key=username, value=password, container=Room.objects.get(name=room))
            except ObjectDoesNotExist:
                Room.objects.create(name=room)
                Dict_user.objects.create(key=username, value=password, container=Room.objects.get(name=room))

        if flag_register == 1:
            Dict_user.objects.create(key=username, value=password, container=Room.objects.get(name=room))






        return redirect('/' + room + '/?username=' + username)



def send(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        print(1234)
        if message == "":
            return HttpResponse('Message sent Folse')

        username = request.POST.get('username')
        room_id = request.POST.get('room_id')

        new_message = Message.objects.create(value=message,user=username, room=room_id)
        new_message.save()

        return HttpResponse('Message sent true')



def getMessages(request ,pk):
    room_details = Room.objects.get(name=pk)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages":list(messages.values())})


def delete_html(request,id=22):

    message = Message.objects.get(id=id)
    username = request.GET.get('username')

    if request.session.get('user') != username:
        return redirect('home')

    context = {'message': message}

    if message.user != username:
        return HttpResponse('Ты не можешь это удалить!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')


    return render(request,'delete.html',context)



