package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var ranges = []int{}

func main() {
	content, err := ioutil.ReadFile("info.txt")
	if err != nil {
		//Do something
	}
	lines := strings.Split(string(content), "\n")
	x := 0
	newnum := 0
	for i := 0; i < len(lines); i++ {
		fmt.Println(lines[i])
		newnum, _ = strconv.Atoi(lines[i])
		x = x + newnum
		ranges[i] = x
		if val, ok := ranges[x]; ok {
			fmt.Println("found it", ranges[x])
			break
		}
	}
	fmt.Println(x)
}
