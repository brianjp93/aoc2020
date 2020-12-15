d = [int(x) for x in '17,1,3,16,19,0'.split(',')]
_d = d[:]
init_length = len(d)

for n in [2020, 30000000]:
    d = _d[:]
    history = {}
    i = 0
    speak = None
    while i < n:
        if len(history.get(speak, [])) > 1:
            last_seen = history[speak]
            speak = last_seen[-1] - last_seen[-2]
        elif i < init_length:
            speak = d[i]
        else:
            speak = 0
        last_seen = history.get(speak, [])
        last_seen.append(i + 1)
        history[speak] = last_seen[-2:]
        i += 1
    print(speak)
