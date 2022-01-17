
from django.http import HttpResponse

functions = [
    {'name':'Polls', 'link':'/polls/'},
    {'name':'Admin', 'link':'/admin/'}
]

def template():
    global functions
    ol = ''
    for function in functions:
        ol += f'''<li><a href={function['link']}>{function['name']}</a></li>'''
    return f'''
    <html>
        <head>
            <title>Root page</title>
        </head>
        <body bgcolor="#F5ECCE">
            <h2>Now You're Seeing Root page of Django_practice2(mysite).</h2>
            <p>If you want to want to use other functions of this site, here is some links.</p>
            <ul>
                {ol}
            </ul>
        </body>
    </html>
    '''

def index(request):
    return HttpResponse(template())
