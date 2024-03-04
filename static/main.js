document.addEventListener("DOMContentLoaded", function (event) {
    // console.log("DOM fully loaded and parsed");
    setTimeout(() => {
        // console.log("Delayed for 1 second.");
        const selects = document.querySelectorAll(".select2-hidden-accessible")
        const navitems = document.querySelectorAll(".nav-item")
        const addRows = document.querySelectorAll(".add-row")
        // console.log(selects)
        selects.forEach((e) => removeUselessClass(e))
        navitems.forEach((e) => addEvents(e))
        addRows.forEach((e) => addEvents(e))
    }, 500);
});


function removeUselessClass(elem) {
    elem.classList.remove("select2-hidden-accessible")
}

function addEvents(elem) {
    elem.addEventListener("click", (ev) => postProcessing(ev))
    // addMultipleFilesInput()
}

function postProcessing(ev) {
    const selects = document.querySelectorAll(".select2-hidden-accessible")
    selects.forEach((e) => test(e))
    const photoTab = ev.target.getAttribute("aria-controls")
    console.log(photoTab)
    const _url = new URL(window.location.href)
    console.log(_url.pathname); //api/v1/objects/objects/
    if (photoTab.includes("фото")) {
        addMultipleFilesInput("фото")
    } else if (photoTab.includes("планы")) {
        addMultipleFilesInput("планы")
    } else if (photoTab.includes("планировки")) {
        addMultipleFilesInput("планировки")
    } else {
        if (document.getElementById("myButton")) {
            document.getElementById("myButton").remove()
        }
        if (document.getElementById("labelFormyButton")) {
            document.getElementById("labelFormyButton").remove()
        }
    }
}

function addMultipleFilesInput(key) {
    if (document.getElementById("myButton")) {
        document.getElementById("myButton").remove()
    }
    if (document.getElementById("labelFormyButton")) {
        document.getElementById("labelFormyButton").remove()
    }

    const capKey = capitalize(key)
    const elem = document.body.innerText.includes(capKey)
    const parentElem = document.getElementById("jazzy-actions").children[0]
    const myButton = document.createElement('input')
    myButton.name = "multipleFiles"
    const labelFormyButton = document.createElement('label')
    labelFormyButton.for = "multipleFiles"
    labelFormyButton.textContent = `Добавить ${key}`


    // myButton.value = "Добавить кучу фото"
    // myButton.textContent = "Добавить кучу фото"
    myButton.type = "file"
    myButton.multiple = true
    myButton.id = "myButton"
    labelFormyButton.id = "labelFormyButton"

    myButton.classList.add("btn")
    myButton.classList.add("hidden")
    // myButton.classList.add("form-control")

    labelFormyButton.classList.add("btn")
    labelFormyButton.classList.add("btn-success")
    labelFormyButton.classList.add("form-control")
    labelFormyButton.addEventListener('click', trigerInput)


    myButton.addEventListener('change', (e) => {
        e.preventDefault()
        const formData = new FormData();
        for (let i = 0; i < e.target.files.length; i++) {
            formData.append('files[]', e.target.files[i]);
        }
        // console.log([...formData]);
        const _url = new URL(window.location.href)
        console.log(_url); //api/v1/objects/objects/
        //
        // fetch('/upload', {
        //     method: 'POST',
        //     body: formData,
        // })
        //     .then(response => response.json())
        //     .then(data => {
        //         console.log(data);
        //         document.getElementById('uploadStatus').textContent = 'Success';
        //     })
        // /admin/apps_admin_objects/reobjectproxy/df36cec6-4eb2-4c60-b225-da2a8e55d738/change/
        //
        //
        //
        //
        // alert("file uploaded")
    })

    if (elem) {
        parentElem.appendChild(labelFormyButton)
        parentElem.appendChild(myButton)
    }
}

function trigerInput() {
    const myButton = document.getElementById('myButton')
    myButton.click()
}


function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

const router = {
    apps_admin_blog: {
        photo: "/api/v1/blog/post/",
        plan: "",
    },
    apps_admin_objects: {
        photo: "0/api/v1/objects/objects/",
        plan: "0/api/v1/objects/objects/",
    },
    apps_admin_village: {
        photo: "0/api/v1/objects/objects/",
        plan: "0/api/v1/objects/objects/",
    },
    apps_admin_employees: {
        photo: "0/api/v1/objects/objects/",
        plan: "0/api/v1/objects/objects/",
    },
    apps_admin_review: {
        photo: "0/api/v1/objects/objects/",
        plan: "0/api/v1/objects/objects/",
    }
}
