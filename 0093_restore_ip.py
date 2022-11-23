def restore_ip_addresses(s):
    valid_octets = [str(x) for x in range(0, 256)]
    if len(s) > 12:
        return []
    pots = []
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                if len(s) - 4 < i + j + k < len(s):
                    pots.append((s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]))
    valids = []
    for p in pots:
        if all(o in valid_octets for o in p):
            valids.append('.'.join(p))
    return valids
    

def main():
    print(restore_ip_addresses('25525511135'))
    print(restore_ip_addresses('0000'))
    print(restore_ip_addresses('101023'))


if __name__ == '__main__':
    main()


"""
there is a backtracking solution that is more efficient since it avoids rechecking some invalid octets

class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        if idx == 4 and not s:
            res.append(path[:-1])
            return 
        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)

"""