import { test } from "../../testRunner";
import { solution as sort_then_two_sum } from "./sort_then_two_sum";

const testCases: { input: number[]; output: number[][] }[] = [
  {
    input: [-1, 0, 1, 2, -1, -4],
    output: [
      [-1, -1, 2],
      [-1, 0, 1],
    ],
  },
  {
    input: [0, 1, 1],
    output: [],
  },
  {
    input: [0, 0, 0],
    output: [[0, 0, 0]],
  },
];

test(sort_then_two_sum, testCases);
