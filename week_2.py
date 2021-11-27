#Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list.



#sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
#last = sports[0:2]
#print(last)



#-2: gir de to siste av sports, så setter du 1 får du den siste, -2 gir de to siste siden indexen ikke begynner på 0. Motsatt ville du skrevet last = sports[0:2] for å få de to første. Da får du 0 + 1, ikke med 2.

#by = "You are"
#az = "doing a great "
#io = "job"
#qy = "keep it up!"
#message = by+" "+az+io+", "+qy


#my_str = "MICHIGAN"
#for i in my_str:

 #   print(i)



#several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
#for things in several_things:
    #print(things)

#for item in several_things:
    #print(type(item))

#Ved å skrive type(variabel_navn) så bruker du en av de predefinerte ordene til å si:
#Jeg vil vite hva dette er for noe, dvs type/class


#str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
#for lengde_liste in str_list:
#    print((len(lengde_liste)))

#Her ser du igjen det at "len" som er et reservert ord brukes for å identifisere det du itererer gjennom.


#original_str = "The quick brown rhino jumped over the extremely lazy fox."
#num_chars = 0

#for i in original_str:
    #num_chars = num_chars + 1
    #print(num_chars)


#num_chars = accumulator, dvs at du angir at man starter på 0, og så for hvert tall/bokstav er det +1 en på forrige.

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#accum = 0
#for w in nums:
#    accum = accum + print(accum)

addition_str = "2+5+10+20"
#fjern_liste = addition_str.split("+")
sum_val = 0
for i in addition_str:
    sum_val = sum(map(int,addition_str.split("+")))
    print(sum_val)


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
rense_liste = week_temps_f.split(",")
liste = [float(i) for i in rense_liste]
avg_temp = sum(liste) / len(liste)
print(avg_temp)

nums = list(range(0, 68))
print(nums)

original_str = "The quick brown rhino jumped over the extremely lazy fox"

original_list = list(original_str.split())
num_words = len(original_list)
num_words_list = []
for i in original_list:
    num_words_list.append((len(i)))

print(num_words_list)


lett = ''
for i in range(7):
    lett += 'b'
    print(lett, end='')

import turtle

imdone = turtle.Turtle()

for i in range(3):
    imdone.forward(50)
    imdone.right(144)

turtle.done()
