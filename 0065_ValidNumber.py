# A valid number can be split up into these components (in order):
# - A decimal number or an integer.
# - (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):
# - (Optional) A sign character (either '+' or '-').
# - One of the following formats:
#   - One or more digits, followed by a dot '.'.
#   - One or more digits, followed by a dot '.', followed by one or more digits.
#   - A dot '.', followed by one or more digits.
# An integer can be split up into these components (in order):
# - (Optional) A sign character (either '+' or '-').
# - One or more digits.
# For example, all the following are valid numbers:
#   ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", 
#    "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
# while the following are not valid numbers:
#   ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
# Given a string s, return true if s is a valid number.
# Constraints:
#   1 <= s.length <= 20
#   s consists of only English letters (both uppercase and lowercase),
#       digits (0-9), plus '+', minus '-', or dot '.'.


# Deterministic Finite Automaton (DFA), or Deterministic Finite-State Machine (DFSM)
# Analysis:
# - state      meaning          condition         next_state
#       0      start            sign(+/-)         1
#                               digit(0~9)        2
#                               dot(.)            4
#    
#       1      (number sign)    digit(0~9)        2
#                               dot(.)            4
#    
#       2      integer          digit(0~9)        2
#                               dot               3
#                               exp(e/E)          5
#    
#       3      decimal          digit(0~9)        3
#                               exp(e/E)          5
#
#       4      (dot without     digit(0~9)        3
#               digit prefix)
#    
#       5    (exponent to be    sign(+/-)         6
#            followed by int)   digit(0~9)        7
#    
#       6      (exponent sign)  digit(0~9)        7
#
#       7      number           digit(0~9)        7
# - At the end, the valid number should be in state 2, 3, or 7.
class Solution:
    def isNumber(self, s: str) -> bool:
        machine = [{'sign': 1, 'digit': 2, 'dot': 4},
                   {'digit': 2, 'dot': 4},
                   {'digit': 2, 'dot': 3, 'exp': 5},
                   {'digit': 3, 'exp': 5},
                   {'digit': 3},
                   {'sign': 6, 'digit': 7},
                   {'digit': 7},
                   {'digit': 7}
                  ]

        state = 0
        for ch in s:
            if ch.isdigit():
                condition = 'digit'
            elif ch in ('+', '-'):
                condition = 'sign'
            elif ch == '.':
                condition = 'dot'
            elif ch in ('e', 'E'):
                condition = 'exp'
            else:
                return False
            
            if condition in machine[state]:  # type: ignore
                state = machine[state][condition]
            else:
                return False

        return state in (2, 3, 7)


# Logic and Flow Control:
# - works, but the code is not so clear
class Solution1:
    def isNumber(self, s: str) -> bool:
        checkLeadingSign = True
        checkDecimal = True
        checkExp = True
        digitsAppeared = False
        for ch in s:
            if checkLeadingSign:
                checkLeadingSign = False
                if ch in ('+', '-'):
                    continue
            if ch in ('+', '-'):
                return False
            elif ch == '.':
                if not checkDecimal:
                    return False
                checkDecimal = False
            elif ch in ('e', 'E'):
                if not checkExp or not digitsAppeared:
                    return False
                checkExp = False
                checkDecimal = False
                checkLeadingSign = True
                digitsAppeared = False
            elif ch.isdigit():
                digitsAppeared = True
            else:
                return False

        return  digitsAppeared


if __name__ == '__main__':
    def unit_test(sol):
        for s in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", 
                  "0", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
            r = sol.isNumber(s)
            print(r, s)
            assert r == True

        for s in ["e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
            r = sol.isNumber(s)
            print(r, s)
            assert r == False

    unit_test(Solution())
    unit_test(Solution1())
