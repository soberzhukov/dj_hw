from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    bk = Book.objects.all()
    context = {
        'books': bk
    }
    return render(request, template, context)


def pub_date(request, year, month, day):
    template = 'books/pagin.html'

    date_const = f'{year}-{month}-{day}'

    contact_list = list(Book.objects.order_by('pub_date'))
    p = Paginator(contact_list, 1)
    previous_date, next_date = '', ''

    try:
        bk = Book.objects.filter(pub_date=date_const)

        if bk[0] in contact_list:
            index_now = contact_list.index(bk[0])
            p_number = p.get_page(index_now+1)

            if p_number.has_previous():
                previous_date = contact_list[p_number.previous_page_number()-1].slag_date()

            if p_number.has_next():
                next_date = contact_list[p_number.next_page_number()-1].slag_date()

            context = {
                'p_number': p_number,
                'previous_date': previous_date,
                'next_date': next_date,

            }
            return render(request, template, context)

    except Exception:
        raise Http404('Неверный формат')


