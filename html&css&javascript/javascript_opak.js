function fact(n) {
    let res = 1
    for (let i = 1; i <= n; i++) {
        res *= i
    }
    return res
}

console.log(fact(5)) // 120


const squareBtn = document.querySelector('.square-btn')
const textBtn = document.querySelector(".inp")
const input = document.querySelector(".inp2")
const body = document.querySelector("body")
const list = document.querySelector("#list")

squareBtn.addEventListener("click", createSquares)
textBtn.addEventListener("click", getText)

function createSquares(){
    for (let i = 0; i < 3; i++) {
        let square = document.createElement("div")

        square.style.width = "50px"
        square.style.height = "50px"
        square.style.backgroundColor = "lime"
        square.style.margin = "5px"
        
        body.append(square)
    }
}


function getText(){
    let value = input.value
    if (value.trim() === "") return

    console.log(value)
    let li = document.createElement("li")

    li.innerText = input.value

    input.value = ""

    list.append(li)
}

