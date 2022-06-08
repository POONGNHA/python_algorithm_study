from collections import deque


def isPalindrome(s = 'A man, a plan, a canal: Panama'):
    strs = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # Until left one char
    while len(strs)>1:
        # pop 1st String => pop(0), pop last String => pop()
        if strs.popleft() != strs.pop(): # O(1) + O(1)
            return False
    return True
print(isPalindrome())

# deque's pop and append time is overwhelmingly fast than list

# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
# deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.
# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).