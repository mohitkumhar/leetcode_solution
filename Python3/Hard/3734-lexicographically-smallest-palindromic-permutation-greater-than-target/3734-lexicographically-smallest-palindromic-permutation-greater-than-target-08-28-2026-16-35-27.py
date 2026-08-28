class Solution:

    def build_palindrome(self, half: str, middle: str) -> str:
        return half + middle + half[::-1]

    def smallest_greater_or_equal(self, original_count, target_half: str) -> str:
        count = original_count[:]
        k = len(target_half)
        matched = 0

        while matched < k and count[ord(target_half[matched]) - ord('a')] > 0:
            count[ord(target_half[matched]) - ord('a')] -= 1
            matched += 1

        if matched == k:
            return target_half

        for pos in range(matched, -1, -1):
            if pos < matched:
                count[ord(target_half[pos]) - ord('a')] += 1

            current = ord(target_half[pos]) - ord('a')

            for c in range(current + 1, 26):
                if count[c] == 0:
                    continue

                result = target_half[:pos] + chr(ord('a') + c)
                count[c] -= 1

                for ch in range(26):
                    result += chr(ord('a') + ch) * count[ch]

                return result

        return ""

    def next_permutation(self, chars) -> bool:
        pivot = len(chars) - 2

        while pivot >= 0 and chars[pivot] >= chars[pivot + 1]:
            pivot -= 1

        if pivot < 0:
            return False

        swap_pos = len(chars) - 1

        while chars[swap_pos] <= chars[pivot]:
            swap_pos -= 1

        chars[pivot], chars[swap_pos] = chars[swap_pos], chars[pivot]

        chars[pivot + 1:] = reversed(chars[pivot + 1:])

        return True

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch) - ord('a')] += 1

        middle = ""
        odd_count = 0

        for c in range(26):
            if frequency[c] % 2 == 1:
                odd_count += 1
                middle = chr(ord('a') + c)

        if odd_count > 1:
            return ""

        half_count = [count // 2 for count in frequency]
        k = len(s) // 2
        target_half = target[:k]

        half = self.smallest_greater_or_equal(half_count, target_half)

        if not half and k > 0:
            return ""

        candidate = self.build_palindrome(half, middle)

        if candidate > target:
            return candidate

        chars = list(half)

        if not self.next_permutation(chars):
            return ""

        return self.build_palindrome("".join(chars), middle)