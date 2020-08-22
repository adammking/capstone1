
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
    let resp = await axios.get("https://api.thecatapi.com/v1/images/search")
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