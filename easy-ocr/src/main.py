import easyocr

reader = easyocr.Reader(['en', 'ja'])
result = reader.readtext('menu.webp')
print(result)

result = reader.readtext('menu.webp', detail=0)
print(result)
