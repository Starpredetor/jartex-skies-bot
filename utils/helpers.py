import re

def find_url(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def parse_duration(s):
    if is_integer(s):
        return s
    else:
        values = {"w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
        nums = []
        tempnums = []
        for char in s:
            if char.isdigit():
                tempnums.append(char)
            else:
                multiple = values.get(char, 1)
                num = int("".join(tempnums))
                tempnums.clear()
                nums.append(num * multiple)
        if len(nums) > 0:
            return sum(nums)
        else:
            return -1

