import pymupdf as reader
from PIL import Image

#doc = reader.open("test_pattern.pdf")
#print(doc)

def find_ruler(page):
    drawings = page.get_drawings()
    for drawing in drawings:
        #print([item[0] for item in drawing['items']])
        pass
    item = drawings[0]
    print(item['items'][0])
    line = item['items'][0]
    x0, y0 = line[1][0], line[1][1]
    x1, y1 = line[2][0], line[2][1]
    rect_like = reader.Rect(x0, y0, x1+1, y1+1)
    print(rect_like)
    highlight = page.add_highlight_annot(rect_like)
    highlight.update()
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.show()



doc = reader.open("test_pattern.pdf")
first_page = doc[0]
find_ruler(first_page)

