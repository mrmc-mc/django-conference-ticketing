from django.shortcuts import render , redirect , HttpResponse , get_object_or_404
from django.views import View
from . import models, forms
import time,random


class Index(View):

    def get(self, request):
        # messages.error(request, 'اطلاعات وارد شده اشتباه است')
        capacity = 200 - models.Ticket.objects.all().count()
        greeting = {}
        greeting['aud'] = capacity
        greeting['title'] = "خانه"
        return render(request, 'ticket/index.html', greeting)



class Result(View):

    def get(self, request):
        qs = models.Ticket.objects.all()
        greeting = {}
        greeting['person'] = qs
        greeting['title'] = "نتایج"
        return render(request, 'ticket/result.html', greeting)



class Register(View):

    def get(self, request):
        greeting = {}
        greeting['title'] = "ثبت نام"
        return render(request, 'ticket/register.html', greeting)


    def post(self, request):
            greeting = {}
            form = forms.TicketForm(request.POST)
            try:
                if form.is_valid:
                    if models.Ticket.objects.all().count() <200:
                        try:
                            
                            form.save(commit=False)
                            number_ticket = str(int(time.time())+models.Ticket.objects.all().count())[5:]
                            print(request.POST.get('submited'))
                            form.instance.invitecode  = number_ticket
                            form.save()

                            greeting['message']='ای جان! اطلاعاتت رو ثبت کردیم. توی سالن جرجانی چشم انتظارتیم 👀'
                            greeting['ticket']=number_ticket

                        except:
                            greeting['message']='نچ! نچ! اطلاعاتی که دادی اشتباهه عزیزم'

                        return render(request, 'ticket/message.html', greeting)

                    greeting['message']='آخی , دیر رسیدی ظرفیت تموم شد 🤤'    
                    return render(request, 'ticket/message.html', greeting)
                
            except:
                greeting['message']='خطایی پیش اومده. به پشتیبانی پیام بده ببینم چی شده'
                return render(request, 'ticket/message.html', greeting)
