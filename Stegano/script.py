from PIL import Image
from PIL.ExifTags import TAGS


image = Image.open("bleach.jpg")
exifdata = image.getexif()


for tagId in exifdata:
    tagName = TAGS.get(tagId)

    value = exifdata.get(tagId)

    print(f"{tagName} : {value}")


