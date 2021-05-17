print(
    """

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
)

continue_loop = True
salmonCount = 0
wingsCount = 0
cookiesCount = 0
springRollsCount = 0
steakCount = 0
meatTorCount = 0
gardenCount = 0
icreamCount = 0
cakeCount = 0
pyeCount = 0
coffeeCount = 0
tCount = 0
uniTearsCount = 0
while continue_loop:
    print(
        """
  ***********************************
  ** What would you like to order? **
  ***********************************
  """
    )
    response = input("> ")
    if response.upper() == "QUIT":
        continue_loop = False
        print(
            f"""
    ***********************************
    Your order is 
    ***********************************
    Appetizers
    ----------
    Wings: {wingsCount}
    Cookies: {cookiesCount}
    Spring Rolls: {springRollsCount}

    Entrees
    -------
    Salmon: {salmonCount}
    Steak: {steakCount}
    Meat Tornado: {meatTorCount}
    A Literal Garden: {gardenCount}
    
    Desserts
    --------
    Ice Cream: {icreamCount}
    Cake: {cakeCount}
    Pie: {pyeCount}

    Drinks
    ------
    Coffee: {coffeeCount}
    Tea: {tCount}
    Unicorn Tears: {uniTearsCount}
    
    ***********************************
    Your total is: Over 9,000
    ***********************************

    """
        )
        break

    elif response.upper() == "SALMON":
        if salmonCount >= 1:
            salmonCount += 1
            print(f"{salmonCount} is the number of {response}'s in your order")
        elif salmonCount == 0:
            salmonCount += 1
            print(f"{salmonCount} is the number of {response} in your order")
    elif response.upper() == "WINGS":
        wingsCount += 1
        print(f"{wingsCount} is the number of {response} in your order")
    elif response.upper() == "COOKIES":
        cookiesCount += 1
        print(f"{cookiesCount} is the number of {response} in your order")
    elif response.upper() == "SPRING ROLLS":
        springRollsCount += 1
        print(f"{springRollsCount} is the number of {response} in your order")
    elif response.upper() == "STEAK":
        steakCount += 1
        print(f"{steakCount} is the number of {response} in your order")
    elif response.upper() == "MEAT TORNADO":
        meatTorCount += 1
        print(f"{meatTorCount} is the number of {response} in your order")
    elif response.upper() == "A LITERAL GARDEN":
        gardenCount += 1
        print(f"{gardenCount} is the number of {response} in your order")
    elif response.upper() == "ICE CREAM":
        icreamCount += 1
        print(f"{icreamCount} is the number of {response} in your order")
    elif response.upper() == "CAKE":
        cakeCount += 1
        print(f"{cakeCount} is the number of {response} in your order")
    elif response.upper() == "PIE":
        pyeCount += 1
        print(f"{pyeCount} is the number of {response} in your order")
    elif response.upper() == "COFFEE":
        coffeeCount += 1
        print(f"{coffeeCount} is the number of {response} in your order")
    elif response.upper() == "TEA":
        tCount += 1
        print(f"{tCount} is the number of {response} in your order")
    elif response.upper() == "UNICORN TEARS":
        uniTearsCount += 1
        print(f"{uniTearsCount} is the number of {response} in your order")
    elif response.upper() != "QUIT":
        print(f"{response} is not on our menu")
