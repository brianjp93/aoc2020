import fs from 'fs'
import path from 'path'

let filename = path.join(path.dirname(process.argv[1]), 'data')

let data = new Set(
    fs.readFileSync(filename, 'utf8')
        .split('\n')
        .filter(x => x !== '')
        .map(item => {
            let reg = /(\d+)-(\d+) (\w): (\w+)/
            let match = reg.exec(item)
            let [_, low, high, letter, word] = match
            return [low, high, letter, word]
        })
)

let count1 = 0
let count2 = 0

for (let [low, high, letter, word] of data) {
    low = parseInt(low)
    high = parseInt(high)

    let exp = new RegExp(`${letter}`, 'g')
    let lcount = (word.match(exp) || []).length
    if (low <= lcount && lcount <= high) {
        count1 += 1
    }

    if ((word[low-1] + word[high-1]).includes(letter) && word[low-1] !== word[high-1]) {
        count2 += 1
    }
}

console.log(count1)
console.log(count2)
