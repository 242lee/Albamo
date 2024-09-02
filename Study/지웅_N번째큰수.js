const readline = require('readline');

class PriorityQueue {
    constructor() {
        this.queue = [null];
    }

    enqueue(element) {
        let insertIdx = this.queue.length;
        while (insertIdx > 1 && this.queue[Math.floor(insertIdx / 2)] >= element) {
            this.queue[insertIdx] = this.queue[Math.floor(insertIdx / 2)];
            insertIdx = Math.floor(insertIdx / 2);
        }
        this.queue[insertIdx] = element;
    }

    dequeue() {
        let delValue = this.queue[1];
        let lastValue = this.queue.pop();
        if (this.size() > 0) {
            this.queue[1] = lastValue;

            let qSize = this.queue.length - 1;
            let pIdx = 1;
            let cIdx = 2;

            while (cIdx <= qSize) {
                if (cIdx < qSize && this.queue[cIdx] > this.queue[cIdx + 1]) {
                    cIdx += 1;
                }

                if (lastValue <= this.queue[cIdx]) {
                    break;
                }

                this.queue[pIdx] = this.queue[cIdx];

                pIdx = cIdx;
                cIdx *= 2;
            }

            this.queue[pIdx] = lastValue;
        }
        return delValue;
    }

    size() {
        return this.queue.length - 1;
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let N;
let pq = new PriorityQueue();
let lineCount = 0;

rl.on('line', (line) => {
    if (lineCount === 0) {
        N = parseInt(line);
    } else {
        line.split(' ').forEach(num => {
            pq.enqueue(parseInt(num));
            if (pq.size() > N) {
                pq.dequeue();
            }
        });
    }
    lineCount++;
});

rl.on('close', () => {
    console.log(pq.dequeue());
});
