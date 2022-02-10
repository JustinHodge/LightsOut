import random

import pygame

from Tile import Tile


class GameBoard:
    __black = [0, 0, 0]
    __edge_tiles = 5
    collapse_counter = 0

    def __init__(self, screen):
        """the section below gives a randomized board that will always be solvable"""
        self.tile_list = []
        screen.fill(self.__black)
        for row in range(self.__edge_tiles):
            for column in range(self.__edge_tiles):
                current_tile = Tile(row, column, 0, screen)
                self.tile_list.append(current_tile)

        for i in range(10):
            self.click_tile_code(random.randint(0, 4), random.randint(0, 4), screen)

        pygame.display.update()
        """the section below gives a truly random board that likely produces unsolvable boards"""
        # self.tile_list = []
        # screen.fill(self.__black)
        # for j in range(self.__edge_tiles):
        #     for i in range(self.__edge_tiles):
        #         current_tile = Tile(i, j, random.randrange(2), screen)
        #         self.tile_list.append(current_tile)
        # pygame.display.update()

    def click_tile_mouse(self, clicked_spot, screen):
        clicked_tile = 5 * int(clicked_spot[0] / 100) + int(clicked_spot[1] / 100)
        set_of_tiles = []

        if clicked_spot[0] < 500 and clicked_spot[1] < 500:
            set_of_tiles.append(self.tile_list[clicked_tile])
            if (clicked_tile + 1) % 5 != 0:
                set_of_tiles.append(self.tile_list[clicked_tile + 1])
            if clicked_tile % 5 != 0:
                set_of_tiles.append(self.tile_list[clicked_tile - 1])
            if (clicked_tile - 5) >= 0:
                set_of_tiles.append(self.tile_list[clicked_tile - 5])
            if (clicked_tile + 6) <= 25:
                set_of_tiles.append(self.tile_list[clicked_tile + 5])
        for i in set_of_tiles:
            i.change_state(screen)

    def click_tile_code(self, row, column, screen):
        center_tile = 5 * row + column
        set_of_tiles = [self.tile_list[center_tile]]
        if (center_tile + 1) % 5 != 0:
            set_of_tiles.append(self.tile_list[center_tile + 1])
        if center_tile % 5 != 0:
            set_of_tiles.append(self.tile_list[center_tile - 1])
        if (center_tile - 5) >= 0:
            set_of_tiles.append(self.tile_list[center_tile - 5])
        if (center_tile + 6) <= 25:
            set_of_tiles.append(self.tile_list[center_tile + 5])
        for i in set_of_tiles:
            i.change_state(screen)

    def is_game_over(self):
        return all(i.state for i in self.tile_list)

    def collapse(self, screen):
        self.collapse_counter += 1
        for tile in self.tile_list:
            if (not tile.state) and (tile.row < 4):
                row_to_change = tile.row + 1
                column_to_change = tile.column
                self.click_tile_code(row_to_change, column_to_change, screen)
