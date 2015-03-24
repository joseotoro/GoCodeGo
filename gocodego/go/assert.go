package main
import "fmt"

/*
 * INPUT: value, result, expected
 *
 * BOOM if result != expected
 */
func assert(result interface{}, expected interface{}){
	if(result != expected){
		panic(fmt.Sprintf("FAILED! Yielded %v, but expected %v as the result", result, expected))
	}
}

func main() {
	assert(1,1)
    assert(1,2)
}
