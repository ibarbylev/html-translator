# html-translator

This script 
* downloads the HTML code from the specified URL, 
* extracts the text from it, 
* translates it, 
* and returns the translated text back to the HTML code.

VERY IMPORTANT: 
It must be "pure" HTML code without any admixture of JavaScript and other non-HTML code! 

You must first install the packages:
* requests
* googletrans==4.0.0rc1 (exactly this version!)