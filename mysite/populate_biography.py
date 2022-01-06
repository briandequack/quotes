import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from quotes.models import Author, Quote
from slugify import slugify
import wikipedia

wiki_data =  wikipedia.page("alberteinstein")
wiki_content = wiki_data.content
first_paragraph = wiki_content.splitlines(True)[0]
print(first_paragraph)

all_objects = Author.objects.all()

for object in all_objects:

    name = ''.join(slugify(object.name).split('-'))
    try:

        wiki_data =  wikipedia.page(name)
        wiki_content = wiki_data.content
        first_paragraph = wiki_content.splitlines(True)[0]
        object.bio = first_paragraph
        print(first_paragraph)
    except:
        print(name,': not found')
    else:
        object.bio = first_paragraph
        object.save()
