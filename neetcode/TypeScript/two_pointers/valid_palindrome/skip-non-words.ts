function solution(s: string): boolean {
  if (s.length < 2) return true;

  let frontPointer = 0;
  let backPointer = s.length - 1;

  while (frontPointer < backPointer) {
    while (/\W|_/.test(s[frontPointer])) {
      frontPointer++;

      // all chars are non-word so it's a valid palindrome
      if (frontPointer > backPointer) return true;
    }
    while (/\W|_/.test(s[backPointer])) backPointer--;

    if (
      s[frontPointer].toLocaleLowerCase() != s[backPointer].toLocaleLowerCase()
    )
      return false;

    frontPointer++;
    backPointer--;
  }

  return true;
}

export { solution };
