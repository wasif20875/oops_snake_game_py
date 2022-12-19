"""
Imports
"""
import random # used to generate random positions of the food


"""
File that implements the Food class
"""
class Food:
    """
    Class that holds all the attributes of the food
    that the snake consumes in the game.
    """
    def __init__(self, window_size: tuple):
        """
        Constructor for the Food class. Takes the game
        window size as tuple for input. Has to initialize
        the following parameters.

        shape: str
               Indicates the shape of the food. Can have the
               values  “arrow”, “turtle”, “circle”, “square”,
               “triangle” and “classic”.

        color: str or tuple of RGB integers.
               Indicates the color of the food. Can have values
               "red", "green", "yellow" etc or be a tuple of
               integers like (44,99,244).

        size:  int
               Indicates the size of the food.

        window_size:
                tuple of integers
                Holds the size of the current game window

        position: tuple of integers
                  Holds the (x,y) position of the food


        You are to initialize the above variables with suitable
        values.

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW  ###############
        self.color=random.choice(['red','green','black','white'])
        self.shape=random.choice(['square','triangle','circle','classic'])
        self.window_size=window_size
        self.size=1
        self.position=(0,0)
                                  
        ###########################################

    def set_position(self, new_food_position: tuple) -> None:
        """
        Function that updates the value of the position of the
        food with the value that is passed to the function.

        :param new_food_position: A tuple of integers which
                                  represents the new position
                                  of the food.
        :return: None
        """
        ############### WRITE BELOW ################
        self.new_food_position=new_food_position
        self.position=self.new_food_position
        return None
        
        ############################################

    def update_random_food_position(self)-> None:
        """
        Function that generates a random pair of (x,y)
        points inside the game window and updates the
        value of the position
        :return: None
        """
        ################ WRITE HERE ################
        self.__k=(self.window_size[0]//2)-30
        self.__l=(self.window_size[1]//2)-30
        self.x=random.randint(-1*self.__k,self.__k)
        self.y=random.randint(-1*self.__l,self.__l)
        self.position=(self.x,self.y)
        return None
        ############################################

