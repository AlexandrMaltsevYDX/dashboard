document.addEventListener("DOMContentLoaded", function (event) {
    console.log("DOM fully loaded and parsed");
    setTimeout(() => {
        console.log("Delayed for 1 second.");
        const selects = document.querySelectorAll(".select2-hidden-accessible")
        console.log(selects)
        selects.forEach((e) => test(e))
    }, 1500);
});


function test(elem) {
    elem.classList.remove("select2-hidden-accessible")
}