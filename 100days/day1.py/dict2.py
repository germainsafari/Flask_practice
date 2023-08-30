shuffled =[
{
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"dance" : "move in a quick and lively way.",
},
{
"Armenia" :	"Yerevan",
"Australia":"Canberra",
"Austria" : "Vienna " 
},

{
"A Passage to India" : "E.M. Foster",
"A Revenue Stamp" : "Amrita Pritam"
}
]
def add_new(location, lake, fish):
    element = {}
    element[location] = location
    element[lake] = lake
    element[fish] = fish
    shuffled.append(element)
add_new("Rwanda", "Kivu", "normal")
print(shuffled)

    
