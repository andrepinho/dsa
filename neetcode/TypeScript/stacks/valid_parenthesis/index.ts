import { test } from "../../testRunner";
import { mySolution } from "./solution";

const testCases = [
  {
    input: "()",
    output: true,
  },
  {
    input: "()[]{}",
    output: true,
  },{
    input: "(]",
    output: false,
  },{
    input: "([)]",
    output: false,
  }
]


test(mySolution, testCases);
