function solution(s: string): boolean {
  const cleanS = s.replace(/\W/g, "");

  for (let i = 0; i < cleanS.length / 2; i++) {
    const front = cleanS[i].toLocaleLowerCase();
    const back = cleanS[cleanS.length - 1 - i].toLocaleLowerCase();

    if (front != back) return false;
  }

  return true;
}

export { solution };
