from main import *

run_cases = [
    (Wall(2, 3, 4), (2, 3, 4, 24)),
    (Wall(4, 5, 6), (4, 5, 6, 120)),
    (Wall(22, 23, 24), (22, 23, 24, 12144)),
    (Wall(3, 4, 4), (3, 4, 4, 48)),
]

def test(wall, expected_output) -> bool:
    print("=============================================")
    expected_depth, expected_height, expected_width, expected_volume = expected_output
    try:
        print("Expected Wall:")
        print("  - volume: ", expected_volume)
        print("  - depth:  ", expected_depth)
        print("  - height: ", expected_height)
        print("  - width:  ", expected_width)
        print("Actual wall:")
        print("  - volume: ", wall.volume)
        print("  - depth: ", wall.depth)
        print("  - height: ", wall.height)
        print("  - width: ", wall.width)
        if (
            expected_volume == wall.volume
            and expected_depth == wall.depth
            and expected_height == wall.height
            and expected_width == wall.width
        ):
            print("Pass")
            return True

        print("Fail")
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

def main() -> None:
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
        
    if failed == 0:
        print(f"{passed} test cases passed")
        print(f"All test cases passed")
    else:
        print(f"{passed} test cases passed, {failed} test cases failed")

test_cases = run_cases

main()