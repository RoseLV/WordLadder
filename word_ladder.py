import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])
#for (c,t) in zip(item, target):
#  if c == t:
#    return c

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]
#for word in words:
#  if re.search(pattern, word) and word not in seen.keys() and word not in list:
#    return word

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    if word[i] != target[i]:# this will reduce the words in list
      list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False # if cannot find any word like the target word, there is no such a path
  if target in list:# this will make the search more efficient
    return True # this will make the search more efficient
  list = sorted([(same(w, target), w) for w in list], reverse=True) # sorted in decrease order so that it is easier to choose the shorest way.
  for (match, item) in list:
       if match >= len(target) - 1: #if not the same and there is one or more letters different.
         if match == len(target) - 1: #if only one word
            path.append(item) # add this word to path
         return True
       seen[item] = True
  for (match, item) in list:
    path.append(item)
 #   seen[item] = True # move to this place: after adding the word to path
    if find(item, words, seen, target, path):
      return True
    path.pop() # if not delete this word from path and go back to upper level
while True:
     fname = input("Enter dictionary name: ")
     file = open(fname)
     lines = file.readlines()
     start = input("Enter start word:")
     words = []
     for line in lines:
        word = line.rstrip()
        if len(word) == len(start):
          words.append(word)
     if start not in words:
            print(start + "is not in the dictionary")
            continue
     target = input("Enter target word:")
     if len(target) != len(start):
        print("Words must be same length")
        continue
     if target not in words:
        print(target + "not in the dictionary")
        continue
     break

path = [start]
seen = {start : True} # have already seen this word
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")