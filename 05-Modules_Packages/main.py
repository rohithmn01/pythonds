from pricing import *
from product import *
import sys

def main():
    tax = get_tax(100)
    print(tax)

    for path in sys.path:
        print(path)

if __name__ == '__main__':
    main()
#__name__ = dunder name (dunder stands for double underscores)
# the main() functions gets called only when this script is executed directly
# https://www.youtube.com/watch?v=CqvZ3vGoGs0&t=1156s