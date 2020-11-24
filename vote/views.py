from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contestants, Voters

# Create your views here.
voteOn = 'true' # 'None' #'False'

def login(request):
    if request.method == 'POST':
        mail = request.POST['Pemail']
        if Voters.objects.filter(email=mail).exists():
            # create session for login user
            request.session.get('Vemail', '')
            request.session['Vemail'] = mail
            
            voter = Voters.objects.get(email=mail)
            if voter.voted == True:
                return redirect('success')
            return redirect('vote')
        else:
            messages.info(request, "You are not Eligible to vote")
            return redirect('login')
    else:
        # delete user session
        try:
            del request.session['Vemail']
        except KeyError: pass
        return render(request, 'login.html')

def vote(request):
    vmail = request.session.get('Vemail')
    if vmail == None:
        return redirect('login')
    else:
        if request.method == 'POST':
            cast = request.POST['votee']
            voter =  Voters.objects.get(email=vmail)# vmail
            
            print(f'{voter} --> {cast}')
            voter.vote = cast
            voter.voted = True
            voter.save()
            return redirect('success')
        else:
            contestants = Contestants.objects.all()
            return render(request, 'vote.html', {'contestants': contestants})

def success(request):
    vmail = request.session.get('Vemail')
    if vmail == None:
        return redirect('vote')
    else:
        # delete user session
        try: del request.session['Vemail']
        except KeyError: pass
    return render(request, 'success.html')


def stats(request):
    contestants = Contestants.objects.all()
    count = Voters.objects.all().count()
    
    return render(request, 'scores.html', {'voting':voteOn, 'contestants': contestants, 'total': count})
