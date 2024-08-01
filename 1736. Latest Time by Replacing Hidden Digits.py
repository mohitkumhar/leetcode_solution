class Solution:
    def maximumTime(self, time: str) -> str:
        hr = list(time[:2])
        minutes = list(time[3:])

        if hr[0] == '?' and hr[1] == '?':
            hr[0] = '2'
            hr[1] = '3'

        elif hr[0] == '?':
            if hr[1] <= '3':
                hr[0] = '2'
            else:
                hr[0] = '1'

        elif hr[1] == '?':
            if hr[0] == '2':
                hr[1] = '3'
            else:
                hr[1] = '9'

        if minutes[0] == '?' and minutes[1] == '?':
            minutes[0] = '5'
            minutes[1] = '9'

        elif minutes[0] == '?':
            minutes[0] = '5'

        elif minutes[1] == '?':
            minutes[1] = '9'

        return ''.join(hr) + ':' + ''.join(minutes)
