class VerboseClass:
    debug_mode = False

    def __init__(self):
        pass

    def log(self, message, minimum_verbosity = 3):
        if self.verbosity < minimum_verbosity:
            return False
        print(message)

    def set_debug_mode(self, mode):
        self.debug_mode = mode
        if self.debug_mode:
            self.verbosity = 10

    verbosity = 0

    def set_verbosity(self, verbosity):
        self.verbosity = verbosity