import pygame
import sys
from GameBoard import GameBoard
import random

_num_trials = 1000
_num_success = 0
collapse_counter_list = []


def new_game():
    pygame.init()
    __screen_size = [600, 600]
    _screen = pygame.display.set_mode(__screen_size)
    collapse_counter = 0

    current_board = GameBoard(_screen)
    # while True:
    #     pygame.display.update()
    #     for event in pygame.event.get():
    #
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             clicked_spot = pygame.mouse.get_pos()
    #             current_board.click_tile_mouse(clicked_spot, _screen)
    #             if current_board.is_game_over():
    #                 print("congrats!")
    #                 new_game()
    # return current_board.collapse(_screen)

    # while not current_board.is_game_over():
    #     current_board.click_tile_code(0, random.randint(0, 4), _screen)
    #     # if random.getrandbits(1):
    #     #     current_board.click_tile_code(0, random.randint(0, 4), _screen)
    #     current_board.collapse(_screen)
    #     collapse_counter += 1
    # collapse_counter_list.append(collapse_counter)
    # return True

    while not current_board.is_game_over():
        list_of_need_click = []
        for tile_col in range(5):
            if not current_board.tile_list[20 + tile_col].state:
                list_of_need_click.append(tile_col)
        for click in list_of_need_click:
            current_board.click_tile_code(0, click, _screen)
        # if random.getrandbits(1):
        #     current_board.click_tile_code(0, random.randint(0, 4), _screen)
        current_board.collapse(_screen)
        collapse_counter += 1
    collapse_counter_list.append(collapse_counter)
    return True


for i in range(_num_trials):
    if new_game():
        _num_success += 1
print("Number of Success: " + str(_num_success))
print("Number of Trials: " + str(_num_trials))
print("Percentage of single collapse solve: "
      + str(float(_num_success) / float(_num_trials) * 100) + "%")
print("Average number of collapses: " + str(sum(collapse_counter_list) / len(collapse_counter_list)))
print("Maximum number of collapses: " + str(max(collapse_counter_list)))
print("Minimum number of collapses: " + str(min(collapse_counter_list)))
sys.exit()

# new_game()

