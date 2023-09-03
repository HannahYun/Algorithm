def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    n_id = ''
    for s in new_id:
        if s.isalpha() or s.isdigit() or s == "-" or s == "_" or s == ".":
            n_id += s
    
    cnt = n_id.count("..")
    for i in range(cnt):
        n_id = n_id.replace("..", ".")
    
    if len(n_id) != 0 and n_id[0] == ".":
        n_id = n_id[1:]
    if len(n_id) != 0 and n_id[-1] == ".":
        n_id = n_id[:-1]
    if len(n_id) == 0:
        n_id = "a"
    if len(n_id) >= 16:
        n_id = n_id[:15]
        if n_id[-1] == ".":
            n_id = n_id[:-1]
    if len(n_id) <= 2:
        tmp = n_id[:-1]
        n_id = tmp + n_id[-1] * (3-(len(n_id)-1))
    answer = n_id
    return answer