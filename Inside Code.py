#chatbot introduction
import time
print('Hello. I am Zyxo 64. I am a chatbot.')
time.sleep(2)
print('I like animals and I love to talk about food.')
time.sleep(1)
name = input('What is you name?: ')
print('Hello', name, ', Nice to meet you.')
#get year info
time.sleep(2)
year = input('I am not very good with dates. What is this year?: ')
print('Yes, I think that is correct. Thanks! ')
#ask user to guess age
time.sleep(2)
myage = input('Can you guess my age? - enter a number: ')
print('Yes you are right. I am ', myage)
#calculate when he will turn 100
myage = int(myage)
nyears = 100 - myage
time.sleep(2)
print('I will be 100 in', nyears, 'years')
print('That will be the year', int(year) + nyears)
#food conversation
time.sleep(2)
print('I love chocolate and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print('I like',food, 'too.')
time.sleep(2)
question = 'How often do you eat ' + food + '?: '
time.sleep(1)
howoften = input(question)
print('Interesting. I wonder if that is good for your health')
#animal conversation
time.sleep(2)
animal = input('My favorite animal is a giraffe. What is yours?: ')
print(animal,'! I do not like them.')
time.sleep(1)
print('I wonder if a', animal, 'likes to eat', food, '?')
time.sleep(2)
#feelings conversation
feeling = input('How are you feeling today?: ')
print('Why are you feeling', feeling, 'now')
time.sleep(1)
reason = input('Please tell me: ')
print('I understand. Thanks for sharing')
#goodbye
time.sleep(1)
print('*yawn*')
time.sleep(1)
print('It has been a long day')
time.sleep(1)
print('I am to tired to talk. We can chat again later.')
time.sleep(1)
print('Goodbye', name, 'I liked chatting with you')

