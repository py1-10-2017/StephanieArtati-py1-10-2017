
def print_list(people_list):
    for i in range(len(people_list)):
        name = ""
        for value in people_list[i].values():
            name += value + " "
        print(name)

def print_nested_dict(dict):
    for role in dict:
        print(role)
        counter = 0
        for person in dict[role]:
            counter += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(first_name) + len(last_name)
            print("{} - {} {} - {}".format(counter,first_name,last_name,length))

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print_list(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print_nested_dict(users)
