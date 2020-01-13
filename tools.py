import random


def success(chance):
    return random.random() <= chance


def calculate_level(cp) -> int:
    level = 1
    while cp > 0:
        level += 1
        cp -= level
    level -= 1
    return level


def calculate_cp(level) -> int:
    current_level = 1
    cp = 1
    while current_level < level:
        current_level += 1
        cp += current_level
    return cp


def calculate_chance_narrow(challenge_level, cp) -> float:
    levels_above = calculate_level(cp) - challenge_level
    if levels_above > 0:
        chance = .6 + .1 * levels_above
        if chance > 1:
            chance = 1
        return chance
    else:
        return .6


def run(casing_level, challenge_level, suspicion_gain, casing_loss, runs, fun):
    total_actions = 0
    casing_needed = calculate_cp(casing_level)
    for x in range(runs):
        total_actions += fun(casing_needed, challenge_level, suspicion_gain, casing_loss)
    print("Average Actions per Success for Casing {}: {}".format(casing_level, total_actions/runs))