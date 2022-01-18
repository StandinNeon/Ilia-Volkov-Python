'''TASK1'''

DICT_NUM = {
  "zero": "ноль",
  "one": "один",
  "two": "два",
  "three": "три",
  "four": "четире",
  "five": "пять",
  "six": "шесть",
  "seven": "семь",
  "eight": "восемь",
  "nine": "девять",
}


def num_translate(num_word):
  """ convert one to один...nine to девять """
  return DICT_NUM.get(num_word)

'''TASK3'''

def thesaurus(*args):
  """ conver name list to dictionary like {A: [Alex..] , B:[Bob..]} """
  out_dict = {}

  for name in args:

    if out_dict.get(name[0]):
      out_dict[name[0]].append(name)
    else:
      out_dict[name[0]] = [name]
  return out_dict

'''TASK5'''

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def gen(from_, used_, unique):
  while True:
    n_nouns = choice(from_)
    if not (unique and n_nouns in used_):
      used_.append(n_nouns)
    break
  return (n_nouns, used_)


  