
# Aux functions for differents Users endpoints
def search_user(id, users_list):
    current_user = list(filter(lambda user: user.id == id, users_list))
    try:
        return current_user[0]
    except:
        return None