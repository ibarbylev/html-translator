# html-translator

This script can translate the text of an HTML page into 107 languages (see the list in the "language.py" file).
The source language is determined automatically, but it can also be specified explicitly. 
HTML can be retrieved either by specifying the URL, or by passing the HTML code as a text string.

The code works according to the following algorithm:
* downloads the HTML code from the specified URL or by passing the HTML code as a text string, 
* extracts the text from it, 
* translates it, 
* and returns the translated text back to the HTML code.

VERY IMPORTANT: 
It must be "pure" HTML-code without any admixture of JavaScript and other non-HTML code! 

You must first install the packages:
* requests
* googletrans==4.0.0rc1 (exactly this version!)

## Example 1
### Get HTML-code from URL http://it4each.com and translate it into English
(The URL example here is not quite correct as this html code contains JavaScript elements)
```
    tr = HTMLTranslator('en')
    URL = 'http://it4each.com'
    tr.get_html_from_url(URL)
    tr.translate()
    print(tr.html)
```

## Example 2
### In the example below we get html as string and translate it to Spain.
```
    HTML = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Заголовок страницы</title>
            </head>
            <body>
                Привет <br> мир!
            </body>
            </html>
        """
    tr = HTMLTranslator('es')
    tr.get_html_as_str(HTML)
    tr.translate()
    print(tr.html)
```