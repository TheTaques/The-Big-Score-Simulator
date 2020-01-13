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


def destroy_statue(casing_needed, challenge_level, casing=0, actions=0) -> int:
    if casing >= casing_needed:
        if success(calculate_chance_narrow(challenge_level, casing)):
            return actions
        else:
            casing -= 9
            actions += .25  # suspicion can be lowered with the help of friends at the cost of 1 Action / 4 CP
            return destroy_statue(casing_needed, challenge_level, casing, actions)
    elif casing >= casing_needed - 9:
        actions += 3
        casing += 9
        return destroy_statue(casing_needed, challenge_level, casing, actions)
    else:
        actions += 5
        casing += 18
        return destroy_statue(casing_needed, challenge_level, casing, actions)


def bomb_financiers(casing_needed, challenge_level, casing=0, actions=0) -> int:
    if casing >= casing_needed:
        if success(calculate_chance_narrow(challenge_level, casing)):
            return actions
        else:
            casing -= 10
            actions += .5  # suspicion can be lowered with the help of friends at the cost of 1 Action / 4 CP
            return bomb_financiers(casing_needed, challenge_level, casing, actions)
    elif casing >= casing_needed - 9:
        actions += 3
        casing += 9
        return bomb_financiers(casing_needed, challenge_level, casing, actions)
    else:
        actions += 5
        casing += 18
        return bomb_financiers(casing_needed, challenge_level, casing, actions)


def run(casing_level, challenge_level, runs, fun):
    total_actions = 0
    casing_needed = calculate_cp(casing_level)
    for x in range(runs):
        total_actions += fun(casing_needed, challenge_level)
    print("Average Actions per Success for Casing {}: {}".format(casing_level, total_actions/runs))


runs = 1000000
challenge_level = 12

run(9, challenge_level, runs, bomb_financiers)
run(10, challenge_level, runs, bomb_financiers)
run(11, challenge_level, runs, bomb_financiers)
run(12, challenge_level, runs, bomb_financiers)
run(13, challenge_level, runs, bomb_financiers)
run(14, challenge_level, runs, bomb_financiers)
run(15, challenge_level, runs, bomb_financiers)
run(16, challenge_level, runs, bomb_financiers)
