import fs from 'fs'
import path from 'path'

let filename = path.join(path.dirname(process.argv[1]), 'data')

let data = fs.readFileSync(filename, 'utf8')
    .split('\n')
    .filter(x => x !== '')

const TREE = '#'
function count_trees_on_slope(data, dx, dy) {
    const max_x = data[0].length
    const max_y = data.length
    let x = 0
    let y = 0
    let count = 0
    while (y < max_y) {
        if (data[y][x%max_x] === TREE) {
            count++
        }
        x += dx
        y += dy
    }
    return count
}

let slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
let counts = slopes.map(([x, y]) => count_trees_on_slope(data, x, y))

console.log(`Part 1: ${counts[1]}`)
console.log(`Part 2: ${counts.reduce((x, y) => x*y)}`)
