#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def generate_num_from_gender(gender):
    uneven = ["1","3","5","7","9"]
    even = ["0","2","4","6","8"]
    if gender.lower() == "male":
        gender_num = uneven[randint(0,4)]
    elif gender.lower() == "female":
        gender_num = even[randint(0,4)]
    else:
        return False

    return gender_num

def generate_num_from_year(year):
    days_in_month = {"1": "31","2": "28","3": "31","4": "30","5": "31","6": "30",
                     "7": "31","8": "31","9": "30","10": "31","11": "30","12":"31"}
    year_num = 0
    month_num = randint(1,12)
    day_num = randint(1,int(days_in_month[str(month_num)]))
    if len(year) == 4:
        year_num = year[2:4]
    elif len(year) == 2:
        year_num = year
    else:
        return False

    if month_num < 10:
        month_num = "0" + str(month_num)
    if day_num < 10:
        day_num = "0" + str(day_num)
    return str(year_num) + str(month_num) + str(day_num)

def generate_num_from_place(place):
    nums = ""
    places = {"stockholm": "00–13", "kristianstad": "35–38" , "kopparberg": "71–73", "uppsala": "14–15" , "malmöhus": "39–45" , "gävleborg": "75–77",
"södermanland": "16–18" , "halland": "46–47" , "västernorrland": "78–81", "östergötland": "19–23" , "västra götaland": "48–54" , "jämtland": "82–84",
"jönköping": "24–26" , "älvsborg": "55–58" , "västerbotten": "85–88", "kronoberg": "27–28" , "skaraborg": "59–61" , "norrbotten": "89–92", "kalmar":
"29–31" , "värmland": "62–64", "gotland": "32" , "örebro": "66–68", "blekinge": "33–34" , "västmanland": "69–70"}

    if place.lower() in places:
        nums = places[place.lower()]
    else:
        return False

    values = nums.split("–")
    if len(values) != 1:
        return randint(int(values[0]),int(values[1]))
    else:
        return values[0]

def generate_pnr(birthyear, place, gender):
    birth_num = str(generate_num_from_year(birthyear))
    place_num = str(generate_num_from_place(place))
    gender_num = str(generate_num_from_gender(gender))

    if len(place_num) == 1:
        place_num = "0" + str(place_num)

    print str(birth_num) + "-" + str(place_num) + str(gender_num) + "?"

generate_pnr("1997", "stockholm", "Male")