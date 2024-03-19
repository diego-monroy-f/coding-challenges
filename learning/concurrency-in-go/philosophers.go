package main

import (
	"fmt"
	"sync"
)

// Constants

const TIMES_EATING = 3

// Declating structs

type Chopstick struct{ sync.Mutex }

type Philosopher struct {
	leftChopstick  *Chopstick
	rightChopstick *Chopstick
	number         int
}

type Host struct {
	actions *sync.WaitGroup
	seats   chan int
}

// Host functionality

func (h *Host) run() {
	// Add two seat positions to start execution.
	h.seats <- 1
	h.seats <- 1
}

func (h *Host) takeSeat() int {
	// Take a seat by consuming from channel.
	return <-h.seats
}

func (h *Host) leaveSeat() {
	// Return a seat by adding to channel and decrementing actions.
	h.seats <- 1
	h.actions.Done()
}

// Philosopher functionality

func (p *Philosopher) eat(h *Host) {
	for i := 0; i < TIMES_EATING; i++ {
		// Wait to be seated (if seats are available).
		h.takeSeat()
		// Pick up chopsticks.
		p.leftChopstick.Lock()
		p.rightChopstick.Lock()
		fmt.Println("starting to eat ", p.number+1)
		fmt.Println("finishing eating ", p.number+1)
		// Leave chopsticks.
		p.leftChopstick.Unlock()
		p.rightChopstick.Unlock()
		// Leave seat.
		h.leaveSeat()
	}
}

// Main routine

func main() {
	// Initialize data.
	chopsticks := make([]*Chopstick, 5)
	for i := 0; i < len(chopsticks); i++ {
		chopsticks[i] = new(Chopstick)
	}
	philosophers := make([]*Philosopher, 5)
	for i := 0; i < len(philosophers); i++ {
		philosophers[i] = &Philosopher{
			leftChopstick:  chopsticks[i],
			rightChopstick: chopsticks[(i+1)%len(chopsticks)],
			number:         i,
		}
	}
	host := &Host{
		actions: &sync.WaitGroup{},
		seats:   make(chan int, 2),
	}
	// Run host and philosophers.
	host.actions.Add(len(philosophers) * TIMES_EATING)
	go host.run()
	for i := 0; i < len(philosophers); i++ {
		go philosophers[i].eat(host)
	}
	host.actions.Wait()
}
