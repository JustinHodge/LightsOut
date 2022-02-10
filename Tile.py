import pygame


class Tile:
    __red = [255, 0, 0]
    __blue = [0, 0, 255]
    __state_dict = {False: __red, True: __blue}
    __tile_size = [95, 95]

    def __init__(self, row, column, state, screen):
        position_x = row * self.__tile_size[0] + row * 10
        position_y = column * self.__tile_size[1] + column * 10
        self.rectangle_layout = (pygame.Rect(position_x,
                                             position_y,
                                             self.__tile_size[0],
                                             self.__tile_size[1]))

        self.row = row
        self.column = column
        self.absolute_position = row * 5 + column
        self.state = state
        self.color = self.__state_dict[state]
        self.onscreen_tile = pygame.draw.rect(screen,
                                              self.color,
                                              self.rectangle_layout)
        pygame.display.update()

    def change_state(self, screen):
        self.state = not self.state
        self.color = self.__state_dict[self.state]
        pygame.draw.rect(screen, self.color, self.rectangle_layout)
        pygame.display.update()
