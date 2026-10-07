class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        while x != 0:
            # 取出带符号的末位数字
            digit = x % 10
            if x < 0 and digit != 0:
                digit -= 10

            # 去掉末位，向 0 截断
            x = (x - digit) // 10

            # 检查追加 digit 后是否超过最大值
            if result > 214748364:
                return 0
            if result == 214748364 and digit > 7:
                return 0

            # 检查追加 digit 后是否低于最小值
            if result < -214748364:
                return 0
            if result == -214748364 and digit < -8:
                return 0

            result = result * 10 + digit

        return result
        