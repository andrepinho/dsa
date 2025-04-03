const bracketPairs = {
  ")": "(",
  "]": "[",
  "}": "{",
} as const;

type openingBracketType = (typeof bracketPairs)[keyof typeof bracketPairs];
type closingBracketType = keyof typeof bracketPairs;

function isOpeningBracket(char: string): char is openingBracketType {
  return (Object.values(bracketPairs) as readonly string[]).includes(char);
}

function isClosingBracket(char: string): char is closingBracketType {
  return (Object.keys(bracketPairs) as readonly string[]).includes(char);
}

function mySolution(s: string): boolean {
  if (s.length == 0) return false;
  if (s.length % 2 != 0) return false;

  let openingStack: (typeof bracketPairs)[keyof typeof bracketPairs][] = [];

  for (const c of s) {
    if (isOpeningBracket(c)) {
      openingStack.push(c);
    } else if (isClosingBracket(c)) {
      if (openingStack.length === 0 || openingStack.pop() !== bracketPairs[c])
        return false;
    }
  }

  return openingStack.length === 0;
}

export { mySolution };
