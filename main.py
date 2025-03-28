MAX_VOLUME = 1000000
MAX_DIMENSION = 150
MAX_HEAVY = 20


def calculate_volume(width: int, height: int, length: int) -> int:
    return width * height * length


def is_bulky(width: int, height: int, length: int) -> bool:
    if (calculate_volume(width, height, length) >= MAX_VOLUME or (width >= MAX_DIMENSION) or (height >= MAX_DIMENSION)
            or (length >= MAX_DIMENSION)):
        return True

    return False


def is_heavy(mass: int) -> bool:
    return mass >= MAX_HEAVY


def sort(width: int, height: int, length: int, mass: int) -> str:
    if is_bulky(width, height, length) and is_heavy(mass):
        return "REJECTED"

    if is_bulky(width, height, length) or is_heavy(mass):
        return "SPECIAL"

    if not is_bulky(width, height, length) or not is_heavy(mass):
        return "STANDARD"


if __name__ == '__main__':
    print(sort(width=100, height=80, length=25, mass=5))  # standard
    print(sort(width=100, height=80, length=25, mass=50))  # special
    print(sort(width=100000, height=80, length=25, mass=100))  # rejected
