import fs from 'fs'
import path from 'path'

let filename = path.join(path.dirname(process.argv[1]), 'data')

let data = fs.readFileSync(filename, 'utf8')
    .split('\n')
    .filter(x => x !== '')


function find_seat(word) {
    word = word
        .replaceAll('B', '1')
        .replaceAll('L', '0')
        .replaceAll('F', '0')
        .replaceAll('R', '1')
    let row = parseInt(word.slice(0, 7), 2)
    let col = parseInt(word.slice(7), 2)
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
