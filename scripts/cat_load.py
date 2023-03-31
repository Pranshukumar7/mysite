import csv

# python manage.py runscripts cat_load
from cats.models import Cat ,Breed 

def run():
    fhand = open('cats/meow.csv', 'r')
    reader = csv.reader(fhand)
    next(reader)

    Cat.objects.all().delete()
    Breed.objects.all().delete()

    for row in reader:
        print(row)
        b,created = Breed.objects.get_or_create(name = row[1])
        
        c = Cat(nickname = row[0],breed = b, weigth= row[2])
        c.save()

