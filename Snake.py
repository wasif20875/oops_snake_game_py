'''Imports'''
import random
class Snake():
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################
        self.color=random.choice(['green','red','white'])
        self.__offsets__={'up':'facing_upward','down':'facing_downward','right':'facing_right','left':'facing_left'}
        self.shape=[[0,0]]
        self.direction="stop"
        self.window_size=window_size
        self.GAME_OVER=False
        ###########################################
    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.direction != "down":
            self.direction = "up"

        ##########################################
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != "up":
            self.direction = "down"
        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != "right":
            self.direction = "left"
        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != "left":
            self.direction = "right"
        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """
        ############## WRITE BELOW ###############
        if ((self.shape[0][0]-current_food_position[0])**2+(self.shape[0][1]-current_food_position[1])**2)**0.5<20:
            return True
        else:
            return False
        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """ 
        ############## WRITE BELOW ###############
        if self.shape[0][0] > self.window_size[0]//2-20:
            self.shape[0][0] = -1*self.window_size[0]//2+10
        if self.shape[0][0] < -1*self.window_size[0]//2+10:
            self.shape[0][0] = self.window_size[0]//2-20
        if self.shape[0][1] < -1*self.window_size[1]//2+20:
            self.shape[0][1] = self.window_size[1]//2-20
        if self.shape[0][1] > self.window_size[1]//2-20:
            self.shape[0][1] = -1*self.window_size[1]//2+20
        #########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.direction == "up":
            self.shape[0][1]=self.shape[0][1]+20
        if self.direction == "down":
            self.shape[0][1]=self.shape[0][1]-20
        if self.direction == "left":
            self.shape[0][0]=self.shape[0][0]-20
        if self.direction == "right":
            self.shape[0][0]=self.shape[0][0]+20
        ##########################################









