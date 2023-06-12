import copy
def solution(attendees, note):
    q = 0
    note = note.split()
    n = len(note)
    possible = [[] for _ in range(n)]
    for i in range(n):
        if note[i] == "?":
            q += 1
            copy_attendees = copy.deepcopy(attendees)
            for j in range(-2, 3):
                idx = i - j
                if 0 <= idx < n:
                    if note[idx] != "?":
                        if note[idx] in copy_attendees:
                            copy_attendees.remove(note[idx])
            possible[i] = copy_attendees

    chk = [0] * n
    cnt = 0
    def roof(depth, chk, start, cnt):
        if depth == q:
            cnt += 1
            return cnt
        copy_chk = copy.deepcopy(chk)
        for i in range(start, n):
            if possible[i]:
                for j in possible[i]:
                    if i - 1 >= 0:
                        if chk[i - 1] == j:
                            continue
                    if i - 2 >= 0:
                        if chk[i - 2] == j:
                            continue
                    copy_chk[i] = j
                    cnt = roof(depth+1, copy_chk, i+1, cnt)
                    copy_chk = copy.deepcopy(chk)
        return cnt
    c = roof(0, chk, 0, cnt)         



    return c

a = solution(["A", "E", "B", "C", "X", "K"], "C ? ? K ? A ? E X ?")
print(a)
