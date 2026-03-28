name="marija"
password="554321"
name=name.lower()

#vezba: proveriti da li je ime 'toma' i da je sifra '123456'
#vezba: proveriti da li je ime 'marija' i da je sifra '554321' print 'dobrodosla marija'

if name=="admin" and password=="mojasifra":
    print("Dobrodosao admine")
elif name=="toma" and password=="123456":
    print("Dobrodosao Tomo")
elif name=="marija" and password=="554321":
    print("Dobrodosla Marija")
else:
    print("Niste te administrator, pogresna sifra ili ime")
