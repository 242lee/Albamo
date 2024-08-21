package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()
	for {
		if cycle() == false {
			return
		}
	}
}

func cycle() bool {
	// -----cycle내에 reader, writer, Flush 존재 => 오답------
	// var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	// var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	// defer writer.Flush()
	var a, b, c int

	fmt.Fscanln(reader, &a, &b, &c)
	if a == 0 && b == 0 && c == 0 {
		return false
	}
	if check_valid(a, b, c) == false {
		fmt.Println("Invalid")
	} else {
		if a == b && b == c {
			fmt.Println("Equilateral")
		} else if a != b && b != c && a != c {
			fmt.Println("Scalene")
		} else {
			fmt.Println("Isosceles")
		}
	}
	return true
}

func check_valid(a, b, c int) bool {
	pivot := []int{a, b, c}
	sort.Ints(pivot)
	if pivot[0]+pivot[1] <= pivot[2] {
		return false
	} else if pivot[0] == 0 || pivot[1] == 0 || pivot[2] == 0 {
		return false
	} else {
		return true
	}

}
