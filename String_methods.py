# String methods:
print("return a copy of the string with its first character capitalized"
      " (put into titlecase -since version 3.8)"
      " and the rest lowercased."
      .capitalize())

print("return a casefold copy of the string. "
      "May be used for CaSeLeSs matching. Casefold is more AGGResive "
      "than LOWERCASING, because it is intended to remove all case "
      "dIstInctIonS in a string. ".casefold())

print("Return centered in a string of length 'width'.".center(72, "-"))

print("Let's see how the 'count' method is working.".count("o"))
# 'count' found the 'o' character 4 times in our string

print("Let's see how the 'count' method is working. "
      "This time we're gonna mention a range. ".count("e", 0,35))
# 'count' with a start point and an end point returned it found
# the character 'e' 5 times

print("We'll check with this method for the suffix of our string . "
      "The result should be a boolean. ".endswith("boolean. "))
# Returns True for 'boolean' being the last group of characters in our
# string.
print("As in the 'count' case, we can add an optional start and an "
      "optional end to specify the position. ".endswith("add", 10, 20))

print("This\tstring\tis\tgoing\tto\tbe\texpanded\tby\treplacing\ttabs"
      "\tcharacters\tby\tthe\tgiven\tnumber\tof\tspaces.".expandtabs())
# tabsize = 8 by default.
print("Title\tof\tthe\tdocument.".expandtabs(5))  # 5 spaces, 3 spaces,
                                                  # 2 spaces to 10/5.

print("This is a string we want to search for a substring "
      "in.".find("e",20, 30))
# returns '-1' if the substring is not content

print("It is a must to pay attention to indentetion when programming."
      .index("m"))

print("12345n45".isalnum())  # alphanumeric string
print()
print("12fff674f6428".isalpha())  # not all characters are alphabetic
print()
print("12232334".isdecimal())
print()
print("MhnfhMH".islower())  # True if all characters are in lowercase
print()
print("mbs11122".isnumeric())  # True if all characters are numeric
print()
print("    ".isspace())  # True if all characters in the string are
                         #  whitespaces. False otherwise
print()
print("is this StrInG titLEcased? ".istitle())
print()
print("IS THIS STRING UpPeRcAsed?".isupper())  # True if all characters
                                               #  are upperacased.
print()
name_of_brand = ["Dolce ", "Gabbana"]
full_name = "& ".join(name_of_brand)
# Join the elements of a list, a tuple, a dictionary into a string, with
# a separator (e. g. '&').
print(full_name)

print()
print("THis sTRing wiLl be ConvertED to LoweRcaSE.".lower())
print()

print("   The leading characters of this string will be stripped."
      .lstrip())  # Removes spaces by default
print("   The leading characters of this string will be stripped."
.lstrip(" Theldgaincrst"))  # all leading combinations of its values
                            # are stripped.
print("Don't forget to check-in 24h before your flight."
      .removeprefix("dOn't ForGet ").casefold())
# This method removes a single prefix rather than all of a set
# of characters.
print()
print("Take all your belongings before getting off the plane."
      .removesuffix("WizzAir"))  # retuned the same string as the string
                                 # doesn't contain that suffix.

print()
print("First I want to make a call. ".replace("call", "sandwich"))
# Replace an old substring with a new one
print()
print("Buy : carrots, cabbage, onion, minced garlic."
      .replace(",", " & ", 2))  # we can count the replacement.
print()
print("Even if I lived in Australia, I've never seen a kangaroo."
      .rfind("r"))  # this method returns the HIGHEST index.
print("I still got a chance to attend that course.".rindex("c"))
# returns ValueError if the substring is not found.
print()

print("Why* did* you* choose* this* course?*".rsplit("*", 3))
# splits 3 times, as specified, from the right.
print("Why* did* you* choose* this* course?*".split("*"))
# all possible splits are made
print()
print("1234 \nCome on, please, and shut the door.".startswith("1"))
print()
print("UppERcase CHaraCters wILL beComE LOweR CaSe anD Vice VerSA."
      .swapcase())

print()
print("the name of this course is introduction in programming.".title())
# Words are seen as groups of consecutive letters by the algorithm.
# The apostrophes in contractions and other signs form word boundaries,
# following a not intended result.
print("Let's see what's happening in this case."
      .title())  # as expected, apostrophes are treated as boundaries.

print()
print("Convert this string TO Uppercase.".upper())