from typing import List, Dict, Any, Callable, TypeVar

T = TypeVar('T')

class TestRunner:
    @staticmethod
    def run_tests(solution_func: Callable[..., T], test_cases: List[Dict[str, Any]]) -> None:
        for case in test_cases:
            inputs = case['inputs']
            expected = case['expected']

            actual = solution_func(**inputs)
            
            if actual == expected:
                print(f"Case {inputs} passed.")
            else:
                print(f"Case {inputs} failed. Expected {expected} but Got {actual}")