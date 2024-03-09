document.addEventListener("DOMContentLoaded", function (event) {
    console.log("DOM fully loaded and parsed");
    const selects = document.querySelectorAll(".select2-hidden-accessible")
    selects.forEach((e) => removeUselessClass(e))
    setTimeout(() => {
        const selects = document.querySelectorAll(".select2-hidden-accessible")
        const navitems = document.querySelectorAll(".nav-item")
        const addRows = document.querySelectorAll(".add-row")
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
    selects.forEach((e) => removeUselessClass(e))
    const tabName = ev.target.getAttribute("aria-controls")
    console.log(tabName)
    const _url = new URL(window.location.href)
    console.log(_url.pathname); //api/v1/objects/objects/

    const pathObj = parsePath(_url.pathname)

    if (tabName.includes("фото")) {
        console.log("postProcessing", pathObj)
        addMultipleFilesInput("фото", pathObj.model, pathObj.uuid)
    } else if (tabName.includes("планы")) {
        addMultipleFilesInput("планы", pathObj.model, pathObj.uuid)
    } else {
        if (document.getElementById("myButton")) {
            document.getElementById("myButton").remove()
        }
        if (document.getElementById("labelFormyButton")) {
            document.getElementById("labelFormyButton").remove()
        }
    }
}

function addMultipleFilesInput(key, model, objectModel_uuid) {
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

    myButton.type = "file"
    myButton.multiple = true
    myButton.id = "myButton"
    labelFormyButton.id = "labelFormyButton"

    myButton.classList.add("btn")
    myButton.classList.add("hidden")

    labelFormyButton.classList.add("btn")
    labelFormyButton.classList.add("btn-success")
    labelFormyButton.classList.add("form-control")
    labelFormyButton.addEventListener('click', trigerInput)


    myButton.addEventListener('change', (e) => {
        e.preventDefault()

        const _url = new URL(window.location.href)


        const urls = {
            "villageproxy": {
                "фото": "villages_images",
                "планы": "villages_plans"
            },
            "reobjectproxy": {
                "фото": "objects_images",
                "планы": "objects_plans"
            },
            "employeeprofileproxymodel": {
                "фото": "profiles_images"
            },
            "postproxy": {
                "фото": "posts_images"
            },
            "reviewproxy": {
                "фото": "reviews_images"
            }
        }

        const url = `${_url.origin}/api/v1/${urls[model][key]}/`

        for (let i = 0; i < e.target.files.length; i++) {
            let lastElem = false
            if (i === e.target.files.length - 1) {
                lastElem = true
            }
            let body = {image: e.target.files[i], objectModel: objectModel_uuid}
            uploadFile(body, url, lastElem)
        }
    })

    if (elem) {
        parentElem.appendChild(labelFormyButton)
        parentElem.appendChild(myButton)
    }
}


function uploadFile(body, url, lastElem) {
    const {objectModel, image} = body
    console.log("uploadFile", body)
    const formData = new FormData();
    formData.append('image', image)
    formData.append('objectModel', objectModel)
    fetch(url, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (lastElem) {
                alert("Все загружено")
                location.reload()
            }
        })
}

function trigerInput() {
    const myButton = document.getElementById('myButton')
    myButton.click()
}


function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function parsePath(str) {
    const ar = str.replace('/admin/').replace('change/').split('/')
    return new PathObj(...ar)
}


class PathObj {
    constructor(app, model, uuid) {
        this.app = app;
        this.model = model;
        this.uuid = uuid;
    }
}