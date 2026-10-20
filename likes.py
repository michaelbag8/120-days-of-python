# TODO: use type annotation

def media_likes(likes):

    if not isinstance(likes , list):
        return "Sorry, only list is allowed"

    count = len(likes)

    if count == 0:
        return "No one like this"

    elif count == 1:
        return f"{likes[0]} like this"

    elif count == 2:
        return f"{likes[0]} and {likes[1]} like this"

    elif count == 3:
        return f"{likes[0]}, {likes[1]} and {likes[2]} like this"
    else:
        return f"{likes[0]}, {likes[1]} and {count - 2} others like this"

a = []
b = ["James"]
c = ["Joel", "Jay"]
d = {}
names = ["John", "Moses", "Clems", "Kings", "Eazy", "Yaks", "Joel", "Joyce", "Ahubi", "Queen"]
print(media_likes(a))
print(media_likes(b))
print(media_likes(c))
print(media_likes(d))
print(media_likes(names))