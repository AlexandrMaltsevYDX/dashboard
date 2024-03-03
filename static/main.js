addMultipleFilesInput()
document.addEventListener("DOMContentLoaded", function (event) {
    console.log("DOM fully loaded and parsed");
    addMultipleFilesInput()
    setTimeout(() => {
        console.log("Delayed for 1 second.");
        addMultipleFilesInput()
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

function addMultipleFilesInput() {
    // document.addEventListener("focusin", (e) => (e.preventDefault()), true)
    document.addEventListener("load", (e) => (e.preventDefault()), true)

    // const elem = document.body.innerText.includes("Фото объекта")
    // const parentElem = document.getElementById("jazzy-actions").children[0]
    // const myButton = document.createElement('input')
    //
    //
    // myButton.value = "Добавить кучу фото {{object.id}}"
    // myButton.textContent = "Добавить кучу фото {{object.id}}"
    // myButton.type = "file"
    // myButton.multiple = true
    // myButton.name = "multipleFiles"
    // myButton.classList.add("btn")
    // myButton.classList.add("btn-success")
    // myButton.classList.add("form-control")
    // myButton.addEventListener('change', (e) => {
    //     e.preventDefault()
    //     const formData = new FormData();
    //     for (let i = 0; i < e.target.files.length; i++) {
    //         formData.append('files[]', e.target.files[i]);
    //     }
    //     fetch('/upload', {
    //         method: 'POST',
    //         body: formData,
    //     })
    //         .then(response => response.json())
    //         .then(data => {
    //             console.log(data);
    //             document.getElementById('uploadStatus').textContent = 'Success';
    //         })
    //
    //     alert("file uploaded")
    // })
    //
    // if (elem) {
    //     parentElem.appendChild(myButton)
    // }
}