import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from quotes.models import Author, Quote
from faker import Faker
import CSV_Archive

f_quotes = CSV_Archive.CSV_Archive('raw_data.csv', 'A', ('name', 'A'), ('text', 'U'))
quotes_list = f_quotes.search(('name','text'))

fakegen = Faker()
def add_user(quotes_list):

    for name, text in quotes_list:
        t = Author.objects.get_or_create(name=name)[0]
        print(t.slug)
        t.save()
        q = Quote.objects.get_or_create(text=text)[0]
        q.author = author=Author(id=t.id)
        q.save()






add_user(quotes_list)
