# Given a string s, consider all duplicated substrings: (contiguous) 
# substrings of s that occur 2 or more times. The occurrences may overlap.
# Return any duplicated substring that has the longest possible length. 
# If s does not have a duplicated substring, the answer is "".

# Constraints:
#   2 <= s.length <= 3 * 10^4
#   s consists of lowercase English letters.
from collections import defaultdict


# Binary Search + Rolling Hash (Rabin-Karp): O(n*log(n))
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def dupSub(sz: int) -> str:
            n = len(s)
            m = 2**31-1
            p = 26
            ph = 1      # hign end of power of rolling hash
            rh = 0      # rolling hash
            for i in range(sz):
                rh = (rh * p + ord(s[i]) - ord('a')) % m
                if i > 0:
                    ph = ph*p % m   # final result: ph = p^(sz-1) % m

            hashSet = defaultdict(list) # save a list of substr index, can handle hash conflict
            hashSet[rh].append(0)
            for j in range(1, n-sz+1):
                rh = ((rh + m - ph*(ord(s[j-1]) - ord('a')) % m) * p +
                       ord(s[j+sz-1]) - ord('a')) % m
                if rh in hashSet:
                    for x in hashSet[rh]:
                        if s[x: x+sz] == s[j: j+sz]:
                            return s[j: j+sz]
                hashSet[rh].append(j)
            return ''

        i, j = 1, len(s) - 1
        res = ''
        while i <= j:
            k = (i + j) // 2
            res1 = dupSub(k)
            if res1 != '':
                res = res1
                i = k + 1
            else:
                j = k - 1

        return res


# from the reality perspective, duplicate substring tends to have small length.
# So it is better to try from 1 to (n-1).
# But still O(n^2), if the longest is at the (n-1) end.
class Solution1:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        m = 2**31-1
        p = 26
        ph = 1      # hign end of power of rolling hash
        rh = 0      # rolling hash
        res = ''
        for i in range(1, n):           # substring length form 1 to n-1
            rh = (rh*p + ord(s[i-1]) - ord('a')) % m
            hashSet = defaultdict(list) # save a list of substr index, can handle hash conflict
            hashSet[rh].append(0)
            rh1 = rh
            for j in range(1, n-i+1):
                rh1 = ((rh1 + m - ph*(ord(s[j-1]) - ord('a')) % m) * p +
                       ord(s[j+i-1]) - ord('a')) % m
                if rh1 in hashSet:
                    for x in hashSet[rh1]:
                        if s[x: x+i] == s[j: j+i]:
                            res = s[j: j+i]
                            break
                    else:   # no duplicates of length i
                        continue
                    break
                else:
                    hashSet[rh1].append(j)
            else:   # no duplicates of length i
                break
            ph = ph*p % m

        return res


# Rabin-Karp - Rolling Hash: O(N^2)
# to find fixed length of duplicates is O(N), but for the longest, O(N^2)
# - The duplicated substring has length from n-1 down-to 1, where n=len(s)
# - assume value of each char is: v = ord(ch) - ord('a')
# - The initial hash function is:
#   rh = (v[0]*p^(n-1-1) + v[1]*p^(n-1-2) + ... + v[n-1-1]*p^0) % m
#   where substr length is n-1
# - because p^n could be huge, and x*p % m == ((x % m) * p) % m
#   so the %m operation is continuously applied
# - when no duplicates is found in n-1 length of substr, new hash function:
#   rh = (v[0]*p^(n-1-1) + v[1]*p^(n-1-2) + ... + v[n-1-2]*p^1) % m
#   i.e., the high end power does not change, low end power is p^1 now.
class Solution2:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        m = 2**31-1
        rh = 0
        p = 26
        ph, pl = 1, 1   # hign, low end of power of rolling hash
        for i in range(n-1):    # first rolling hash for s[0:n-1]
            rh = ((rh * p) + ord(s[i]) - ord('a')) % m
            if i > 0:   # final result: ph = p^(n-1-1) % m
                ph = ph*p % m
        for i in reversed(range(1, n)): # substring length form n-1 to 1
            hashSet = defaultdict(list) # save a list of substr index, can handle hash conflict
            hashSet[rh].append(0)
            rh1 = rh
            for j in range(1, n-i+1):
                rh1 = ((rh1 + m - ph*(ord(s[j-1]) - ord('a')) % m) * p +
                        pl*(ord(s[j+i-1]) - ord('a'))) % m
                if rh1 in hashSet:
                    for x in hashSet[rh1]:
                        if s[x: x+i] == s[j: j+i]:
                            return s[j: j+i]
                hashSet[rh1].append(j)
            if i > 1:
                rh = (rh + m - pl*(ord(s[i-1]) - ord('a')) % m) % m
                pl = pl*p % m

        return ''        

        
