def save_user(**user):
    print(user['id'])

save_user(id=1,name="Demis",age=21)

def get_cart_item(**item):
    return item

cart_item = get_cart_item(id=1,name="Banana",price=34.56)

print(cart_item)