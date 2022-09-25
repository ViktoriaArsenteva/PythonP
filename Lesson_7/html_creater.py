

from User_interface import view


def create(result):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>  {} </p>\n'\
        .format(style,view(result))
    html += '</body\n</html>'

    with open('data.html','a') as file:
        file.write(html)

    return html