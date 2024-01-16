# # fruits = ["Apple", "Pear", "Orange"]

# # def make_pie(index):

# #     try:
# #         fruit = fruits[index]
# #     except IndexError:
# #         print("Fruit pie")
# #     else:
# #         print(fruit + " pie")

# # make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments':2},
#     {'Likes': 33, 'Comments':2, 'Shares':1},
#     {'Likes': 13, 'Comments':8, 'Shares':3},
#     {'Likes': 11, 'Comments':2},
#     {'Likes': 31, 'Comments':5},
#     {'Comments':2, 'Shares':1},
#     {'Comments':4, 'Shares':1}
# ]


# total_likes = 0


# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#          pass

# print(total_likes)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("./day-30/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

done = True
while done:
    try:
        word = input("Enter a word: ").upper()    
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")

    else:
        done = False
        print(output_list)




