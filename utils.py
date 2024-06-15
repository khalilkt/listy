from vote.models.entities import *
from vote.models.person import Person


def create_random_data(model, n):
    random_name = lambda : ''.join(random.choices(string.ascii_uppercase + string.digits + " ", k=10))
    arabe = lambda : ''.join(random.choices("بتثجحخدذرزسشصضطظعغفقكلمنهوي ", k=10))
    def get_order(bureau):
        return bureau.person_set.count() + 1
    def random_dob():
        year = random.randint(1950, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"
    for i in range(n):
        if model is Wilaya:
            model.objects.create(name=random_name(), name_ar=arabe())
        elif model is Moughataa:
            model.objects.create(name=random_name(), name_ar=arabe(), wilaya=random.choice(Wilaya.objects.all()))
        elif model is Commune:
            model.objects.create(name=random_name(), name_ar=arabe(), moughataa=random.choice(Moughataa.objects.all()))
        elif model is Centre:
            model.objects.create(name=random_name(), name_ar=arabe(), commune=random.choice(Commune.objects.all()))
        elif model is Bureau:
            model.objects.create(name=random_name(), name_ar=arabe(), centre=random.choice(Centre.objects.all()))
        elif model is Person:
            bureau = random.choice(Bureau.objects.all())
            model.objects.create(name=random_name(), name_ar=arabe(), date_of_birth=random_dob(), birth_place=random_name(), birth_place_ar=arabe(), order=get_order(bureau), bureau=bureau)
        else:
            raise ValueError(f"model {model} not supported")

        print (f"{model.__name__} {i} created")
