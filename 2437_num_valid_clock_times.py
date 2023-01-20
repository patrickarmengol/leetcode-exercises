class Solution:
    def countTime(self, time: str) -> int:
        minutes = tuple(time[-2:])
        hours = tuple(time[:2])

        match minutes:
            case '?', '?':
                mv = 60
            case '?', _:
                mv = 6
            case _, '?':
                mv = 10
            case _:
                mv = 1

        match hours:
            case '?', '?':
                hv = 24
            case '?', _:
                if int(hours[1]) > 3:
                    hv = 2
                else:
                    hv = 3
            case _, '?':
                if int(hours[0]) == 2:
                    hv = 4
                else:
                    hv = 10
            case _:
                hv = 1

        return hv * mv
