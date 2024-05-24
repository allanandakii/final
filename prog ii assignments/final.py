import os
import pyglet

# compiles all images and gifs into the program
idle = pyglet.image.load_animation('ampersand_blink.gif')
title = "Complex Apartment"
# creates window
window = pyglet.window.Window(960, 540, title)
idle_sprite = pyglet.sprite.Sprite(img=idle)
text1 = pyglet.image.load('text_box1.png')
text1_sprite = pyglet.sprite.Sprite(img=text1)
text2 = pyglet.image.load('text_box2.png')
text2_sprite = pyglet.sprite.Sprite(img=text2)
talk = pyglet.image.load_animation('ampersand_talk.gif')
talk_sprite = pyglet.sprite.Sprite(img=talk)

# properly sizes ^ images

talk_sprite.scale = 0.5
talk_sprite.position = (200, 0, 200)
text1_sprite.scale = 0.5
text1_sprite.position = (50, 0, 200)
text2_sprite.scale = 0.5
text2_sprite.position = (300, 0, 200)

# defines what the text will print

intro = "Hello! Welcome to the Complex Apartment!"
instructions = "(Press space to proceed to the next text prompt)"
intro2 = "I'm Amp, it's nice to meet you."
name_ask = "What is your name?"

# prints the label onto the window

labelname = pyglet.text.Label(name_ask,
                          font_name ='Arial',
                          font_size = 20,
                          x = window.width//2, y = window.height//2,
                          anchor_x ='center', anchor_y ='center')

label = pyglet.text.Label(instructions,
                           font_name='Arial',
                           font_size=20,
                           x=100, y=65,
                           color=(0, 0, 0, 255))
label1 = pyglet.text.Label(intro,
                           font_name='Arial',
                           font_size=20,
                           x=100, y=65,
                           color=(0, 0, 0, 255))
  
label2 = pyglet.text.Label(intro2,
                           font_name='Arial',
                           font_size=20,
                           x=100, y=65,
                           color=(0, 0, 0, 255))

label3 = pyglet.text.Label(name_ask,
                           font_name='Arial',
                           font_size=20,
                           x=100, y=65,
                           color=(0, 0, 0, 255))

label3 = pyglet.text.Label(name_ask,
                           font_name='Arial',
                           font_size=20,
                           x=100, y=65,
                           color=(0, 0, 0, 255))                           


text1_sprite.visible = True
text2_sprite.visible = True
current_text = 1

# allows the text to switch between each option

def switch_label():
    global current_text
    if current_text == 1:
        current_text = 2
    elif current_text == 2:
        current_text = 3
    elif current_text == 3:
        current_text = 4

# when the user presses the spacebar they proceed to the next dialogue

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        switch_label()
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ENTER:
        tenant 

# draws out the sprites and text

@window.event
def on_draw():
    window.clear()
    talk_sprite.draw()
    text1_sprite.draw()
    text2_sprite.draw()
    if current_text == 1:
        label.draw()
    elif current_text == 2:
        label1.draw()
    elif current_text == 3:
        label2.draw()
    elif current_text == 4:
        label3.draw()

pyglet.app.run()

# defines the user's character's class

class Tenant():
    def __init__(self, name, age, hair_color, height, special_attribute):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.height = height
        self.special_attribute = special_attribute
        self.describe = print((f"{self.name} has just moved into Complex Apartment! They are {self.age} years old, have {self.hair_color} hair, is {self.height}, and {self.special_attribute}."))

# creates a sub-class for the user's speech criteria

class Talk():
    def __init__(self, speed, tone, humor, languages, volume):
        self.speed = speed
        self.tone = tone
        self.humor = humor
        self.languages = languages
        self.volume = volume
        self.speaks = print((f"I speak at a {self.speed} speed, a {self.tone} tone, use {self.humor}, and speak {self.languages} at a {self.volume} volume."))

# creates a sub-class for the user's movement criteria

