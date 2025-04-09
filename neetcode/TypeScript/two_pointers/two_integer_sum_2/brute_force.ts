function solution([numbers, target]: [number[], number]) {
  let point1 = 0;
  let point2 = 1;

  do {
    if (numbers[point1] + numbers[point2] === target) break;

    if (point2 + 1 < numbers.length) {
      point2++;
    } else {
      point1++;
      point2 = point1 + 1;
    }
  } while (numbers[point1] + numbers[point2] !== target);

  return [point1 + 1, point2 + 1];
}

export { solution };
