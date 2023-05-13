# Unsecure-Password-Generator
This is a simple tool to generate passwords based of a few keywords. 
If your can generate your own password with this you should change it NOW!

usage: unsecure-password-generator.py [-h] [-l] [-ll] [-o OUTPUT] (-w WORDS [WORDS ...] | -i INPUT)

options:
  -h, --help            show this help message and exit
  -l, --long            make the list long
  -ll, --longerthanlong
                        make the list really long
  -o OUTPUT, --output OUTPUT
                        output file (default: output.txt)
  -w WORDS [WORDS ...], --words WORDS [WORDS ...]
                        The words that may be in the password (sperated by space)
  -i INPUT, --input INPUT
                        input file with words (one on each line)

Example:

unsecure-password-generator.py -w john admin wordpress -o passwords.txt #uses the words john, admin and wordwpress and outputs to passwords.txt

unsecure-password-generator.py -l -i words.txt #uses the --long option and uses words form the file words.txt
