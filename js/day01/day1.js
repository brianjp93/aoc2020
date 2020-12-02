import fs from 'fs'
import path from 'path'

let filename = path.join(path.resolve(), 'data')

let data = new Set(
    fs.readFileSync(filename, 'utf8')
        .split('\n')
        .filter(x => x !== '')
        .map(item => parseInt(item.trim()))
)

function find_group(nums, n, count) {
    if (n < 0) {
        return null
    }
    for (let i of nums) {
        if (count <= 2) {
            if (nums.has(n-i)) {
                return [i, n-i]
            }
        }
        else {
            let copy = new Set(nums)
            copy.delete(i)
            let possible = find_group(copy, n-i, count-1)
            if (possible) {
                possible.push(i)
                return possible
            }
        }
    }
    return null
}

console.log(find_group(data, 2020, 2))
console.log(find_group(data, 2020, 3))
