from django.shortcuts import render, get_object_or_404

from apps.models import ContactModel


# from apps.models import Film


# Create your views here.

def index_view(request):
    # films = Film.objects.all().order_by('id')
    # context = {
    #     'films': films
    # }
    # if context = database table if/else -> url not working
    return render(request, 'apps/index.html')


# def detail_view(request, film_id):  # Add film_id as a parameter
#     film = get_object_or_404(Film, pk=film_id)
#     context = {
#         'film': film
#     }
#     return render(request, 'apps/detail.html', context)


def exam_view(request):
    contacts = ContactModel.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'apps/exam.html', context)


def exam_detail_view(request, id):
    contact = get_object_or_404(ContactModel, pk=id)
    context = {
        'contact': contact
    }
    return render(request, 'apps/exam_detail.html', context)
