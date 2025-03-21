from typing import List, Dict, Any, Callable, TypeVar

T = TypeVar('T')


class TestRunner:
    @staticmethod
    def run_tests(solution_func: Callable[..., T], test_cases: List[Dict[str, Any]]) -> None:
        for i, case in enumerate(test_cases):

            caseName = i + 1

            inputs = case['inputs']
            expected = case['expected']
            actual = solution_func(**inputs)

            # Display test results
            if actual == expected:
                print(f"Case {caseName} passed.")
            else:
                print(
                    f"Case {caseName} failed. Expected {expected} but Got {actual}")
