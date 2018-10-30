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

    for activity in activities:
        age = parent.get('age', 0)
        if age == activity['age']:
            child = activity

    if child:
        print("Activities for age %d:" % child['age'])

        for activity in child['activity']:
            print(activity)
        print("Curriculum complete!")

    else:
        print("There are no curriculum for this child age.")

def add_parent():
    parent    = input("Enter parent name: ")
    childName = input("Enter your child's name: ")
    age       = input("Enter your child's age: ")
    child = { 'childName': childName, 'age': int(age) }
    parents[parent] = child
    return parents[parent]

def add_activity(age):
    if age is None:
        print("Please enter an age")
parent = input("Enter parent: ")
print_activity(parents[parent])
add_parent()
print(parents)

