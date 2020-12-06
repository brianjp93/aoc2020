import fs from 'fs'
import path from 'path'

let filename = path.join(path.dirname(process.argv[1]), 'data')
let data = fs.readFileSync(filename, 'utf8')
    .trim()
    .split('\n\n')
    .filter(x => x !== '')

let inters = []
let unions = []
for (let group of data) {
    let groupsets = group.split('\n').map(person => new Set([...person]))
    unions.push(groupsets.reduce((x, y) => new Set([...x, ...y])))
    inters.push(groupsets.reduce((x, y) => new Set([...x].filter(a => y.has(a)))))
}

console.log(unions.map(x => x.size).reduce((x, y) => x+y))
console.log(inters.map(x => x.size).reduce((x, y) => x+y))
