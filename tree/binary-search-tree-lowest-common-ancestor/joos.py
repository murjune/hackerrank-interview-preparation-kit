# bst 인 것 실컷 풀다가 이상해서 깨달은 저 ㅋㅋㅋㅋ
# 여러분 문제를 잘 읽읍시다(?)

# 두 node 모두의 공통조상이어야 하니 root.info를 가지고 v1, v2모두에게 작거나 큰 값이어야 할 것이에요.
# 그래서 아래와 같은 풀이로 만들 수가 있습니다.

# time complexity O(logN) 최악일 때는 O(N)이겠지만


def lca(root, v1, v2):
    if not root:
        return None
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    return root

