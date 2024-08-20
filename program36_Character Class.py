import re
partten = r"[aeiou]" # we can also used a-z or 1-9

if re.match(partten,"afniouhf mahadi hasan"):
    print("match")