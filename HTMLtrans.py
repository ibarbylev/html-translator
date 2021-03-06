"""
With this code, you can translate the text of an HTML page into 107 languages
(see the list in the "language.py" file).
The source language is determined automatically, but it can also be specified explicitly.

HTML can be retrieved either by specifying the URL, or by passing the HTML code as a text string.

The code examples you can see below.
"""

import requests
from googletrans import Translator
# pip install googletrans==4.0.0rc1


class HTMLTranslator:
    def __init__(self, lang_dest, lang_src="auto"):
        self.lang_src = lang_src
        self.lang_dest = lang_dest
        self.html = ''
        self.html_as_list = []

    def get_html_from_url(self, url) -> None:
        """
        The method retrieve HTML from specified url.
        The result is stored in the self.html attribute
        :param url: web address
        """
        r = requests.get(url)
        if r.status_code == 200:
            self.html = r.text
        else:
            raise ValueError(f"Can't HTML code from {url}")

    def get_html_as_str(self, html_text: str) -> None:
        """
        By this method You can set HTML as string.
        The result is stored in the self.html attribute
        :param html_text: html as string
        """
        if isinstance(html_text, str):
            self.html = html_text
        else:
            raise ValueError('Type of <html_text> must be string!!!')

    def translate(self) -> None:
        """
        The main method of the class. Before calling the method,
        you must call the method for getting the HTML code.
        (get_html_from_url() or get_html_as_str()).

        The method itself calls 3 separate methods in sequence:
            - a way to create a list from html code;
            - a method for optimizing and translating text blocks from this list;
            - and a way to restore html code from the list.

        The result is stored in the self.html attribute
        """
        self._split_html()
        self._translate_text_items()
        self._collect_list_into_html()

    def _split_html(self):
        """
        The method splits the HTML code into tags and saves the result in the self.html_as_list.
        The result is stored in the self.html_as_list attribute

        """
        count = 0
        count_text = 0
        idx_last = 0
        self.html_as_list = []

        for i in range(len(self.html)):
            if self.html[i] == '<':
                count += 1

                if count_text > 0:
                    chunk = self.html[idx_last:i]
                    self.html_as_list.append(chunk)
                    idx_last = i
                    count_text = 0

            elif self.html[i] == '>':
                count -= 1
                count_text = 0

                if count < 0:
                    # It means that error is in the HTML code.
                    raise Exception(f'Error in HTML in {i} position')

                if count == 0 and count_text == 0:
                    chunk = self.html[idx_last:i + 1]
                    self.html_as_list.append(chunk)
                    idx_last = i + 1
            else:
                if count == 0:
                    count_text += 1

        if count_text > 0:
            chunk = self.html[idx_last:len(self.html)-1]
            self.html_as_list.append(chunk)
            idx_last = i
            count_text = 0

    def _translate_text_items(self):
        """
        Method finds text items in self.html_as_list and translates them.
        The result is stored in the self.html_as_list attribute
        """
        translator = Translator()
        for idx in range(len(self.html_as_list)):
            item = self.html_as_list[idx]
            if not ('<' in item or '>' in item):
                if item.strip():
                    # item = item.strip().replace('.', '')
                    print(idx, f'|{item.strip}|', end='')
                    # In this point we've got text.
                    # And we can translate it with function translated()
                    # And replace text in item to translated_text
                    try:
                        new_item = translator.translate(item, src=self.lang_src, dest=self.lang_dest).text
                        self.html_as_list[idx] = new_item
                        print(f' --> {new_item}')
                    except Exception as e:
                        print(f'Translation error: {e}!!!')

    def _collect_list_into_html(self):
        """
        The method again recovery HTML-code:
        collects tags and translated text from self.html_as_list into html.
        The result is stored in the self.html attribute
        """
        html_recovery = ''
        for item in self.html_as_list:
            html_recovery += item
        self.html = html_recovery


if __name__ == '__main__':
    """
    In the example below, we get html from http://it4each.com and translate it into English.
    """
    tr = HTMLTranslator('en')
    URL = 'http://it4each.com'
    tr.get_html_from_url(URL)
    tr.translate()
    print(tr.html)

    """
    In the example below we get html as string and translate it to Spain.
    """
    HTML = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>?????????????????? ????????????????</title>
                </head>
                <body>
                    ???????????? <br> ??????!
                </body>
                </html>
            """
    tr = HTMLTranslator('es')
    tr.get_html_as_str(HTML)
    tr.translate()
    print(tr.html)
