import unittest

from tembo import add_activity, add_parent, activities, parents, get_activity_by_age, add_age_group

class TestAddActivityAndParentMethods(unittest.TestCase):
    def test_add_activity(self):
        activity = { 'age': 5, 'activities': 'Play soccer on weekdays' }
        add_activity(activity['age'], activity['activities'])
        atvs = get_activity_by_age(activity['age'])
        self.assertIn(activity['activities'], atvs)

    def test_add_parent(self):
        parent = { 'Allan': {'childName': 'Brutus', 'age': 3 } }
        add_parent('Allan', parent['Allan'])
        self.assertIn('Allan', parents.keys())

    def test_add_age_group(self):
        age = 5
        add_age_group(age)
        ages = [ atvs['age'] for atvs in activities ]
        self.assertIn(age, ages)

if __name__ == '__main__':
    unittest.main()
