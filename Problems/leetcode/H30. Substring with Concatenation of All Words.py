from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words : list[str])-> list[int] :
        result = []
        words_count = defaultdict(int)
        word_len = len(words[0])
        substr_len = len(words) * word_len

        for k in words:
            words_count[k] += 1
       
        for v in range(len(s) -substr_len +1):
            seen = defaultdict(int)
            for w in  range(v , v+substr_len, word_len):
                word = s[w : w+word_len]
                if word  in words_count:
                    seen[word] += 1
                    if seen[word] > words_count[word]:
                        break
                else:
                    break
            else:
                result.append(v)
        return result 



s = Solution()
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","the","foo"]))