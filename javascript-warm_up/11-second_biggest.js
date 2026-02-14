#!/usr/bin/node

const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let second = -Infinity;
  for (const num of args) {
    if (num < max && num > second) {
      second = num;
    }
  }
  console.log(second === -Infinity ? 0 : second);
}
