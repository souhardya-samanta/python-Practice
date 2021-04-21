phone=input("Phone number ")
output=""
digitsMapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

for x in phone:
    output+=" "+digitsMapping.get(x,"!")
print(output+" ")