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
        const newIndexElem = draggable.querySelector('.index-box').querySelector('.index-new')
        newIndexElem.textContent = String(index + 1);
    }))
}


async function updateValues() {
    let cookie = document.cookie
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
    const newIndexElems = document.querySelectorAll('.index-new');
    const updatedValues = Array.from(newIndexElems).map(elem => elem.textContent);
    try {
        const response = await fetch('/update_values/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({values: updatedValues}),
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message);
        } else {
            console.error('Ошибка при отправке данных:', response.status);
        }
    } catch (error) {
        console.error('Ошибка при отправке данных:', error);
    }
}