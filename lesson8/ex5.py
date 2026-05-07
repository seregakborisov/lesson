class SuperStr(str):

    def is_repeatance(self, s):
        if s == "":
            return False

        return self == s * (len(self) // len(s)) and len(self) % len(s) == 0

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]