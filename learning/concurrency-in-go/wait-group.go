package main

import (
	"fmt"
	"sync"
)

func something(waitGroup *sync.WaitGroup) {
	fmt.Println(("New goroutine!"))
	waitGroup.Done()
}

func main() {
	var waitGroup sync.WaitGroup
	waitGroup.Add(1)
	go something(&waitGroup)
	waitGroup.Wait()
	fmt.Println("Main goroutine!")
}
