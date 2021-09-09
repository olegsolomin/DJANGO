import csv
from unesco.models import Category, Region, State, Site, Iso

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:

        print(row)
        n = row[0]
        d = row[1]
        j = row[2]

        a, created = Category.objects.get_or_create(name=row[7])
        a.save()

        b, created = State.objects.get_or_create(name=row[8])
        b.save()

        c, created = Region.objects.get_or_create(name=row[9])
        c.save()

        d, created = Iso.objects.get_or_create(name=row[10])
        d.save()

        #for year
        try:
            y = int(row[3])
        except:
            y = None
        #for longitude
        try:
            ln = float(row[4])
        except:
            ln = None
        #for latitude
        try:
            lt = float(row[5])
        except:
            lt = None

        #for area_hectares
        try:
            h = float(row[6])
        except:
            h = None
        #name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso

        site = Site(
            name = n ,description=d ,justification=j,year=y,
            longitude=ln, latitude = lt,area_hectares=h ,category=a,
            state=b, region=c, iso=d
            )
        site.save()