#!/usr/bin/python3

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

def print_activity(parent={}):
    child = None
    age = parent.get('age', 0)

    for activity in activities:
        if age == activity['age']:
            child = activity

    if child:
        print("Activities for %s age %d:" % (parent['childName'], age))

        for activity in child['activity']:
            print(activity)
        print("Curriculum complete!")

    else:
        print("There are no curriculum for this child age.")

def add_age_group(age):
    age_group = { 'age': age, activity: list() }
    activities.append(age_group)

def add_parent():
    parent    = input("Enter parent name: ")
    childName = input("Enter your child's name: ")
    age       = int(input("Enter your child's age: "))
    child = { 'childName': childName, 'age': int(age) }
    ages = [ activity['age'] for activity in activities ]
    if age not in ages:
        add_age_group(age)
    parents[parent] = child
    return parents[parent]


def get_activity_by_age(age):
    for activity in activities:
        if activity['age'] == age:
            return activity.get('activity', [])


def add_activity():
    age = int(input("Enter child's age group: "))
    add_more = True

    while add_more:
        activity = input("Enter activity for age group %d: \n" % age)
        activities = get_activity_by_age(age)
        activities.append(activity)
        should_add_more = input("Do you want to add another activity? (y/n): ")
        if should_add_more == 'n':
            add_more = False

def run():
    add_new_parent = input("Do you want to add a parent? (y/n): ")
    if add_new_parent == 'y':
        add_parent()

    add_new_activity = input("Do you want to add activity? (y/n): ")
    if add_new_activity == 'y':
        add_activity()

    print("Welcome to Tembo curriculum checker")
    parents_list = list(parents.keys())
    parent_name = input("Enter parent name to view their child's curriculum: \
            \nSelect parent: (%s) \n" % ', '.join(parents_list))
    print("")
    print("=========================================")
    print("")
    print_activity(parents[parent_name.capitalize()])
    print("")
    print("=========================================")

run()
