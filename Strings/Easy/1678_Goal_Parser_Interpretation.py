class Solution:
    def interpret(self, command: str) -> str:
        # using the .replace() method we replace string elements as specified in the task statement
        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')
        return command
        