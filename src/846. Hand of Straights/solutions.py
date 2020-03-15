from collections import Counter


class Solution(object):
    def isNStraightHand(self, hand, W):
        # 转换成Dict {"1": 出现次数，"2": 出现次数}
        cards = Counter(hand)
        for start in sorted(cards):
            if cards[start] > 0:
                # 遍历起始牌后面的W位牌
                for j in range(W)[::-1]:
                    # 如果字典里没有start+j 代表顺子组成不了 return false
                    if start+j not in cards:
                        return False
                    # 在字典里减去起始牌的次数
                    cards[start+j] -= cards[start]
                    # 如果字典里的start+j位牌出现次数少于0 return false
                    if cards[start+j] < 0:
                        return False
        return True
