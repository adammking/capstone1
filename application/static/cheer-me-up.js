import * as API_KEY from '/static/api-key.js';
let jokeButton = $("#joke")
let dogButton = $("#dog")
let catButton = $("#cat")


async function handleJoke() {
    /** Send a get request to specific api, handle response, and display data */
    let resp = await axios.get("https://icanhazdadjoke.com/", {
        headers: {
            "Accept": "application/JSON",
            "User-Agent" : "My library: https://github.com/leftykilla/capstone1"
        }
    })
    let joke = resp.data.joke
    $("#joke-data").append(`<h1>${joke}</h1>`)
}


async function handleDog() {
    /** Send a get request to specific api, handle response, and display data */
    let resp = await axios.get("https://dog.ceo/api/breeds/image/random")

    let dogPic = resp.data.message
    $("#dog-data").append(`<div><img src=${dogPic}></div>`)
}

async function handleCat() {
    /** Send a get request to specific api, handle response, and display data */
    let resp = await axios.get("https://api.thecatapi.com/v1/images/search?limit=1",{
        headers: {
            "x-api-key": API_KEY
        }})
    let catPic = resp.data[0].url

    $("#cat-data").append(`<div><img src=${catPic}></div>`)

    
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