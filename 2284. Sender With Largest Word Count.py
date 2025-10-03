class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        msg_sender = {}
        for sender, msg in zip(senders, messages):
            if sender in msg_sender:
                msg_sender[sender] += len(msg.split())
            else:
                msg_sender[sender] = len(msg.split())

        maxi = 0
        ans = 0
        for key, value in msg_sender.items():
            if value > maxi:
                ans = key
                maxi = value
            elif value == maxi:
                if key > ans:
                    ans = key
        return ans