# Data Structures and Algorythms

Just a place to commit my DSA exercises and studies. Feel free to check them out.

## Running exercises

Every exercise has at least one solution and a set of test cases to verify it's correctness.

There's a helper function to abstract some of of the repeated code to run solutions against test cases called `testRunner`.

To run, for example, the exercise in duplicateInteger.py, just run the command:

> `python3 -m neetcode.arraysAndHashing.duplicateInteger`

## Neetcode

I'm following [Neetcode's Rodmap](https://neetcode.io/roadmap) and solving them using Python.

## Arrays and hashing

Even thought those are very basic, they were a bit challenging as I was quite rusty with Python and this type of exercise.

In `duplicateInteger`, the naive solution would be to compare every item with every other item, that would be O(n^2) time and O(1) space. By using a hash - aka dict in Python - to store and check for values we already seen, it's possible to solve it in O(n) time with O(n) space. This tradeoff between a lot less time for a bit more space is usually well worth it.
