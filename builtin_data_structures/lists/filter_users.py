users = [
    {'id':1,'name':"Demis",'job':"Student"},
    {'id':2,'name':"Mosh",'job':"Instructor"},
    {'id':3,'name':"John",'job':"Accountant"}
]

new_users = []
for user in users:
    if user['id'] > 1:
        new_users.append(user)
    
print(new_users)

# Filter using the built in filter function
filtered_users = filter(lambda user: user['id'] > 1,users)

for user in filtered_users:
    print(user)

# convert to iterable lis from dictionary

filtered_user_list = list(filter(lambda user: user['id'] > 1, users))
print(filtered_user_list)

facebook_users = [
    {'id':1,'name':'Demis','is_active':True},
    {'id':2,'name':'Dereje','is_active':False},
    {'id':3,'name':'Hailu','is_active':True},
    {'id':4,'name':'Dagim','is_active':False},
    {'id':5,'name':'Eyosias','is_active':True},
    {'id':6,'name':'Shambel','is_active':False},
    {'id':7,'name':'Shegaw','is_active':True}
]

active_facebook_users = filter(lambda user: user['is_active'], facebook_users)

for user  in active_facebook_users:
    print(user)

in_active_facebook_users = filter(lambda user: not user['is_active'], facebook_users)
for user  in in_active_facebook_users:
    print(user)

# Convert to iterable user list(js array ) form iterable dictionary(js object)

active_user_list = list(filter(lambda user: user['is_active'],facebook_users))
print(active_user_list)
