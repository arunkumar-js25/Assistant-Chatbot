import re
import random

# String for each madlib. [] denotes an input
mad_libs = [
    "I spent last summer on my grandfather's [adjective] farm. He raises [plural noun] for local food [plural noun]. He also grows corn on the [noun], [adjective] lettuce and lima [plural noun]. My favorite place to [verb] on the farm is the [adjective] house where grandfather keeps his [plural noun]. But when I visit in November, there are no [plural noun]! They are all gone! I anxiously await at the table that Thanksgiving. I see the corn on the [noun] and even the lima [plural noun]. I am relieved when grandma brings out a [noun] for Thanksgiving dinner!",
    "Today we are celebrating [holiday] dinner at [name of person]'s house. When we arrived, my [name of family member] greeted us with a big, [adjective] kiss. Kisses are so [adjective]! Now we're just waiting for the [animal] to come out of the oven. My dad is watching [sport] on TV. He always shouts, \"[exclamation]\" when his team scores a [noun]. Yesss!!! Only [number] more minutes until the [animal] will be ready to eat. I wonder if my mom will let me try the [food] first. My grandma makes the best [flavor] pie! It smells like [noun]. (Much better than my [name of family member]. He/She smells like [noun]!) Happy [holiday]!",
    "It all began way back in 1621. The [adjective] pilgrims set sail from (the) [place] in hopes of starting new lives in the \"New World\" that we now call The [adjective] States of America. The first Plymouth colonists needed help adjusting to the new land. Fortunately, a Native American named Squanto (which means \"To [present tense verb] a/an [object]\") was glad to help. He taught them how to grow tall stalks of [food], make maple syrup from [type of plant] sap, and catch [living creature] from the river. He even advised them as to which plants were edibly [adjective] and which were poisonous. That first autumn harvest celebration actually lasted [number] whole days! We're pretty sure that lots of [food] and [food] were on the menu! President Lincoln made Thanksgiving an official natiional holiday in 1863. And we've been stuffing our grateful faces with [food] ever since!"
]
BOLD_MARKER = "\033[1m"
NORMAL_MARKER = "\033[0m"

print("Welcome to the Thanksgiving Mad Lib Generator!")

# Randomly choosing a mad libs from the template we have
for mad_lib in random.choice(mad_libs):

    # set the pattern to search for []
    bracket_pattern = re.compile('\[.*?\]')  #checking any character except new line(.), multiple characters(*), 0 or 1 represent(?)

    # for each match found
    for field in bracket_pattern.finditer(mad_lib):

        # value found
        value = field.group()

        # user's input
        user_input = input(BOLD_MARKER + "Enter a " + value[1:-1] + ": " + NORMAL_MARKER)

        # replace the match found with the user input. Uses the first found so it does not replace more than one.
        mad_lib = mad_lib.replace(value, user_input, 1)

    # prints the mad lib generated
    print(mad_lib)

''' #RE compile 
#Test any Regex word with sample sentences in site https://regexr.com/

CHEATSHEET:-
Character classes
.	any character except newline
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g

Anchors
^abc$	start / end of the string
\b\B	word, not-word boundary
Escaped characters
\.\*\\	escaped special characters
\t\n\r	tab, linefeed, carriage return

Groups & Lookaround
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead
(?!abc)	negative lookahead

Quantifiers & Alternation
a*a+a?	0 or more, 1 or more, 0 or 1
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three
a+?a{2,}?	match as few as possible
ab|cd	match ab or cd
'''