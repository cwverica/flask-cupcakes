BASE_URL = "/api/cupcakes"

$("#add_cupcake_btn").on('click', add_cupcake)

/** Sends a new cupcake to the api */
async function add_cupcake(evt) {
    evt.preventDefault();
    const flavor = $('#flavor').val()
    const size = $('#size').val()
    const rating = $('#rating').val()
    const image = $('#image').val()

    console.log(flavor, size, rating, image);
    const response = await axios({
        url: `${BASE_URL}`,
        method: "POST",
        data: {
            "flavor": flavor,
            "size": size,
            "rating": rating,
            "image": image
        }
    });

    loadCupcakes()


}



async function loadCupcakes() {
    const allCupcakes = await axios({
        url: `${BASE_URL}`,
        method: "GET"
    });

    $("#cupcake_list").empty();

    for (let cake of allCupcakes.data.cupcakes) {
        // const markup = `<li>${cake['flavor']}</li>`;
        const flavor = cake['flavor'];
        $("#cupcake_list").append(`<li class="cupcake" data-id="${cake['id']}">${cake['flavor']}</li>`);
    };

    $("#cupcake_list").show();


}


$(document).ready(loadCupcakes());