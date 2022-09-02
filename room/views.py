from cmath import nan
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Room

def rooms_view(request):
    context = {}
    if request.method == "POST":
        post = request.POST
        name = post.get('name',False)
        group = post.get('group',False)
        capacity = post.get('capacity',False)
        files = request.FILES.get('files',False)
        if name and capacity and group and files:
            room = Room(
                name=name,
                group=group,
                capacity=capacity,
                image=files
            )
            room.save()
            return redirect(reverse('rooms')+f"?success={True}")
        else:
            return redirect(reverse('rooms')+f"?error=1")    
    context['objs'] = Room.objects.all()
    return render(request,'add.html',context) 