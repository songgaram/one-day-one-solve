from collections import deque
def solution(begin, target, words):
    # visited
    visited = dict()
    for w in words:
        visited[w] = False
        
    def bfs(start):
        q = deque()
        q.append(start)
        while q:
            word, cnt = q.popleft()
            # 글자 배열 순회
            for base in words:
                flag = 0
                if visited[base]:
                    continue
                # 기존 배열에서 현재 단어 비교
                for i in range(len(word)):
                    if word[i] != base[i]:
                        flag += 1
                # 만약 1개 이상 글자가 다르다면 패스
                if flag > 1:
                    continue
                # 타겟과 같다면 리턴
                if base == target:
                    return cnt
                # 아니라면 덱에 넣기
                visited[base] = True
                q.append([base, cnt+1])
            
        return 0
    answer = bfs([begin, 1])
    return answer