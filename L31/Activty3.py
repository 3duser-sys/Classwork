class India():
    def capital(self):
        print("New Delhi is da capital")

    def language(self):
        print("Its Hindi! The most widely spoken language in India")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Its Washington D.C baby! I 'm going there soon for a school trip")

    def language(self):
        print("English is the MOST USED language. U here me?! Most USED!!!!!!!")

    def type(self):
        print("USA is a developed country")

India1 = India()
USA1 = USA()

for country in (India1, USA1):
    country.capital()
    country.language()
    country.type()