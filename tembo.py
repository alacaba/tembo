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

def print_activity_index(index):
    def print_atv(child, parent):
        try:
            activity_list = get_activity_by_age(child.get('age', 0))
            params = (parent, child['childName'], child['age'], activity_list[index])
            print("%s's child %s aged %d: %s \n" % params)
        except IndexError:
            pass # ignore
    return print_atv

def print_activity():
    print("Printing Activities....\n")

    max_activities = max([ len(ac['activity']) for ac in activities ])
    printers = map(print_activity_index, range(max_activities))
    [ [ printer(child, parent) for parent, child in parents.items() ] for printer in printers ]

    print("Curriculum Complete!")

def add_age_group(age):
    age_groups = [ activity['age'] for activity in activities ]
    if age not in age_groups:
        age_group = { 'age': age, 'activity': list() }
        activities.append(age_group)

def get_activity_by_age(age):
    filter_activity = lambda x: x['age'] == age
    atvs = filter(filter_activity, activities)
    return list(atvs)[0].get('activity', [])

def add_activity(age, activity):
    add_age_group(age)
    atvs = get_activity_by_age(age)
    atvs.append(activity)
    print("Activity added!")

def add_parent(parent, child):
    add_age_group(child['age'])
    parents[parent] = child
    print("Parent added!")

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

