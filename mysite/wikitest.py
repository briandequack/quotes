import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from quotes.models import Author
from slugify import slugify
import wikipedia

lol = 'Joanne Rowling ( ROH-ling; born 31 July 1965), known by her pen name J. K. Rowling, is a British author, philanthropist, film producer, and screenwriter. She is the author of the Harry Potter series, which has won multiple awards and sold more than 500 million copies, becoming the best-selling book series in history. The books are the basis of a popular film series. She also writes crime fiction under the pen name Robert Galbraith.'

if len(lol) <= 600:
    print(len(lol))

my_list = Author.objects.all().filter(bio=None)
print(my_list)



'''

not found:  ['andregide']
not found:  ['thomasaedison']
not found:  ['eliewiesel']
not found:  ['allensaunders']
not found:  ['ralphwaldoemerson']
not found:  ['charlesmschulz']
not found:  ['williamnicholson']
not found:  ['jorgeluisborges']
not found:  ['georgeeliot']
not found:  ['georgerrmartin']
not found:  ['jamesbaldwin']
not found:  ['alexandredumasfils']
not found:  ['charlesbukowski']
not found:  ['suzannecollins']
not found:  ['alfredtennyson']
not found:  ['jdsalinger']
not found:  ['khaledhosseini']
not found:  ['harperlee']
not found:  ['madeleinelengle']

not found:  ['georgeeliot', 'george eliot']
not found:  ['khaledhosseini', 'khaled hosseini']
'''


def all_lower_with_whitespace(string):
    return ' '.join(slugify(string).split('-'))

print(all_lower_with_whitespace('ander-gide'))

search_term = 'andre gide'
'''
try:
    wiki_data =  wikipedia.page(search_term)
    wiki_content = wiki_data.content
    first_paragraph = wiki_content.splitlines(True)[0]
    print(first_paragraph)
except:
    print('not found')
'''
