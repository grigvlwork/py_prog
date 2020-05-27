def spectral_analysis(spectrum_dict, waves_list):
    match = []
    for name, waves in spectrum_dict.items():
        if len(set(waves) & set(waves_list)) == len(waves):
            match.append(name)
    return sorted(match)
