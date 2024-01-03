export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const taskUp = false;
    const task2Up = true;
    return [taskUp, task2Up];
  }

  return [task, task2];
}
