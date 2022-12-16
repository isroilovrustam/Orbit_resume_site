from django.shortcuts import render, redirect
from .models import Home, About, Degree, Portfolio, Category, Service, Happy_Client, Medium, Work, Education
from contact.forms import ContactForm
from contact.models import ContactMe
# Create your views here.


def index_view(request):
    object_home = Home.objects.all()
    object_about = About.objects.all()
    object_degree = Degree.objects.all()
    object_portfolio = Portfolio.objects.all()
    object_category = Category.objects.all()
    object_service = Service.objects.all()
    object_heppy = Happy_Client.objects.all()
    object_medium = Medium.objects.all()
    object_work = Work.objects.all()
    object_education = Education.objects.all()
    cat = request.GET.get("cat")
    if cat:
        object_portfolio = object_portfolio.filter(category__name__iexact=cat)
    form = ContactForm(request.POST or None)
    object_contactme = ContactMe.objects.all()
    if form.is_valid():
        form.save()
        return redirect("/#contact-section")

    context = {
        'homes': object_home,
        'abouts': object_about,
        'degrees': object_degree,
        'portfolios': object_portfolio,
        'categorys': object_category,
        'services': object_service,
        'happys': object_heppy,
        'mediums': object_medium,
        'works': object_work,
        'educations': object_education,
        'form': form,
        'contactmes': object_contactme
    }

    return render(request, 'index.html', context)