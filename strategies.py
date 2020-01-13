from tools import success, calculate_chance_narrow


def heist_optimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing=0, actions=0) -> int:
    if casing >= casing_needed:
        if success(calculate_chance_narrow(challenge_level, casing)):
            return actions
        else:
            casing -= casing_loss
            # suspicion can be lowered with the help of friends at the cost of 1 Action / 4 CP
            actions += .25 * suspicion_gain
            return heist_optimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing, actions)
    elif casing >= casing_needed - 9:
        actions += 3
        casing += 9
        return heist_optimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing, actions)
    else:
        actions += 5
        casing += 18
        return heist_optimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing, actions)


def heist_suboptimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing=0, actions=0) -> int:
    if casing >= casing_needed:
        if success(calculate_chance_narrow(challenge_level, casing)):
            return actions
        else:
            casing -= casing_loss
            # suspicion can be lowered with the help of friends at the cost of 1 Action / 4 CP
            actions += .25 * suspicion_gain
            return heist_suboptimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing, actions)
    else:
        actions += 5
        casing += 18
        return heist_suboptimal_high_level(casing_needed, challenge_level, suspicion_gain, casing_loss, casing, actions)