class PowerOfTwoMaxHeap {
    constructor(x) {
      if (x < 0) {
        throw new Error("The exponent x must be non-negative.");
      }
      this.childFactor = Math.pow(2, x);
      this.heap = [];
    }
  
    insert(value) {
      this.heap.push(value);
      this.heapifyUp(this.heap.length - 1);
    }
  
    popMax() {
      if (this.isEmpty()) {
        throw new Error("Heap is empty.");
      }
  
      const max = this.heap[0];
      const last = this.heap.pop();
      if (!this.isEmpty()) {
        this.heap[0] = last;
        this.heapifyDown(0);
      }
      return max;
    }
  
    isEmpty() {
      return this.heap.length === 0;
    }
  
    heapifyUp(index) {
      const current = this.heap[index];
      let parentIndex = Math.floor((index - 1) / this.childFactor);
  
      while (index > 0 && current > this.heap[parentIndex]) {
        this.heap[index] = this.heap[parentIndex];
        index = parentIndex;
        parentIndex = Math.floor((index - 1) / this.childFactor);
      }
  
      this.heap[index] = current;
    }
  
    heapifyDown(index) {
      let maxChildIndex = this.getMaxChildIndex(index);
  
      while (maxChildIndex !== -1 && this.heap[index] < this.heap[maxChildIndex]) {
        [this.heap[index], this.heap[maxChildIndex]] = [this.heap[maxChildIndex], this.heap[index]];
        index = maxChildIndex;
        maxChildIndex = this.getMaxChildIndex(index);
      }
    }
  
    getMaxChildIndex(index) {
      const start = this.childFactor * index + 1;
      const end = Math.min(start + this.childFactor, this.heap.length);
      if (start >= this.heap.length) {
        return -1;
      }
      return Array.from({ length: end - start }, (_, i) => start + i)
        .reduce((maxIndex, i) => (this.heap[i] > this.heap[maxIndex] ? i : maxIndex), start);
    }
  }
  