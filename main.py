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


def test_standard_package():
    print("Testing STANDARD package")
    assert sort(width=100, height=80, length=25, mass=5) == "STANDARD"


def test_special_package():
    print("Testing SPECIAL package")
    assert sort(width=100, height=80, length=25, mass=50) == "SPECIAL"


def test_rejected_package():
    print("Testing REJECTED package")
    assert sort(width=100000, height=80, length=25, mass=100) == "REJECTED"


if __name__ == '__main__':
    test_special_package()
    test_standard_package()
    test_rejected_package()
    
    print(sort(width=100, height=80, length=25, mass=5))  # standard
    print(sort(width=100, height=80, length=25, mass=50))  # special
    print(sort(width=100000, height=80, length=25, mass=100))  # rejected
