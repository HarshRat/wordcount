class Wc:
    def __init__(self, st):
        self.st = st

    def characters(self):
        return len(self.st)

    def words(self):
        if ":" in self.st:
            return len(self.st.split()) + self.st.count(":")
        return len(self.st.split())


def main():
    st = input("Enter a string: ")
    chars = Wc(st).characters()
    words = Wc(st).words()
    print("Characters:", chars)
    print("Words:", words)


if __name__ == '__main__':
    main()
