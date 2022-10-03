def num_rolls_to_target(n, k, target):
    def rec_roll(rem_dice, rem_total, memo={}):
        # quick check for impossible to reach targets
        if rem_dice * k < rem_total or rem_dice > rem_total:
            return 0
        
        # base cases
        if rem_dice == 0: # out of dice
            if rem_total == 0:
                return 1
            else:
                return 0
        if rem_total < 0: # overshot target
            return 0
        
        # check memo if we've already done this
        if (rem_dice, rem_total) in memo:
            return memo[(rem_dice, rem_total)]
        
        # recurse to get num ways for each die result
        ways = 0
        for i in range(1, k + 1):
            ways += rec_roll(rem_dice - 1, rem_total - i)
        memo[(rem_dice, rem_total)] = ways

        return ways
    
    return rec_roll(n, target) % (10 ** 9 + 7)

        
# right idea but wayyy too slow
def orig_rec_roll(n, k, target, s, combos):
    if n == 0 and s == target:
        return (combos + 1) % (10**9 + 7)
    elif s > target: # overjumped target
        return combos
    elif n <= 0: # out of rolls
        return combos
    elif n * k < target - s: # not enough max rolls to reach target
        return combos
    for i in range(1, k + 1):
        #print(i, target, s + i)
        combos = rec_roll(n - 1, k, target, s + i, combos)
    return combos




def main():
    print(num_rolls_to_target(1, 6, 5))
    print(num_rolls_to_target(2, 6, 7))
    print(num_rolls_to_target(30, 30, 500))

    #print(num_rolls_to_target(4, 6, 14))

if __name__ == '__main__':
    main()