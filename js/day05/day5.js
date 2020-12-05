import fs from 'fs'
import path from 'path'

let filename = path.join(path.dirname(process.argv[1]), 'data')

let data = fs.readFileSync(filename, 'utf8')
    .split('\n')
    .filter(x => x !== '')


function find_seat(word) {
    let part1 = word.slice(0, 7)
    let part2 = word.slice(7)
    let start = 1
    let end = 128
    for (let ch of part1) {
        let size = end - start + 1
        if (ch == 'F') {
            end -= Math.floor(size / 2)
        }
        else if (ch == 'B') {
            start += Math.floor(size / 2)
        }
    }
    let row = start - 1

    start = 1
    end = 8
    for (let ch of part2) {
        let size = end - start + 1
        if (ch == 'L') {
            end -= Math.floor(size / 2)
        }
        else if (ch == 'R') {
            start += Math.floor(size / 2)
        }
    }
    let col = start - 1
    return [row, col]
}

function find_my_seat(seat_ids) {
    let seat_id_set = new Set(seat_ids)
    for (let x of seat_id_set) {
        if (!seat_id_set.has(x+1) && seat_id_set.has(x+2)) {
            return x + 1
        }
    }
}

let seat_ids = data.map(line => {
    let [row, col] = find_seat(line)
    return row * 8 + col
})
let my_seat = find_my_seat(seat_ids)

console.log(`Part 1: ${Math.max(...seat_ids)}`)
console.log(`Part 2: ${my_seat}`)
