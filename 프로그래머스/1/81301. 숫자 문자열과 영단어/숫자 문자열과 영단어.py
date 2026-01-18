def solution(s):

    vocab_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, st in enumerate(vocab_list):
        # print(st, str(idx))
        s = s.replace(st, str(idx))
    
    # print(s)
    return int(s)