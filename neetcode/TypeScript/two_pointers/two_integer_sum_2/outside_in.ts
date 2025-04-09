function solution([numbers, target]: [number[], number]) {
  let left = 0;
  let right = numbers.length - 1;

  while (target != numbers[left] + numbers[right]) {
    if (numbers[left] + numbers[right] < target) {
      left++;
    } else {
      right--;
    }
  }

  return [left + 1, right + 1];
}

export { solution };
