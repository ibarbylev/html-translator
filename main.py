from pprint import pprint

import requests


def translated(text):
    """
    The function must translate the text parameter into translation_text.
    """
    translated_text = text
    return translated_text


URL = 'http://it4each.com'

html = requests.get(URL).text

count = 0
count_text = 0
idx_last = 0
html_list = []
i = 0
for i in range(len(html)):
    if html[i] == '<':
        count += 1

        if count_text > 0:
            chunk = html[idx_last:i]
            html_list.append(chunk)
            idx_last = i

    elif html[i] == '>':
        count -= 1
        count_text = 0

        if count < 0:
            # If the error is in the HTML code.
            raise Exception('Error in html in {}')

        if count == 0 and count_text == 0:
            chunk = html[idx_last:i+1]
            html_list.append(chunk)
            idx_last = i + 1

    else:
        if count == 0:
            count_text += 1


for idx in range(len(html_list)):
    item = html_list[idx]
    if not ('<' in item or '>' in item):
        if item.strip():
            print(item.strip())
            # In this point we've got text.
            # And we can translate it with function translated()
            # And replace text in item to translated_text
            html_list[idx] = translated(item)

# HTML code recovery
html_recovery = ''
for item in html_list:
    html_recovery += item


# html_recovery - translated html code
