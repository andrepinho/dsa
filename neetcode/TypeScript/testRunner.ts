import { isEqual as lodashIsEqual } from "lodash";

function isEqual<T>(arg1: T, arg2: T) {
  return lodashIsEqual(arg1, arg2);
}

function test<InputType, OutputType>(
  func: (i: InputType) => OutputType,
  testCases: readonly { input: InputType; output: OutputType }[]
): void {
  console.log("Running solution:");
  testCases.forEach(({ input, output: expectedOutput }, i) => {
    const actualOutput = func(input);

    console.log(`Running test ${i + 1}`);
    if (!isEqual(actualOutput, expectedOutput)) {
      console.log(
        `Fail. Expected ${expectedOutput} but got ${actualOutput}. Input was: ${JSON.stringify(
          input
        )}`,
        "\n"
      );
    } else {
      console.log("Passed! \n");
    }
  });
}

export { test };
