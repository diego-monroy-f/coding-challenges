package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func selectionSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		smallest := i
		for j := i; j < len(arr); j++ {
			if arr[j] < arr[smallest] {
				smallest = j
			}
		}
		temp := arr[i]
		arr[i] = arr[smallest]
		arr[smallest] = temp
	}
	return arr
}

func asyncSortArray(name string, arr []int, channel chan []int) {
	fmt.Println("--", name, "\nSorting array:", arr)
	channel <- selectionSort(arr)
	fmt.Println("Sorted array:", arr)
}

func main() {
	// Get input data
	var input string
	fmt.Println("Please enter comma-separated integers:")
	fmt.Scan(&input)
	fmt.Println("These are the inputs:", input)
	// Create int array from user input
	arr := make([]int, 0)
	for _, elem := range strings.Split(input, ",") {
		intElem, err := strconv.Atoi(elem)
		if err == nil {
			arr = append(arr, intElem)
		}
	}
	// If length is less than 4, exit
	if len(arr) < 4 {
		fmt.Println("Error: Array must have at least 4 elements.")
		return
	}
	// Split into 4 different partitions
	half := math.Floor(float64(len(arr) / 2))
	var (
		p0 = 0
		p1 = int(math.Floor(half / 2))
		p2 = int(half)
		p3 = int(math.Floor(half/2) + half)
		p4 = len(arr)
	)
	// Use partitions to call sorting
	channel := make(chan []int, 4)
	go asyncSortArray("first", arr[p0:p1], channel)
	go asyncSortArray("second", arr[p1:p2], channel)
	go asyncSortArray("third", arr[p2:p3], channel)
	go asyncSortArray("fourth", arr[p3:p4], channel)
	// Get results from channel
	subArr1 := <-channel
	subArr2 := <-channel
	subArr3 := <-channel
	subArr4 := <-channel
	// Join all together
	var result = make([]int, 0)
	result = append(result, subArr1...)
	result = append(result, subArr2...)
	result = append(result, subArr3...)
	result = append(result, subArr4...)
	result = selectionSort(result)
	// Print final result
	fmt.Println("==\nFinal sorted array:", result)
}
