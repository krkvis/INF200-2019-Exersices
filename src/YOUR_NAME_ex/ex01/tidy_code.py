# -*- coding: utf-8 -*-

__author__ = 'Kjersti Rustad Kvisberg'
__email__ = 'kjkv@nmbu.no'

from random import randint as rdint


def take_user_guess():
    """Take user guess.
    :return: Number guessed by user, as integer.
    """
    user_guess = 0
    while user_guess < 1:
        user_guess = int(input('Your guess: '))
    return user_guess


def roll_two_die():
    """Simulate throwing two die as random numbers between 1 and 6, and return sum of them.
    :return: Random integer between 2 and 12.
    """
    return rdint(1, 6) + rdint(1, 6)


def compare_throw_and_guess(sum_two_die, user_guess):
    """Check if user guess is the same as dice throw.
    :param sum_two_die: Random number between 2 and 12,
        simulating random throw of two die.
    :param user_guess: Integer guessed by user.
    :return: Boolean expression,
        True if parameters have same value, False if not.
    """
    return sum_two_die == user_guess


if __name__ == '__main__':
    correct_answer = False
    points_remaining = 3
    number_to_guess = roll_two_die()
    while not correct_answer and points_remaining > 0:
        guess = take_user_guess()
        correct_answer = compare_throw_and_guess(number_to_guess, guess)
        if not correct_answer:
            print('Wrong, try again!')
            points_remaining -= 1

    if points_remaining > 0:
        print('You won {} points.'.format(points_remaining))
    else:
        print('You lost. Correct answer: {}.'.format(number_to_guess))