if __name__ == '__main__':
    def unitTest(sol):
        r = sol.longestDupSubstring(s = "banana")
        print(r)
        assert r == 'ana'

        r = sol.longestDupSubstring('abcd')
        print(r)
        assert r == ''

        s = "shabhlesyffuflsdxvvvoiqfjacpacgoucvrlshauspzdrmdfsvzinwdfmwrapbzuyrlvulpalqltqshaskpsoiispneszlcgzvygeltuctslqtzeyrkfeyohutbpufxigoeagvrfgkpefythszpzpxjwgklrdbypyarepdeskotoolwnmeibkqpiuvktejvbejgjptzfjpfbjgkorvgzipnjazzvpsjxjscekiqlcqeawsdydpsuqewszlpkgkrtlwxgozdqvyynlcxgnskjjmdhabqxbnnbflsscammppnlwyzycidzbhllvfvheujhnxrfujwmhwiamqplygaujruuptfdjmdqdndyzrmowhctnvxryxtvzzecmeqdfppsjczqtyxlvqwafjozrtnbvshvxshpetqijlzwgevdpwdkycmpsehxtwzxcpzwyxmpawwrddvcbgbgyrldmbeignsotjhgajqhgrttwjesrzxhvtetifyxwiyydzxdqvokkvfbrfihslgmvqrvvqfptdqhqnzujeiilfyxuehhvwamdkkvfllvdjsldijzkjvloojspdbnslxunkujnfbacgcuaiohdytbnqlqmhavajcldohdiirxfahbrgmqerkcrbqidstemvngasvxzdjjqkwixdlkkrewaszqnyiulnwaxfdbyianmcaaoxiyrshxumtggkcrydngowfjijxqczvnvpkiijksvridusfeasawkndjpsxwxaoiydusqwkaqrjgkkzhkpvlbuqbzvpewzodmxkzetnlttdypdxrqgcpmqcsgohyrsrlqctgxzlummuobadnpbxjndtofuihfjedkzakhvixkejjxffbktghzudqmarvmhmthjhqbxwnoexqrovxolfkxdizsdslenejkypyzteigpzjpzkdqfkqtsbbpnlmcjcveartpmmzwtpumbwhcgihjkdjdwlfhfopibwjjsikyqawyvnbfbfaikycrawcbkdhnbwnhyxnddxxctwlywjcisgqfsctzatdgqqauuvgclicdrpjcphysqdjaflpdbmvnhqggixxzcmpsysbwfkzwxzjictnngufpqhcxlbkodyrqlfomlkiefbmcfenugzqnyqqvgpxonmizkpjdlaqyyowjagzkzrzvcrupfyofeftyfvoqorzvxphhdhydnqiyiczfcgzsecxzsoaobwrixcajabjnvtoerzwayjowahrmuixmmkbtchogfizmvbjnpespxngxjxntohzatlpkcmpphmewevpteharnszafbpbexrvnbedieojezdhnyooiivhnhakilvkobxepbksnqrtxxuqhalvtjspyvporalbliiwjciamlhttaydhxoelimuorjnfvebjhcocbkrgbguwdncodskzzoqrzgavsbjcippetltqaxjhkqacwlgmsbxezqubyzeznnsoqegkykzlxohvitbmjcxllbrvgdijyovpjyeaojlyxqwnheyblznwoyikhqiutotpfukyqkvatxotulvlqzfcvskdccuixthzqrwymzccosjmjqjigehcnfphjuuybaxxukconatzseljyirycbhucxmwwftulfwfmyqyprlnsmxzyfmgjctgeunuuexhbrbsaaingqxqrjvpuhbvcmyztmkgenhonajrkzfrqjinjrbmjyinhwvlcmmxvbgvjgfmaoliosmxbonvlzoiqvkxxtoposygcgkcotohcrauivxxvmrghuauadwojxjligrgstczirnvhqpzwgjbvqzlkxltqnqrfxieggnuriytavbnouwhuamdtlspednyckixkhxedjmotiuucewllthhducwgwmgzxsbkqzfnqfynwisvsctyqdoaiypjivtxkxgoyhwhccklbdjoqykaqzljejlizgbehekmkfetvgfstmypmfnyoundudqlorcogbzoznddfalthwpmiewkmvogmzirbprjftbtffjrkrfminnechitfyfaujgtugadqbrskulsjbaunonxolauvsifevpdyurvfocxtkizflcuvltzuhwyhlbxaphifhtgkfktfnnmocpenrlujsuppbbuorvtubuiyszawzftijwhwgdyubjmmodzybiyunksuixnkariubegpdgctbayaynfskkuyhjvegsjwsbppodvhpjdjlzhxixswdncapxyfjspxeqxdfkhockvrzoisikaymoiqzqbjyoscwegfomlnurwboesfiszetebjblaolnovgvfcpnbemwambkhwcgdbhvkoluhjfxlfrfaeedocdilaboesauplmttewlbojkocklhsbzrtzeyhqtmgroupbzlymupmupsvlkzchclujuozzmngjvktzstsvocxrziuxelruwojzaleyrkjkdleavwqxwgjdbtiywqtdtaamrlcjogxufhgvoqpqkgopbtyqchzhexqgecheahjzxapqjdylzjqhzlzssbjmokncxalgasexztnlzfisxxpeerywlrjdohprewwnlwdbtwmfnnxnoolfhqqxzcvoymdbvmaoliedpvwzyvgyrwjguvoqnxrnaeqwvcfrqkwjmlvxovptultyfuxerelpfgctnpdxluqeruxkxqntosggfjqmrnlnkhhilznpycdrnemnktcsmzufpqgiraphzmgfhevzejhavsypohpttnnowfahpxfwmvxgwfuomxemdkzdlzldesmowzmhwoydnsovwykxqyllbmcurlvtwcfwxvvkxfknwwcwfjkzjtonalgijdsulcfagehiptszrcltbbypopdbmdfkyofelmrdmdbceguyxnkheqqtbletpqmjugpckmjyuuvsbqhyzmposwcgscnishluuhnwkyrkujefpgtsqrmcoortgitpdoagdncxlofkqozgngbtmlyyoyodcmcwetdtltupjrtemrjswekkfjvfecmvagyptjjuwsqpjwlxxosqhpssdvjraaicjfwvesyqfbumjjbqytkinpldxopxjzmvpigmberobyzyxwvwmlmbziduqhmbescgkvhgqtalmaxfsjlysmvrizgvrudstiwmaahtqehfbofvqwgqygvseykmgmhgjbxcrtdjqvojvyhohallyewqelzhjeuqmmsqhkluvqsfmxzbqqokehfoqrlqmwpnwojfowqpqebnuggeuvsszgfywceolvabyvbrwatuyherijsdqvpyyhdyradbammmchqkvdbxpbrxzrpfrsiiezvowrfqejibvociujtcwbygvfwojgfnvvwqlqqgipxhrogppzghtnweodaxuqxknnqnajlnsvheiycsvifvoljsncgnunsqcymnyoeeslrjflpprvtksimffvnuvakskdakvmlkpowfpfzdrcfctikhvvbagrvjlzjydnlmspzyynyjjfxnozpjjgjelipswsmfroitqphzsuqgumlnkxksbzhrsvcnfwufofhurmhksvvfjzggbtgrezkrkqmhduyqgwuwxoxaiifemtwrbilftiuhcgpjvqxldrnlzphdffncevlcyrxlpbwuswjfdegexeoooshdfqtqithpfocyowaqeedikssptyvkabhtaeotcwxccgguuotqvypugpcbwzalxwqbjdcokoxjnqhggpbbfeyjiellsikiqqtxpvzmjsfleepjpbxpeicxfcwbpprzgcrjgjaxshewradetsqsvfmcxptmksecfpynqzpctqpogcgokzrkltsbmwxkmynasohpkzjupapngusnvdjfqezqhyikllgkelewwwhhbdjvxdagnnxscjkotbbmhzkqbjwuwidrnvmztikmqjcxmcpgkoudhydmdvberfuvjnhlnfcsbpzmuquvrgogtfwefhqzkmxxgadtvjpxvurxprbsssihviypclwkjfaatzjxtvlzwaacqlwnqetgkldqaqghuihrgxbbpmjfsvaigqrhiiskkfibaeilqptkdsqqfwxeixuxgkiboaqnuaeutjcydnxyxnmattjrrxmthwvyipgazaxgrrjcvdnyxpktsldhluhicyqprxhljyfhawuvoonrwyklcdlmdvsgqrwqqomisksftsfyeifmupvylkjbagzyctuifbsrugqsbrkvskmundmczltpamhmgqespzgrkxebsvubrlmkwyqhjyljnkeqvdxtjxjvzlrubsiiahciwefwsswgssxmvyvgjrobvubcbgjomqajmotbcgqjudneovfbjtjzwqtsovzshmxeqofssukkvcdwlsdtyplrlgwtehnwvhhegtwkwnqqdiajpcaajsylesadaiflruewhrbrogbujbppunsqgytgnyuhnkejhccavaptbydtqhvyatftxcaaljyhhkkadzdhhzawgndunwwgknnbtqaddpszqgummmnomfqmdxqtwjexsbadfdqhnyixjslsaisscocbabivzokkgiinqqzsrtfpzjmxfkqmuzzlelqjtjidjarkwbwlcqrefokrlwdmuzyffdtajnqoimlzzpcgpjjwlqkusefzbgznhexzojxnzxmmedobgvdabtdoiskozrdrjscxwivaekrkyyfynuktmgyziteavdxfctvkfkrmsdwpaywzbkeojeycwdkectydojttisizruilwokhepscqdnjygiakomkhyujaffxjyxqmvkemqihpcdygprdeaxgjbkonfvgtzayfbmgwsskoyxjlknwwtehhhpjllhkcblyaxnbekoidbbyqvdqqsyfcemylmqskpxifcnhmemkkitqtbfwhmyemkzightkjbhlquticivpeeclpamsqoztxvdtcqbsonxyecnhcadtghkjckhrcdfggnqlwurydzbeybqkcfnnbwkciwaqdzgmcrbltvcuftxsqfpxnoombsbeoqxivgtkrjklxatgcorkdrvmngwlekeopgecefzxtprcoajoopxviijxilxfiwuajsbtcctfcqqgzhyjmonwdbyjlnneidyaqhhothzpzaxcthvbxpdcqofaeamxbqjwhunnqwclhcqhagawjsxygorgbuqryzickyplbaivkabbrkibqzqacabbwmnpndaqvbknbqcjuywxjrdbznndomwbbqfgulwczydrhrocebhygriiwxmwtjjyqqiqrjblxuamddlsiocdoysdaacuovljtpgocephnxuugdyggsnhcqiqhulyhlxiwzvhrtbmvjnhacwunckqzhpcthqgsupptdwkfeprbg"
        r = sol.longestDupSubstring(s)
        print(r)
        assert r == 'maoli'

    unitTest(Solution())
    unitTest(Solution1())
    # unitTest(Solution1())
