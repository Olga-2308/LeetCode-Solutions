class Solution:
    def defangIPaddr(self, address: str) -> str:

        # using the string method we replace '.' to '[.]'
        new_address = address.replace('.', '[.]')

        return(new_address)
        