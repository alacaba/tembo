#!/usr/bin/env python3

parents = {
    'Henry': {'childName': 'Calvin', 'age': 1},
    'Ada': {'childName': 'Lily', 'age': 4},
    'Emilia': {'childName': 'Petra', 'age': 2},
    'Biff': {'childName': 'Biff Jr', 'age': 3},
    'Milo': {}
}

activities = [
    {
        'age': 1,
        'activity': [
            'Go outside and feel surfaces.',
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

def print_activity():
    print("Printing Activities....\n")

    ac_length = [ len(ac['activity']) for ac in activities]

    for i in range(max(ac_length)):
        for parent, child in parents.items():
            activity_list = get_activity_by_age(child.get('age', 0))
            try:
                if activity_list:
                    print("%s's child %s aged %d: %s \n" %
                            (parent, child['childName'], child['age'], activity_list[i]))
            except IndexError:
                next

    print("Curriculum Complete!")

def age_groups():
    return [ activity['age'] for activity in activities ]

def add_age_group(age):
    age_group = { 'age': age, 'activity': list() }
    activities.append(age_group)

def get_activity_by_age(age):
    for activity in activities:
        if activity['age'] == age:
            return activity.get('activity', [])

def add_activity(age, activity):
    if age not in age_groups():
        add_age_group(age)
    atvs = get_activity_by_age(age)
    atvs.append(activity)

def add_parent(parent, child):
    if child['age'] not in age_groups():
        add_age_group(child['age'])
    parents[parent] = child

def add_parent_input():
    print("Enter parent name: ")
    parent = input("> ")
    print("Enter child's name: ")
    childName = input("> ")
    print("Enter child's age: ")
    age = int(input("> "))
    child = { 'childName': childName, 'age': int(age) }
    add_parent(parent, child)

def add_activity_input():
    print("Enter child's age group: ")
    age = int(input("> "))
    print("Enter activity for age group %d:" % age)
    activity = input("> ")
    add_activity(age, activity)

def loop(func, data):
    cont = True

    while cont == True:
        func()
        answer = input("Do you want to add another %s? (y/n): " % data)
        if answer == 'n':
            cont = False

    prompt()

def prompt():
    print("Welcome to Tembo curriculum checker \n")

    print("What do you want to do?")
    print("")
    print("a.) Add parent")
    print("b.) Add activity")
    print("c.) Print parents and activities")
    print("")

    selection = input("select: (a/b/c/q(quit)): ")

    if selection == 'a':
        loop(add_parent_input, 'parent')
    elif selection == 'b':
        loop(add_activity_input, 'activity')
    elif selection == 'c':
        print_activity()
    elif selection == 'q':
        print("Exiting application")
        exit()
    else:
        print("Please select one from the choices")
        prompt()


if __name__ == '__main__':
    prompt()

