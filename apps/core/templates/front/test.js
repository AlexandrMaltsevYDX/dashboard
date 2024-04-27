const draggables = document.querySelectorAll('.draggable')
const containers = document.querySelectorAll('.reobject-photo-container')


draggables.forEach(((draggable, index) => {
    fillNewOrder()
    draggable.addEventListener('dragstart', () => {
        draggable.classList.add('dragging')
    })

    draggable.addEventListener('dragend', () => {
        draggable.classList.remove('dragging')
        fillNewOrder()
    })
}))

containers.forEach(container => {
    container.addEventListener('dragover', e => {
        e.preventDefault()
        const afterElement = getDragAfterElement(container, e.clientY)
        const draggable = document.querySelector('.dragging')
        if (afterElement == null) {
            container.appendChild(draggable)
        } else {
            container.insertBefore(draggable, afterElement)
        }
    })
})

function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')]

    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect()
        const offset = y - box.top - box.height / 2
        if (offset < 0 && offset > closest.offset) {
            return {offset: offset, element: child}
        } else {
            return closest
        }
    }, {offset: Number.NEGATIVE_INFINITY}).element
}

function fillNewOrder() {
    const draggables = document.querySelectorAll('.draggable')
    draggables.forEach(((draggable, index) => {
        const newIndexElem = draggable.querySelector('.index-box').querySelector('.image-index')
        newIndexElem.textContent = String(index + 1);
    }))
}


async function updateValues() {
    const _url = new URL(window.location.href)
    const update_link = _url.pathname.replace('custom', 'update_values')
    console.log(_url.origin, _url.pathname.replace('custom', 'update_values'))
    let cookie = document.cookie
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
    const reObjectId = document.querySelector('[data-entity-name="re_object"]');
    const imageObjects = document.querySelectorAll('[data-entity-name="image"]');
    const updatedValuesArr = Array.from(imageObjects).map(elem => parseImageObject(elem));
    const updatedValues = updatedValuesArr.reduce((obj, x) => {
            obj[x['uuid']] = Number(x['order']);
            return obj
        }, {}
    )

    try {
        const response = await fetch(update_link, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({re_object_id: reObjectId.id, images: updatedValues}),
        });

        if (response.ok) {
            alert('Порядок изображений успешно сохранен!')
            location.reload();
        } else {
            console.error('Ошибка при отправке данных:', response.status);
        }
    } catch (error) {
        console.error('Ошибка при отправке данных:', error);
    }
}

function parseImageObject(element) {
    return {
        uuid: element.id,
        order: element.querySelector('.image-index').textContent
    }
}

function goBack() {
    window.history.go(-1)
}