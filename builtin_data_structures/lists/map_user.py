users = [
    {'id':1,'name':"Demis",'job':"Student"},
    {'id':2,'name':"Mosh",'job':"Instructor"},
    {'id':3,'name':"John",'job':"Accountant"}
]

job_list = []

for user in users:
    job_list.append(user['job'])

print(job_list)

# Using built in filter()

jobs = map(lambda user: user['job'],users)

for job in jobs:
    print(job)

# convert to list

jobs_list = list(map(lambda user: user['job'], users))
print(jobs_list)