# Built by Tejas Deolasee

#########################################################################################


class BodMasOperator:

    def __init__(self, string):
        self.string = string 
        self.answer = 0
        self.calculate()

#########################################################################################

    def calculate(self):

        expression = self.string
        expression = expression.replace(" ", "")

        stack = []

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = ""
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                stack.append(int(num))
                continue

            if expression[i] == '(':
                stack.append('(')
            elif expression[i] == ')':
                while stack[-1] != '(':
                    self.performOperation(stack)
                stack.pop()
            else:
                while stack and self.hasPrecedence(expression[i], stack[-1]):
                    self.performOperation(stack)
                stack.append(expression[i])
            
            i += 1
        
        while stack:
            self.performOperation(stack)
        
        self.answer = stack[-1]

#########################################################################################

    def hasPrecedence(self, op1, op2):
        if op2 == '(' or op2 == ')':
            return False
        if (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
            return False
        return True

#########################################################################################

    def performOperation(self, stack):
        if len(stack) < 3:
            return
        
        num2 = stack.pop()
        operator = stack.pop()
        num1 = stack.pop()
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        
        stack.append(result)

#########################################################################################