class Move():
    def __init__(self, move_speed, success_rate, style, flexibility, stamina):
        self.move_speed = move_speed
        self.success_rate = success_rate
        self.style =  style
        self.flexibility = flexibility
        self.stamina = stamina
        self.moves = print((f"I am {self.move_speed} and {self.success_rate} at moving, move unpredictably, {self.flexibility} flexible, and have a {self.stamina} stamina level."))

# creates a sub-class for the user's food criteria

class Eat():
    def __init__(self, sweet, vegetable, fruit, drink, dish):
        self.sweet = sweet
        self.vegetable = vegetable
        self.fruit = fruit
        self.drink = drink
        self.dish = dish
        self.eats = print((f"I like to eat {self.sweet}, {self.vegetable}, {self.fruit}, and like to drink {self.drink}. My favorite dish is {self.dish}."))

# begins user input sequence

print("Let's start by naming your tenant.")
print("")

# asks the user for their character's basic information
# ideally, this would have all been printed in the window and allow the user
# to type their input in the window with the sprite.

name = input("What is your tenant's name? ")
name = name.capitalize()
print("")
print("Great! Now, what are some basic characteristics of " + name + "? ")
age = int(input("How old are they? "))
hair_color = input("What color is their hair? ")
height = input("How tall are they? (Format Example - 5'4'') ")
special_attribute = input("What's something unique about them? (Appearance, personality, etc.) ")

# prints out the user's inputs in a pre-written sentence
# would have been printed into the window at the end in a sequence
tenant = Tenant(name, age, hair_color, height, special_attribute)
tenant.describe

# asks the user how their character talks
# ideally, this would have all been printed in the window and allow the user
# to type their input in the window with the sprite.

print("")
print("Your tenant will need to talk to their neighbors and landlord, right? Describe how they talk!")
print("")
speed = input("What speed do they talk at? ")
tone = input("What tone do they speak in? Ex. sarcastic, sassy, enthusiastic... ")
humor = input("What kind of humor do they have? Ex. dad humor, child humor, no humor... ")
volume = input("What volume do they speak at? Ex. loud, quiet, muffled... ")
language = int(input("How many languages do they speak? "))
multi_languages = True

# if the user's character has more than 1 language that they speak, it determines if they do or not

if language == 1:
    multi_languages = False
    many_languages = input("What language do they speak? ")

if language > 1:
    multi_languages = True
    many_languages = input("What languages do they speak? Format Example - (English and Spanish) ")
print("")

# prints out the user's inputs in a pre-written sentence
# would have been printed into the window at the end in a sequence
t = Talk(speed, tone, humor, many_languages, volume)
t.speaks

# asks the user about their character's movement statistics
# ideally, this would have all been printed in the window and allow the user
# to type their input in the window with the sprite.
print("")
print("How well do they move around?")
speed = input("What speed do they move at?")
success_rate = input("Are they clumsy, graceful, or varied with their movement?")
style = input("How do they move? Ex. sophisticated, unpredictably, swaggerly... ")
flexibility = input("How flexible are they? Format Example - very, not at all... ")
stamina = input("What's their stamina level? Ex. high, medium, low, non-existent... ")
print("")

# prints out the user's inputs in a pre-written sentence
# would have been printed into the window at the end in a sequence
ten = Move(speed, success_rate, style, flexibility, stamina)
ten.moves

# asks the user what their character likes to eat
# ideally, this would have all been printed in the window and allow the user
# to type their input in the window with the sprite.
print("")
print("What do they like to eat?")
print("")
sweet = input("What's their favorite sweet treat? ")
vegetable = input("What's their favorite vegetable? ")
fruit = input("what's their favorite fruit? ")
drink = input("What's their favorite drink? ")
dish = input("What's their favorite dish? ")
print("")

# prints out the user's inputs in a pre-written sentence
# would have been printed into the window at the end in a sequence
tenan = Eat(sweet, vegetable, fruit, drink, dish)
tenan.eats
