import re
# same方法return对上号的字母 越大越好，所以后面用reverse排列。return the length of the same letter on same position
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words # an array of all same length word
  if re.search(pattern, word) and word not in seen.keys() and word not in list]
  # re.search = match                list[] : 从0到length的某一位和word有一位不一样的

def find(word, words, seen, target, path):
  list = []  # 从0到length的某一位和word有一位不一样的
  for i in range(len(word)):
    if word[i] != target[i]:  # this will reduce the words in list
      list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False   # if cannot find any word like the target word, there is no such a path

  if target in list:  # this will make the search more efficient
    return True    # this will make the search more efficient
  list = sorted([(same(w, target), w) for w in list], reverse=True)
  print(3)
  print(list)
  # sorted in decrease order so that it is easier to choose the shorest way.

  for (match, item) in list:
    if match >= len(target) - 1:  # if not the same and there is one or more letters different.
      if match == len(target) - 1:  # if only one word #如果只有一位和target不一样了，eg：len（target）=4， match=3；
        path.append(item)
        print('1')
        print(path)# add this word to path
      return True
    seen[item] = True

  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()
    print(2)
    print(path)


while True:
  fname = input("Enter dictionary name: ") # 先输入词典名
  file = open(fname)
  lines = file.readlines()
  start = input("Enter start word:")       # 再输入起始单词
  words = []  # 紧接着找出所以长度一样的单词添加到words里；an array of all same length word, for limiting the search scope
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")     # 再输入目标单词
  break
#count = 0

path = [start]  # User input start         # path始于start
seen = {start: True}  # have already seen this word    {DICTIONARY KEY:START, VALUE:TRUE}
if find(start, words, seen, target, path):
  path.append(target)   # append target one by one 一层一层加
  print(len(path) - 1, path)
else:
  print("No path found")

