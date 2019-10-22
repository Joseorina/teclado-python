users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

#has username as key
username_mapping = { 'bob:':{
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

# userid_mapping[1]
# username_mapping['bob']

#has userid as mapping
userid_mapping = { 1: {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

def authenticate(username, password):
    user = userid_mapping.get(username, None)
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_mapping(user_id, None)