# declare a dictionary and store a key value pair into it
def basicExample():
    dictionary = {}
    dictionary['oranges'] = 1.29
    print('the price of oranges is: $' + str(dictionary['oranges']))

fruitDict = {}
fruitDict['oranges'] = 1.29
fruitDict['apples'] = 2.30
fruitDict['bananas'] = 0.54
fruitDict['blueberries'] = 3.99
userInput = 0
while userInput != 5:
    print('Menu')
    print('1. oranges' + ' $' + str(fruitDict['oranges']))
    print('2. apples' + ' $' + str(fruitDict['apples']))
    print('3. bananas' +' $' + str(fruitDict['bananas']))
    print('4. blueberries' + ' $' + str(fruitDict['blueberries']))
    print('5. exit')
    userInput = int(input())
    if userInput == 1:
        print('You chose oranges which cost: $' + str(fruitDict['oranges']))
    elif userInput == 2:
        print('You chose apples which cost: $' + str(fruitDict['apples']))
    elif userInput == 3:
        print('You chose bananas which cost: $' + str(fruitDict['bananas']))
    elif userInput == 4:
        print('you chose blueberries which cost: $' + str(fruitDict['blueberries']))