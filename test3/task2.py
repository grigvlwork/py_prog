electron_distribution = dict()


def level_energy(n):
    return int(136 / (n ** 2)) if n > 0 else None


def energy_transitions(*args, **kwargs):
    global electron_distribution
    if len(args) == 0:
        t = [(level, electron_distribution[level]) for level in
             sorted(electron_distribution.keys())]
        return t
    elif len(args) == 1:
        energys = args[0]
        levels = sorted(electron_distribution.keys())
        for nrg in energys:
            if nrg > 0:
                for i in range(1, len(levels)):
                    for j in range(i):
                        en_i = level_energy(levels[i])
                        en_j = level_energy(levels[j])
                        rem = nrg % (en_j - en_i)
                        n = nrg // (en_j - en_i)
                        if rem == 0:
                            if electron_distribution[levels[j]] >= n:
                                electron_distribution[levels[j]] -= n
                                electron_distribution[levels[i]] += n
            else:
                for i in range(1, len(levels)):
                    for j in range(i):
                        en_i = level_energy(levels[i])
                        en_j = level_energy(levels[j])
                        rem = abs(nrg) % (en_j - en_i)
                        n = abs(nrg) // (en_j - en_i)
                        if rem == 0:
                            if electron_distribution[levels[i]] >= n:
                                electron_distribution[levels[j]] += n
                                electron_distribution[levels[i]] -= n
        t = [(level, electron_distribution[level]) for level in
             sorted(electron_distribution.keys())]
        return t
    elif len(args) == 2 and 'change' not in kwargs:
        energys = args[0]
        new_distr = args[1]
        for level, n_electr in new_distr.items():
            if level in electron_distribution:
                electron_distribution[level] += n_electr
            else:
                electron_distribution[level] = n_electr
        return energy_transitions(energys)
    elif len(args) == 2 and 'change' in kwargs:
        energys = args[0]
        new_distr = args[1]
        change = kwargs['change']
        if not change:
            for level, n_electr in new_distr.items():
                if level in electron_distribution:
                    electron_distribution[level] += n_electr
                else:
                    electron_distribution[level] = n_electr
            return energy_transitions(energys)
        else:
            electron_distribution = dict()
            for level, n_electr in new_distr.items():
                electron_distribution[level] = n_electr
            return energy_transitions(energys)
