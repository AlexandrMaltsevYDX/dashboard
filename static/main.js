document.addEventListener("DOMContentLoaded", function (event) {
    console.log("DOM fully loaded and parsed");
    setTimeout(() => {
        console.log("Delayed for 1 second.");
        const selects = document.querySelectorAll(".select2-hidden-accessible")
        const navitems = document.querySelectorAll(".nav-item")
        const addRows = document.querySelectorAll(".add-row")
        console.log(selects)
        selects.forEach((e) => test(e))
        navitems.forEach((e) => addEvents(e))
        addRows.forEach((e) => addEvents(e))
    }, 1000);
});


function test(elem) {
    elem.classList.remove("select2-hidden-accessible")
}

function addEvents(elem) {
    elem.addEventListener("click", deleteSelect2)
}

function deleteSelect2() {
    const selects = document.querySelectorAll(".select2-hidden-accessible")
    selects.forEach((e) => test(e))
}