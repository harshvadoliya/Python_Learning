#1
def count_word(sen):
    words = sen.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
sen='Complete sentence Complete exercise'
result= count_word(sen)
for word, count in result.items():
    print(f"{word}:{count}")

#2
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([10,12,20,22]))

#3
def smallest_num_in_list(lst):
    min = lst[0]
    for a in lst:
        if a<min:
            min=a
    return min
print(smallest_num_in_list([10,12,20,22,2]))

#4
def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr
print(match_words(['abc','xyz','aa','1221']))

#5
a = [10,12,20,22,10]
dup_items = list()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.append(x)
print(dup_items)

