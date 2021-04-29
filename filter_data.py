DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    python_dev = list(filter(lambda worker: worker["language"]=="python", DATA))
    python_dev = list(map(lambda worker: worker["name"], python_dev))
    print("These people are Python developers: ", python_dev)
    platzi_worker = list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    platzi_worker = list(map(lambda worker: worker["name"], platzi_worker))
    print("These people are adult: ", platzi_worker)
    adult_worker = list(filter(lambda worker: worker["age"]>=18, DATA))
    adult_worker = list(map(lambda worker: worker["name"], adult_worker))
    print("These people are adult: ", adult_worker)
    old_worker = list(map(lambda worker: worker | {"old": worker["age"]>= 60}, DATA))
    print("These are new dictionaries:\n", old_worker)


if __name__ == "__main__":
    run()