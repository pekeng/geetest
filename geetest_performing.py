import time

time1 = int(time.time() * 1000)
time2 = time1 + 2
time3 = time1 + 3
time4 = time1 + 66
time5 = time1 + 68
time6 = time1 + 69
time61 = time1 + 73
time7 = time1 + 178
time8 = time1 + 180
time9 = time1 + 226
performanceing = {
    'connectEnd':
        time2,
    'connectStart':
        time2,
    'domainLookupEnd':
        time2,
    'domainLookupStart':
        time2,
    'fetchStart':
        time2,
    'domComplete':
        time9,
    'loadEventEnd':
        time9,
    'loadEventStart':
        time9,

    'domContentLoadedEventEnd':
        time8,
    'domContentLoadedEventStart':
        time7,
    'domInteractive':
        time7,

    'domLoading':
        time61,
    'navigationStart':
        time1,

    'redirectEnd':
        0,
    'redirectStart':
        0,

    'requestStart':
        time3,
    'responseEnd':
        time5,
    'unloadEventStart':
        time5,

    'responseStart':
        time4,
    'secureConnectionStart':
        0,
    'unloadEventEnd':
        time6,

}
performanceing1 = {
    'a': performanceing["navigationStart"],
    'b': performanceing["unloadEventStart"],
    'c': performanceing["unloadEventEnd"],
    'd': performanceing["redirectStart"],
    'e': performanceing["redirectEnd"],
    'f': performanceing["fetchStart"],
    'g': performanceing["domainLookupStart"],
    'h': performanceing["domainLookupEnd"],
    'i': performanceing["connectStart"],
    'j': performanceing["connectEnd"],
    'k': performanceing["secureConnectionStart"],
    'l': performanceing["requestStart"],
    'm': performanceing["responseStart"],
    'n': performanceing["responseEnd"],
    'o': performanceing["domLoading"],
    'p': performanceing["domInteractive"],
    'q': performanceing["domContentLoadedEventStart"],
    'r': performanceing["domContentLoadedEventEnd"],
    's': performanceing["domComplete"],
    't': performanceing["loadEventStart"],
    'u': performanceing["loadEventEnd"]
}
# performanceing1 = {
#                       "a": 1542172731702,
#                       "b": 1542172731918,
#                       "c": 1542172731924,
#                       "d": 0,
#                       "e": 0,
#                       "f": 1542172731703,
#                       "g": 1542172731706,
#                       "h": 1542172731743,
#                       "i": 1542172731743,
#                       "j": 1542172731805,
#                       "k": 1542172731762,
#                       "l": 1542172731805,
#                       "m": 1542172731913,
#                       "n": 1542172731917,
#                       "o": 1542172731939,
#                       "p": 1542172732346,
#                       "q": 1542172732346,
#                       "r": 1542172732348,
#                       "s": 1542172732988,
#                       "t": 1542172732988,
#                       "u": 1542172732988},
