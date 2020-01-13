from tools import run
import strategies


if __name__ == '__main__':
    runs = 1000000
    # Adjust values for any heist
    challenge_level = 12    # obtainable from the wiki: https://fallenlondon.fandom.com/wiki/Fallen_London_Wiki
    suspicion_gain = 2      # how many CP of suspicion are gained if the heist fails
    casing_loss = 10        # how many CP of Casing... are lost if the heist fails

    # run(casing level to aim for, etc..., heisting strategy)
    # You may want to start on higher or stop on lower levels of Casing... depending on the heist.
    run(9, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(10, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(11, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(12, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(13, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(14, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(15, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)
    run(16, challenge_level, suspicion_gain, casing_loss, runs, strategies.heist_suboptimal_high_level)