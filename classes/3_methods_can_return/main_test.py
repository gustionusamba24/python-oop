from main import *

run_cases = [
    (Wall(), [50, 100, 200]),
    (Wall(), [50, 100, 200, 400, 800, 1600, 3200]),
]

def test(wall: type, expected_outputs: list[int]) -> bool:
    print("=========================================")
    actual_outputs = []
    for _ in expected_outputs:
        cost = wall.get_cost()
        actual_outputs.append(cost)
        print(f"Wall cost: {cost}")
        wall.fortify()
        print("fortifying wall...")
    print(f"Expected output: {expected_outputs}")
    print(f"Actual output: {actual_outputs}")

    if actual_outputs == expected_outputs:
        print("Pass")
        return True
    
    print("Fail")
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