import { test } from "../../testRunner";
import { solution as outside_in } from "./outside_in";
import { solution as brute_force } from "./brute_force";

const testCases: { input: [number[], number]; output: [number, number] }[] = [
  {
    input: [[1, 2, 3, 4], 3],
    output: [1, 2],
  },
  {
    input: [[1, 5, 6, 8], 9],
    output: [1, 4],
  },
  {
    input: [[1, 5, 6, 8], 6],
    output: [1, 2],
  },
  {
    input: [[1, 5, 6, 8], 7],
    output: [1, 3],
  },
  {
    input: [[1, 5, 6, 8], 14],
    output: [3, 4],
  },
  {
    input: [[1, 5, 6, 8], 13],
    output: [2, 4],
  },
];

test(outside_in, testCases);
test(brute_force, testCases);
