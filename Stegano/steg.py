
from stegano import exifHeader
from stegano import lsb
from stegano.lsb import generators


# hiding = exifHeader.hide("aizen.jpg", 'image.jpg', secret_message="hello this is a secret")


# secret = exifHeader.reveal("image.jpg").decode("UTF-8")


# print(secret)
secret_message = "This is a secret message"
secret_image = lsb.hide("war.png", secret_message, generators.eratosthenes())
secret_image.save("secret.png")


message = lsb.reveal("secret.png", generators.eratosthenes())

print(message)

