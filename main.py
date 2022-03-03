from pprint import pprint

import requests


html = requests.get('http://it4each.com').text

count = 0
count_text = 0
idx_last = 0
html_list = []
i = 0
while len(html) > i:
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

    i += 1

# print(html_list)

for item in html_list:
    if not ('<' in item or '>' in item):
        print(item.strip())
