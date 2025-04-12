function solution(nums: number[]): number[][] {
  let result = [];

  const sorted = nums.sort((a, b) => a - b);

  for (const [i, n] of sorted.entries()) {
    if (i > 0 && sorted[i - 1] === n) continue;

    let [left, right] = [i + 1, sorted.length - 1];

    while (left < right) {
      const threeSum = n + sorted[left] + sorted[right];

      if (threeSum > 0) {
        right--;
      } else if (threeSum < 0) {
        left++;
      } else {
        result.push([n, sorted[left], sorted[right]]);

        left++;
        right--;

        while (sorted[left] === sorted[left - 1]) {
          left++;
        }
        while (sorted[right] === sorted[right + 1]) {
          right--;
        }
      }
    }
  }

  return result;
}

export { solution };
