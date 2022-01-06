import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from quotes.models import Author
from slugify import slugify
import wikipedia



def all_lower_no_whitespace(string):
    return ''.join(slugify(string).split('-'))

def all_lower_with_whitespace(string):
    return ' '.join(slugify(string).split('-'))

filters = ["all_lower_with_whitespace","all_lower_no_whitespace"]

all_objects = Author.objects.all()

for object in all_objects:

    failed_search_term = []
    for filter in filters:
        search_term = eval(filter)(object.name)
        try:
            wiki_data =  wikipedia.page(search_term)
            wiki_content = wiki_data.content
            first_paragraph = wiki_content.splitlines(True)[0]
            second_paragraph = wiki_content.splitlines(True)[1]
        except:
            failed_search_term.append(search_term)
        else:
            if len(first_paragraph) <= 1000:
                object.bio = first_paragraph +'\n\n'+ second_paragraph
            else:
                object.bio = first_paragraph
            object.save()
            break
    else:
        print('not found: ',failed_search_term)
