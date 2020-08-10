import * as API_KEY from 'api-key.js';
let jokeButton = $("#joke")
let dogButton = $("#dog")
let catButton = $("#cat")


async function handleJoke() {
    /** Send a get request to specific api, handle response, and display data */

    let resp = await axios({
        url: "https://icanhazdadjoke.com/",
        method: "GET",
        headers: {
            Accept: "application/JSON",
            "User-Agent" : "My library: https://github.com/leftykilla/capstone1"
        }
    })
    let joke = resp.data.joke
    $("#joke-data").append(`<h1>${joke}</h1>`)
}


async function handleDog() {
    /** Send a get request to specific api, handle response, and display data */

    let resp = await axios({
        url: "https://dog.ceo/api/breeds/image/random",
        method: "GET"
    })

    let dogPic = resp.data.message
    $("#dog-data").append(`<div><img src=${dogPic}></div>`)
}

async function handleCat() {
    /** Send a get request to specific api, handle response, and display data */

    let resp = await axios({
        url: "https://api.thecatapi.com/v1/images/search?limit=100",
        method: "GET",
        headers: {
            "x-api-key": API_KEY
        }
    })
    catInfo = resp.data
    return catInfo
    
}

function catPicPool(catInfo) {
    catPics = []
    for (pic of catInfo) {
        catPics.append(catInfo.url[pic])
    }
    
    $("#cat-data").append(`<h1>${joke}</h1>`)
}
