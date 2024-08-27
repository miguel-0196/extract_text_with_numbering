0138639d390f4a505e

I have a Word Doc (.docx) with some text
some of the text is a numbered list, using the list function in Word
I am trying to extract the text and dump it into a .txt file
but it will not capture the list numbering
i need a python script that pulls the text out, with the list numbering


REF:
https://stackoverflow.com/questions/70388809/attribute-that-defines-a-paragraph-is-a-bulleted-list-style-in-python-docx
There is currently no API support in python-docx for detecting this condition. You would need to inspect the XML of the style and you may need to walk through a few references as there is potentially some inheritance involved.

I'd recommend starting with a paragraph style you know has bullets applied and print(style._element.xml) and see what you can make out by way of an element is "number" in its name or whatever hints you can find.

I will tell you that list formatting is a complex matter in Word. You can probably find some other resources on search that may give clues, this one came up on a quick searh: Bullet Lists in python-docx