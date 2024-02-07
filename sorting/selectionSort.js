function selectionSort(array) {
    for (let i = 0; i < array.length; i++) {
        let smallest = i;
        for (let j = i; j < array.length; j++) {
            if (array[j] < array[smallest]) {
                smallest = j;
            }
        }
        let temp = array[i];
        array[i] = array[smallest];
        array[smallest] = temp;
    }
    return array;
}
