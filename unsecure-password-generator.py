print("\nThis is a simple tool to generate passwords based of a few keywords. \nIf your can generate your own password with this you should change it NOW!\n")
import itertools, argparse
#Argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--long", help="make the list long", action="store_true")
parser.add_argument("-ll", "--longerthanlong", help="make the list really long", action="store_true")
parser.add_argument("-o", "--output", action="store", help="output file (default: %(default)s)", default="output.txt")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-w", "--words",nargs='+', help="The words that may be in the password (sperated by space)",)
group.add_argument("-i", "--input", action="store", help="input file with words (one on each line)")

args = parser.parse_args()
if args.longerthanlong:
    print("This may take a few secons. Hold on! \n")

#Characters and SH1T
words = args.words
comb_char = "-_+/#%&@."
spec_char = "@%+\/'!#$?(){}[]~-_."
counter = 0
numbs = ['1', '2', '123', '3', '12', '7', '5', '13', '4', '11', '8', '07', '23', '22', '6', '01', '21', '10', '14', '9', '08', '06', '15', '16', '69', '18', '17', '05', '24', '09', '0', '88', '19', '25', '20', '03', '04', '89', '27', '02', '99', '26', '1234', '101', '77', '28', '33', '00', '2007', '92']
#numbs are the most common in rockyou.txt
replacements1 = {"A": "4", "E": "3"}
replacements2 = {"A": "4", "E": "3", "I": "1", "l": '1', "O": "0", "S": "5", "T": "7"}

o = open(args.output, "w")

#normal
for i in words:
    o.write(i + "\n") #input
    o.write(i.lower() +"\n")  #input lowercase
    o.write(i.capitalize() + "\n") #capitalized
    o.write(i[:-1] + i[-1:].upper() + "\n") #last uppercase
    o.write(i.upper() + "\n") #all uppercase
    counter += 5

#replace simple letters  
for i in range(len(words)):
    word = words[i]
    for letter, replacement in replacements1.items():
        word = word.replace(letter, replacement)
        word = word.replace(letter.lower(), replacement)
    o.write(word + "\n")
    o.write(word.upper() + "\n")
    counter += 2

#replace all letters 
for i in range(len(words)):
    word = words[i]
    for letter, replacement in replacements2.items():
        word = word.replace(letter, replacement)
        word = word.replace(letter.lower(), replacement)
    o.write(word + "\n")
    o.write(word.upper() + "\n")
    counter += 2

#backwards
for i in words:
    o.write(i[::-1]+"\n") #input
    o.write(i[-1:].upper() + i[-2::-1] + "\n") #first uppercase
    o.write(i[:0:-1] + i[0].upper() + "\n") #last uppercase
    o.write(i[::-1].upper() + "\n") #all uppercase
    counter += 4

#combinations
for i in words:
    for j in words:
        if (i != j):
            for k in comb_char:
                o.write(i + k + j + "\n")
                counter += 1

#numbers at end (the most common) 
for i in words:
    for j in numbs:
        o.write(i + j + "\n")
        counter += 1

#capseled
for i in words:
    o.write("\""+ i + "\""+ "\n")
    o.write("(" + i + ")" + "\n")
    o.write("[" + i + "]" + "\n")
    o.write("{" + i + "}" + "\n")
    o.write("<" + i + ">" + "\n")
    o.write("-" + i + "-" + "\n")
    counter += 6

#with 1,2 or 3 special characters at end
for i in words:
    for j in spec_char: #1 char
        o.write(i + j + "\n")
        o.write(i.upper() + j + "\n")
        counter += 2
        if args.long or args.longerthanlong:
            for k in spec_char: #2 chars
                o.write(i + j + k +"\n")
                o.write(i.upper() + j + k + "\n")
                counter += 2
                if args.longerthanlong:
                    for l in spec_char: #3 chars
                        o.write(i +j + k + l + "\n")
                        o.write(i.upper() +j + k + l + "\n")
                        counter += 2

#with 1,2 or 3 special characters at start
if args.long or args.longerthanlong:
    for i in words:
        for j in spec_char: #1 char
            o.write(j + i + "\n")
            o.write(j + i.upper() +"\n")
            counter += 2
            for k in spec_char: #2 chars
                o.write( j + k + i + "\n")
                o.write( j + k + i.upper() + "\n")
                counter += 2
                if args.longerthanlong:
                    for l in spec_char: #3 chars
                        o.write(j + k + l + i + "\n")
                        o.write(j + k + l + i.upper() + "\n")
                        counter += 2

#with numbers at end
if args.long or args.longerthanlong:
    for i in words:
        for numb1 in range(100):
            o.write(i + "{:02d}".format(numb1) + "\n")
            o.write(i.upper() + "{:02d}".format(numb1) + "\n")
            counter += 2
if args.longerthanlong:
    for numb2 in range(10000):
        o.write(i + "{:04d}".format(numb2) + "\n")
        o.write(i.upper() + "{:04d}".format(numb2) + "\n")
        counter += 2           

#with 1 or 2 special characters at start and end 
if args.long or args.longerthanlong:
    for i in words:
        for j in spec_char: #1 char on both sides
            for k in spec_char:
                o.write(j + i + k + "\n")
                o.write(j + i.upper() + k + "\n")
                counter += 2
                if args.longerthanlong:
                    for l in spec_char: #2 chars on both sides
                        for m in spec_char:
                            o.write( j + k + i + l + m + "\n")
                            o.write( j + k + i.upper() + l + m + "\n")
                            counter += 2

#other rules
for i in words:
    o.write("#1" + i + "\n")
    o.write("#1" + i.upper() + "\n")
    counter += 2


#Result:
print("Generated " + str(counter) + " passwords")
print("Output file: " + str(args.output))

