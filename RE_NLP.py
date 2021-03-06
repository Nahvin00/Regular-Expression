import re

def search_pattern_in_string(pattern, string):
  search = re.compile(pattern).search(string)
  if not search:
    return "No match"
  else:
    return "Found pattern: " + search.group()

print(search_pattern_in_string(".", "Sherlock Holmes"))

print(search_pattern_in_string("^S", "Sherlock Holmes"))
print(search_pattern_in_string("^ ", " Holmes"))
print(search_pattern_in_string("^e", "Sherlock Holmes"))
print(search_pattern_in_string("[a^b]", "Look up a^b now"))
print(search_pattern_in_string("[^S]", "Sherlock Holmes"))

print(search_pattern_in_string("$", "Sherlock Holmes"))
print(search_pattern_in_string("s$", "Sherlock Holmes"))
print(search_pattern_in_string("t$", "Sherlock Holmes"))

print(search_pattern_in_string("l*", "Sherlock Holmes"))
print(search_pattern_in_string("S*", "Sherlock Holmes"))
print(search_pattern_in_string("S*", "Ssssssherlock Holmes"))

print(search_pattern_in_string("z*", "Sherlock Holmes"))
print(search_pattern_in_string("z+", "Sherlock Holmes"))
print(search_pattern_in_string("S+", "Ssssssherlock Holmes"))

print(search_pattern_in_string("2{1,3}", "221B Baker Street, London"))
print(search_pattern_in_string("2{3,4}", "221B Baker Street, London"))

print(search_pattern_in_string("[ik]", "221B Baker Street, London"))

string = "Is there any other point to which you would wish to draw my attention?"
print(search_pattern_in_string("\?", string))
print(search_pattern_in_string("z|k", "221B Baker Street, London"))

string = "apple87"
pattern = r"[a-z]+(?=\d)"
search_pattern_in_string(pattern, string)

string = "87apples"
pattern = r"[0-9]+(?=apples)"
search_pattern_in_string(pattern, string)

string = "Hey this is a random text from your friend. \nHow are you doing [name goes here]?\nWell I hope!"
string = re.sub("\[name goes here\]", "HALIZAH", string)
print(string)

string = "Mengulas lanjut, Dr Noor Hisham, berkata 643 kes baharu yang dilaporkan di Sabah, "
string = string + "sebanyak 343 kes dikesan daripada hasil saringan kontak rapat kes positif COVID-19, "
string = string + "manakala 183 kes daripada kluster sedia ada diikuti 117 kes daripada lain-lain "
string = string + "saringan COVID-19."
pattern = re.compile("\d+")
print(pattern.findall(string))

pattern = "\d{3}-\d{3}-\d{4}"
result = re.findall(pattern, 'Call me at 132-222-7218, or at 132-222-1111')
for i in range(len(result)):
  print('Phone Number found:' + result[i])

#Modified

pattern = "\d{2,3}-\d{7}"
result = re.findall(pattern, 'Call me at 06-2702433, or at 013-6302093')
for i in range(len(result)):
  print('Phone Number found:' + result[i])

message = "I am going to grocery tomorrow and need to get the following:"
message = message + "3 onions, 1 bread, 1 Milk, 10 bananas, 5 peppers and 12 oranges."
groceryRegex = re.compile(r'\d+')
print(groceryRegex.findall(message))

#Modified

groceryRegex = re.compile(r'\d+ \w+')
print(groceryRegex.findall(message))
