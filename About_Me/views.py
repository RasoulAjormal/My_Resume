from re import match

from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from About_Me.models import User, ContactModel, WorkSamples, WorkSampleCategory, Certificate, CertificateCategory, \
    Visit, WorkSampleGallery
# Create your views here.
from About_Me.templates.get_client_ip import get_client_ip


class AboutMeView(ListView):
    template_name = 'Home-Page/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data()
        request: HttpRequest = self.request
        if User.objects.filter(is_active=True).exists():
            user_id = User.objects.filter(is_active=True).first()
            context['about_me'] = User.objects.prefetch_related('skill_set',
                                                                'jobtitles_set',
                                                                'education_set',
                                                                'experiences_set',
                                                                'experiences_set__description_set',
                                                                'contactmodel_set',
                                                                'commentsofothersmodel_set').filter(
                is_active=True).first()

            context['work_samples'] = WorkSamples.objects.prefetch_related('Category').filter(Is_Active=True,
                                                                                              user=user_id)
            context['work_sample_categories'] = WorkSampleCategory.objects.filter(worksamples__Is_Active=True,
                                                                                  worksamples__user=user_id).distinct()
            context['certificates'] = Certificate.objects.prefetch_related('CertificateCategory').filter(Is_Active=True,
                                                                                              user=user_id)
            context['certificate_categories'] = CertificateCategory.objects.filter(certificate__Is_Active=True,
                                                                                   certificate__user=user_id).distinct()

            ip = get_client_ip(request)
            if not Visit.objects.filter(ip__iexact=ip).exists():
                new_visit = Visit(ip=ip)
                new_visit.save()
            return context
        else:
            raise Exception('this site is empty')


def portfolio_details(request, portfolio_id):
    work_sample = WorkSamples.objects.filter(id=portfolio_id).first()
    work_samples_gallery = WorkSampleGallery.objects.filter(WorkSample=portfolio_id)
    return render(request, 'Home-Page/portfolio-details.html',
                  {'work_sample': work_sample, 'galleries': work_samples_gallery})

def Add_Message(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    subject = request.GET.get('subject')
    message = request.GET.get('message')

    if not match(r"^[a-zA-Z][\.a-zA-Z1-9]+@[a-zA-Z]+\.[a-zA-Z]{3}$", email):
        return JsonResponse({'status': 'Email_Error'})
    if not len(message) > 500 and len(message) < 10:
        return JsonResponse({'status': 'Message_Error'})
    if len(name) > 50 or len(name) < 3:
        return JsonResponse({'status': 'Name_Error'})
    if len(subject) > 50 or len(subject) < 3:
        return JsonResponse({'status': 'Subject_Error'})
    admin_id = User.objects.filter(is_active=True).first().id
    new_message = ContactModel(FullName=name, EmailAddress=email, Subject=subject, Message=message, user_id=admin_id)
    new_message.save()
    return JsonResponse({'status': 'success'})
