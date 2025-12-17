class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # s = 0
        op = ""
        operator = ['+','-','/','*']
        for i in range(len(tokens)):
            stack.append(tokens[i])
            if tokens[i] in operator:
                op = stack.pop()
                num2 = stack.pop()
                nums1 = stack.pop()
                if op == '+':
                    stack.append(int(nums1)+int(num2))
                elif op == "/":
                    stack.append(int(int(nums1)/int(num2)))
                elif op =='*':
                    stack.append(int(nums1)*int(num2))
                else:
                    stack.append(int(nums1)-int(num2))
        return int(stack[0])
