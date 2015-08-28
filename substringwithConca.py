class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if S == "" or L == []:
            return []
        win = len(L[0])
        l = len(L)
        result = []
        totalHash = 0
        Map = set()
        for word in L:
            Map.add(word)
            totalHash += hash(word)
        for i in range(len(S)-win*l+1):
            if S[i:i+win] not in Map:
                continue
            tmpHash = 0
            j = i 
            while j < i+win*l:
                tmp = S[j:j+win]
                if tmp in Map:
                    tmpHash += hash(tmp)
                else:
                    break
                j += win
            if tmpHash == totalHash:
                result.append(i)
        return result


a = Solution()
S="baauxdthqwzuleorburxbkrksgpgchndjqygttnmsnidtwuutotwylhqtwyvfoboebvxukjozrssqonjcifctmsmktkphlelmbkinwxnnrhfhwokfwmaihptazkjmowargifchusybxgyosfkgfupunpvyahowhgdsnhbhbakziipcpzivtyrjpnjqwxogftaubbbcdmdnwspmtajpaayrpjjogyworwiszmxfacswxkkqkthmwhdnqnbzlzncxxxxjwclywixguosoxemfizvxduicjmajlzujbgizofgivyytdmanmxkrsuvdixmwwjfzpnzfvhpsfqnkcnxqljjfffkoezkbircxfdecktwslkcozceklqrrvchzdtclkhkrmotzjqrvctlbvrojhfcejjgmcizmrjgezzdlrwgvptxnknyssawejcsnnsbgdhmdjroanwyfpvuzistcssidwbqjvrsyzediytklpisgfminebsyvabsdtdylvzmccuaygnnrgwwsemzhezdgbvkuykhwltyqpaoyndptzlodxnndmqkplwmlivjwpjmgjcexftshhgmgvzkkpwbcupqelzacloiuqptwkofrurasrkegiflcvbgichknvuiojdmwrrpoipizbmijrtlouuwydimadwoozamtrcjatrbvdjewcsnymjxrujrxhgniiabaemcxddugnzfrtsqfdnyxypwfvmpgorgsdkrjpmrclwwgomnublrbaqiycxeqqmkwwbflnwqatmijavfdgzehpmhtlljcxvyvwdgmbyowmximsnrzmvidjpwvchxbcxwzaenbfbyraggtvxuivelevkbxryauvwvxcibhlbbmjhfeebozfcgamhzdizxfxsdzcgjohkasrhwxinzpphpboogwpeemyjnbpwryirqzaozibazshotveautgyhgjuhytyybrodtecdgccalqugwwcrecykltujoujpmzsfewlmanmleiscewukzsvknpwbjftxflfliqxkdlwjuqmamglnagyoxwrgdkgkwlvgbuqggoqaeeatkngktgascszicfsasqivkbbqprswvvphivueeuwgoxotejvwzerjhtcwmuukrjtahnelkctyaktgtpduvwdcrhaeevqvgjvnzbajgujggfmzurtroyvfivlmsdhznfomipxolgwrllshcnysnvavrnjlrtmgadsisrzfxvylgqslftfsohqhxzvoshuskodefclexjrgbmtgfabvirffscvnjrfwhkcomqumzmudypjfpmczdjgwlbjxuqvdbxrpnmdpyxsyoddeqfdvpmtcpczkvunyuhpjvtytssthywnqdqlscfvsjweertelauuxnvqhpjonhbdlurfywcshzymqsqdumzszukhkwxzdbdqxuwxsaqzzonrigufswxssjbcfaeldhdadzyxaqwbgmtpspwkntegc"
L=["aayrpjjogyworwiszmxfacsw","jvrsyzediytklpisgfminebs","wxogftaubbbcdmdnwspmtajp","nhbhbakziipcpzivtyrjpnjq","nmxkrsuvdixmwwjfzpnzfvhp","cjmajlzujbgizofgivyytdma","vptxnknyssawejcsnnsbgdhm","sfqnkcnxqljjfffkoezkbirc","kphlelmbkinwxnnrhfhwokfw","zdtclkhkrmotzjqrvctlbvro","jwclywixguosoxemfizvxdui","vxukjozrssqonjcifctmsmkt","djroanwyfpvuzistcssidwbq","idtwuutotwylhqtwyvfoboeb","wsemzhezdgbvkuykhwltyqpa","xfdecktwslkcozceklqrrvch","bcupqelzacloiuqptwkofrur","xgyosfkgfupunpvyahowhgds","jhfcejjgmcizmrjgezzdlrwg","rxbkrksgpgchndjqygttnmsn","maihptazkjmowargifchusyb","oyndptzlodxnndmqkplwmliv","jwpjmgjcexftshhgmgvzkkpw","yvabsdtdylvzmccuaygnnrgw","xkkqkthmwhdnqnbzlzncxxxx"]
S1 = "barfoothefoobarman"
L1 = ["foo","bar"]
print a.findSubstring(S1,L1)