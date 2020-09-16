
let jokeButton = $("#joke")
let dogButton = $("#dog")
let catButton = $("#cat")


async function handleJoke() {
    /** Send a get request to specific api, handle response, and display data */
    let resp = await axios.get("https://icanhazdadjoke.com/", {
        headers: {
            "Accept": "application/JSON"
        }
    })
    let joke = resp.data.joke
    $("#joke-data").empty()
    $("#joke-data").append(`<div class="jumbotron border border-dark"><h2>${joke}</h2></div>`)
}


async function handleDog() {
    /** Send a get request to specific api, handle response, and display data */
    let resp = await axios.get("https://dog.ceo/api/breeds/image/random")

    let dogPic = resp.data.message
    $("#dog-data").empty()
    $("#dog-data").append(`<div class="border border-dark"><img src=${dogPic}></div>`)
}

async function handleCat() {
    /** Send a get request to specific api, handle response, and display data */
    let resp = await axios.get("https://api.thecatapi.com/v1/images/search")
    let catPic = resp.data[0].url
    $("#cat-data").empty()
    $("#cat-data").append(`<div class="border border-dark"><img src=${catPic}></div>`)

    
}

$("#joke").on("click", async function(evt) {
    evt.preventDefault()
    await handleJoke()
})
$("#dog").on("click", async function(evt) {
    evt.preventDefault()
    await handleDog()
})
$("#cat").on("click", async function (evt) {
    evt.preventDefault()
    await handleCat()
})