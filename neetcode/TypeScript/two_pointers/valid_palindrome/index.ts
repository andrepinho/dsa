import { test } from "../../testRunner";
import { solution } from "./clean_and_compare_from_both_ends";
import { solution as solution2 } from "./skip-non-words";

const testCases = [
  {
    input: "A man, a plan, a canal: Panama",
    output: true,
  },
  {
    input: "race a car",
    output: false,
  },
  {
    input: " ",
    output: true,
  },
  {
    input: "a_b",
    output: false,
  },
  {
    input: "A_b,c'D@e: EdCbA",
    output: true, // This should be true (A, b, c, D, e = e, D, c, b, A)
  },
  {
    input: "0_0",
    output: true, // Make sure numbers work correctly
  },
  {
    input: "0P0",
    output: true, // Mixed case with numbers
  },
  // Empty string edge case
  {
    input: "",
    output: true, // Empty string is a palindrome
  },
  // Single character edge case
  {
    input: "a",
    output: true, // Single character is always a palindrome
  },
  // All non-alphanumeric
  {
    input: "!@#$%^&*()",
    output: true, // After filtering, it's empty which is a palindrome
  },
  // Unicode characters
  {
    input: "Madam, I'm Adam.",
    output: true, // Classic palindrome with punctuation
  },
  // Long palindrome
  {
    input: "A Santa at NASA",
    output: true,
  },
  // Case sensitivity check
  {
    input: "AbBa",
    output: true, // Should ignore case
  },
  // Almost palindrome
  {
    input: "abcda",
    output: false, // Not a palindrome
  },
  // With leading/trailing spaces
  {
    input: "  race a car  ",
    output: false, // Spaces should be filtered out
  },
  {
    input: "a!@#$%^&*()a",
    output: true,
  },
  {
    input: ".,;",
    output: true,
  }, // Mixture of alphanumeric and special chars
  {
    input: "a_b:c,b_a",
    output: true, // Should ignore special chars
  },
  {
    input: "a_b:c,d_a",
    output: false, // Not a palindrome after ignoring special chars
  },
  // Unicode characters
  {
    input: "Été",
    output: true, // With accented characters
  },
  // With empty space at one end
  {
    input: "a b a ",
    output: true, // Space at the end only
  },
  {
    input: " a b a",
    output: true, // Space at the beginning only
  },
  // Nested special characters
  {
    input: "a!b@c#d$c%b^a",
    output: true, // Palindrome with nested special chars
  },
  // Almost palindromes
  {
    input: "ab!@#$%^&*()ba",
    output: true, // Valid palindrome after filtering
  },
  {
    input: "ab!@#$%^&*()ca",
    output: false, // Not valid after filtering
  },
  // Very long palindrome
  {
    input:
      "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.",
    output: true, // Long palindrome with punctuation
  },
  // Out-of-bounds potential
  {
    input: "a" + "!".repeat(1000) + "a",
    output: true, // Many special chars in the middle
  },
  // Special case: only one alphanumeric character
  {
    input: "!@#a$%^",
    output: true, // Only one alphanumeric char is trivially a palindrome
  },
  // Special characters with numbers
  {
    input: "1!2@3#3$2%1",
    output: true, // Numbers should work the same as letters
  },
  // Case sensitivity edge case
  {
    input: "A man, a plan, a canal: PanAMa",
    output: true, // Mixed case
  },
];

// test(solution, testCases);

test(solution2, testCases);
