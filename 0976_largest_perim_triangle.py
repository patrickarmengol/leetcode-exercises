import itertools

def largest_perimeter(nums: list[int]) -> int:
    def valid_triangle(a: int, b: int, c: int) -> bool:
        return (a + b > c) and (b + c > a) and (a + c > b)
    
    sl = sorted(nums, reverse=True)
    print(sl)
    for i in range(0, len(sl) - 2):
        for j in range(i + 1, len(sl) - 1):
            for k in range(j + 1, len(sl)):
                a, b, c = sl[i], sl[j], sl[k]
                if valid_triangle(a, b, c):
                    return a + b + c
                else:
                    break
    return 0

def better_largest_perimeter(nums: list[int]) -> int:
    sl = sorted(nums, reverse=True)
    for i in range(0, len(sl) - 2):
        if sl[i] < sl[i + 1] + sl[i + 2]:
            return sl[i] + sl[i + 1] + sl[i + 2]
    return 0

def main():
    #print(largest_perimeter([2, 1, 2]))
    #print(largest_perimeter([1, 2, 1]))
    #print(largest_perimeter([3, 2, 3, 4]))
    #print(largest_perimeter([260318,833310,915317,132443,171985,926435,77036,99099,236978,961229,39004,986277,605451,294419,687921,189987,217625,123472,238857,813620,508593,561489,487326,690513,57665,282320,338487,669746,826641,953494,656869,69260,404982,325324,173267,178254,58130,434365,203944,131349,540812,304242,765614,431551,247611,939790,237253,512943,279527,618108,392578,143817,828057,300391,876376,971398,256744,828230,195701,682772,172046,308497,445628,952708,844116,815206,489482,709905,934633,300606,1797,949550,401091,28423,988538,242662,74099,430080,191273,787903,860369,380329,706080,520381,311943,458676,917916,415401,47738,124694,747558,998172,428591,975611,600955,105722,878415,883747,317297,890877,312313,673054,870936,136610,149099,117921,323181,209112,765149,414883,448149,365233,690914,657019,449965,890361,961166,703661,24608,736376,518245,615474,122216,305809,140233,454491,566737,135725,77771,231430,777663,946254,693829,27981,227992,711704,276712,997622,467658,88519,635393,759744,710806,914483,161061,600984,669874,429519,69286,397512,376755,482078,339901,460248,78679,249931,173541,730598,640404,584389,458778,47960,369692,744514,450413,199966,39511,508115,735678,82395,329790,626947,920227,81671,131575,485220,343931,730039,970769,476062,464402,80770,663312,252520,618837,239352,199543,155835,880752,380656,798205,588094,889915,217160,84105,497752,269953,249714,794161,682734,699389,562218,392533,312016,856340,586391,456008,434001,165875,511553,354737,959244,777986,912672,257107,295487,402536,570508,326342,534968,332638,962046,145717,228532,560037,618911,985313,682883,774820,86524,354141,493245,823990,23889,249470,240422,377317,810465,934430,600924,270387,841059,817814,874078,646778,431665,425436,962643,247390,661794,398621,701347,638739,349654,802750,37512,267606,583811,330091,992908,761832,762783,811840,84452,803802,438756,330924,896374,575255,471992,969513,731475,917506,636610,845814,133994,988013,31588,5812,528636,321265,103708,68585,906641,924749,178085,436840,833840,76417,212640,29781,632153,316897,363662,557460,141349,618311,311376,805905,760992]))
    print(better_largest_perimeter([77,53,76,84,63,77,39,38,97,26841,29,93,87,85,31,88,43447,100,44,6,21,22,6,30,13,27,8,1,48,92,74,89,70,54,61,69,72,98,24,76,85,67,83,4,3,72,100,59,10,75,19,100,70,82,81,7,73,5,78,50,1,72,11,85,44,77,80,10,1,10,41,82,71,11,38,40,66,2,62,49,33,58,93,36,58,42,30,70,34,12,46,51,99,32,69,49,50,64,66,100,14,7,30,62,21,12,52,52,81,27,72,27,10,93,75,91,98,36,23,12,34,53,86,25,73,68,16,6325,1,54,39,47,39,85,94,33,100,27,3,85,82,29,1,6,15,1,53,34,78,3906,80,52,62,59,7,48,83,41,47,100,98,7,4,66,7,31,42,34,4,46,18,68,9,95,12,32,31,16,57,76,85,86,53,29,9,31,3,15,80,75,36,8,20,85,13,3,42,8,28,10,8,21,80,95,74,60,79,79,45,562,20,45,42,46,1,49,2,62,45,36,41,35,66,71,56,25,20,32,59,86,15,5,44,55,76,89,40,8,20,24,54,75,2,72,36,17,78,48,8,71,63,94,51,69,72,94,32,73,29,48,8,84,13,85,30,6,77,14,77,17,54,58,81,61,74,63,3,33,32,56,29,20,49,3,100,78,94,24,24,63,46,94,26,30,76,62,35,33,96,58,58,18,77,72,26,35,96,83,57,69,99,59,85,57,6,37,2,27,50,24,54,61,13,36,74,80,14,16,36,72,27,30,46,28,28,47,91,91,73,34,39,68,17,73,9,8,34,61,82,12,66,75,61,45,56,38,13,86,65,2,56,8,2,70,64,76,10,17,10,53,7,71,41,46,59,88,23,67,91,31,12,72,74,6,89,18,75,41,50,8,10,79,82,67,47,48,1,55,70,23,24,22,94,31,34,46,43,481886,85,82,33,99,9,9,5,64,65,57,67,13,38,12,66,11,63,35,30,34,29,21,6,5,73,26,42,83,100,78,47,12,48,44,95,79,99,43,90,3,56,64,32,28,9,43,64,95,92,65,5,72,44,29,20,33,20,73,82,37,24,33,54,48,37,8,95,94,32,99,28,49,19,48,67,88,29,67,55,67,31,75,53,28,86,32,41,16586,16,76,81,40,90,86,59,36,29,41,93,40,39,95,18,63,13,9,79,97,28,24,14,54,19,5,88,73,53,93,6,90,15,85,1,78,48,83,30,3,27,84,45,47,71,93,69,34,62,71,15,52,74,97,62,41,62,66,36,26,49,83,31,80,60,2401,72,19,23,21,86,41,13,68,15,54,85,29,46,55,31,94,71,3,36,31,95,26,50,40,70292,11,98,7,32,2,83,7,22,78,66,47,76,100,9,60,34,30,89,28,73,32,6,39,70,73,20,63,52,78,67,81,32,76,91,27,28,52,30,297820,7,33,27,3,10,17,70,91,100,94,53,100,44,83,98,61,31,96,22,84,2,2,97,58,17,57,7,19,10,63,60,64,74,2,36,95,53,97,1,42,50,96,66,14,26,39,50,22,31,48,42,68,24,30,30,59,14,96,56,84,77,73,98,59,85,1488,57,41,93,20,28,68,49,41,7,184049,14,73,89,56,7,84,43,22,28,91,74,58,100,65,65,57,51,44,94,73,13,4,13,64,32,73,3,7,66,97,29,48,33,46,80,63,91,8,84,12,24,4,58,44,77,125,67,64,100,64,12,11,87,57,96,56,27,49,71,113756,77,19,26,91,63,92,19,78,80,74,29,908,98,28,85,56,11,22,37,5,42,56,96,21,3,85,54,24,34,1,73,62,41,39,86,81,29,13,205,65,35,85,77,88,70,72,20,4,82,33,83,77,83,41,21,80,29,83,38,48,28,26,87,47,59,95,2,24,93,57,16,12,100,76,31,66,75,50,84,34,93,23,71,51,71,13,5,66,57,26,17,27,91,22,57,39,88,33,16,56,23,43,97,51,60,95,4,95,59,97,96,84,44,79,18,30,80,58,95,56,9,16,78,89,779723,49,51,44,26,18,61,56,97,98,64,77,19,91,4,100,33,345,26,27,57,79,60,40,38,25,77,60,21,2,11,35,21,68,8,89,62,86,76,71,71,60,58,2,6,13,21,51,69,24,2,2,72,44,55,10245,64,44,5,76,76,80,91,67,60,29,67,87,82,25,90,25,63,35,88,48,87,8,39,47,46,36,12,73,18,62,56,69,43,26,50,19,71,63,50,12,81,76,4,41,91,53,2,94,89,37,68,70,94,51,62,16,32,32]))

if __name__ == '__main__':
    main()


"""
wow, maybe i should have spent some more time thinking about this one
if sl[i] > sl[i + 1] + sl[i + 2], then of course sl[i] > sl[i + 1] + sl[i + 3]
so checking every combination was useless
"""