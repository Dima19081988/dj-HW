from django.shortcuts import render, get_list_or_404
from datetime import datetime
from django.http import Http404
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date', 'id')
    context = {
        'books': books,
        'current_date': None,
        'prev_date': None,
        'next_date': None,
    }
    return render(request, template, context)

def books_by_date(request, pub_date):
    template = 'books/books_list.html'

    try:
        current_date = datetime.strptime(pub_date, '%Y-%m-%d').date()
    except:
        raise Http404('Неверный формат даты')

    books = get_list_or_404(Book.objects.order_by('id'), pub_date=current_date)

    prev_dates = Book.objects.filter(pub_date__lt = current_date)\
                             .order_by('-pub_date')\
                             .values_list('pub_date', flat=True)\
                             .distinct('pub_date')
    prev_date = prev_dates[0] if prev_dates else None

    next_dates = Book.objects.filter(pub_date__gt = current_date)\
                             .order_by('pub_date')\
                             .values_list('pub_date', flat=True)\
                             .distinct('pub_date')
    next_date = next_dates[0] if next_dates else None

    context = {
	    'books': books,
	    'current_date': current_date,
	    'prev_date': prev_date,
	    'next_date': next_date
    }
    return render(request, template, context)