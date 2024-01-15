const btnWhite = document.getElementById("button-white");
const btnBlack = document.getElementById("button-black");

btnWhite.addEventListener("click", (e) => {
    document.body.style.backgroundColor = "white"
});
btnBlack.addEventListener("click", (e) => {
    document.body.style.backgroundColor = "black"
});