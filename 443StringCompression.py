class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        left = 0
        right = 0
        count = 0
        while right < len(chars):
            if chars[left] == chars[right]:
                count += 1
                right += 1
            elif chars[left] != chars[right]:
                s.append(chars[left])
                if count > 9:
                    for i in range(len(str(count))):
                        s.append(str(count)[i])
                elif count > 1:
                    s.append(str(count))
                left = right
                count = 0
                continue
            else:
                right += 1
        s.append(chars[left])
        if count > 9:
            for i in range(len(str(count))):
                s.append(str(count)[i])
        elif count > 1:
            s.append(str(count))
        for i in range(len(s)):
            chars[i] = s[i]

        return len(chars[:len(s)])
