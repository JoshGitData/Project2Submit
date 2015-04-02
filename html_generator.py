EXAMPLE_LIST_OF_LESSONS = [['Computer', 'Computer program are'],
                            ['Pyhton Program Language', 'Python is a program language'],
                            ['Compilers and other info', 'Compilers produce other languages']]

def generate_lesson_HTML( subheading, description):
    html_text_1 = '''
    <div class="lesson">
        <div class="subheading">
            ''' + subheading
    html_text_2 = '''
        </div>
        <div class="description">
            ''' + description
    html_text_3 = '''
        </div>
        </div> '''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(lesson):
    subheading = lesson[0]
    description = lesson[1]
    return generate_lesson_HTML(subheading, description)

def make_HTML_for_multiple_lessons(list_of_lessons):
    HTML = " " 
    for lesson in list_of_lessons:
        lesson_HTML = make_HTML(lesson) 
        HTML = HTML + lesson_HTML
    return HTML

print make_HTML_for_multiple_lessons(EXAMPLE_LIST_OF_LESSONS)                          
