# student = {
#     "name": "fatimah",
#     "age": 30,
#     "course": "cybersecurity"
# }

# print(student['name'])

# print(student['age'])
# print(student['course'])

import random

# dictionary in python is part of the data structure types use for collection/ to store data in key/value pairs. And data are accessed via keys.

myInfo = {
    'Chores': {
        'morning': 'I sleep all through the morning',
        'afternoon': 'I eat and then i fat around the room',
        'evening': 'I chat and abuse my guy as i feel like'
    },
    'hobby': 'I love to play music',
    'myType': 'Guys with six packs'
}

# print(myInfo['Chores']['morning'])
# print(myInfo['Chores']['afternoon'])
# print(myInfo['Chores']['evening'])
# print(myInfo['hobby'])
# print(myInfo['myType'])

# myInfo['hobby':'whatIloveToDo'] = 'I like to eat like mad'

# myInfo['interest'] = myInfo.pop('hobby')


# myInfo.get()
# print(myInfo.values())
# print(myInfo.keys())
# print(myInfo.items())
# print(myInfo.get('interest'))


# del myInfo['myType']
# myInfo.pop('hobby')

# print(myInfo)


# studentName = input('type in student name: ')

# studentInfo ={
#     'name': studentName
# }


StudentData = {
    'studentName': input('What\'s your student name: '),
    'studentId':    random.randint(1000, 5000),
    'studentGender': input('What\'s studnet gender: '),
    'studentContact': {
        'studentAddress': input('What\'s your address: '),
        'studentTellPhoneNumber': int(input('What\'s your tellphone number: '))
    },
    'studentAge': int(input('What\'s your age: '))
}

# StudentData = {
#     'studentName': 'fatimah',
#     'studentId': 281,
#     'studentGender': 'female',
#     'student'
# }


print(StudentData["studentName"])
print(StudentData["studentId"])
print(StudentData["studentGender"])
print(StudentData["studentContact"]['studentAddress'])
print(StudentData["studentContact"]['studentTellPhoneNumber'])
print(StudentData['studentAge'])
