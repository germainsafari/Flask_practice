document.getElementById('load-items').addEventListener('click', function() {
    fetchItems();
});

function fetchItems() {
    // assuming we have an API endpoint '/api/items' which returns an array of items
    fetch('/api/items')
        .then(response => response.json())
        .then(items => {
            displayItems(items);
            attachItemClickHandlers();
        });
}

function displayItems(items) {
    const itemList = document.getElementById('item-list');
    itemList.innerHTML = '';
    items.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('item');
        itemElement.setAttribute('data-item-id', item.id);
        itemElement.textContent = item.name;
        itemList.appendChild(itemElement);
    });
}

function attachItemClickHandlers() {
    document.querySelectorAll('.item').forEach(itemElement => {
        itemElement.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            fetchItemDetails(itemId);
        });
    });
}

function fetchItemDetails(itemId) {
    // assuming we have an API endpoint '/api/items/:id' which returns details of an item
    fetch(`/api/items/${itemId}`)
        .then(response => response.json())
        .then(itemDetails => {
            displayItemDetails(itemDetails);
        });
}

function displayItemDetails(itemDetails) {
    const itemDetailsDiv = document.getElementById('item-details');
    itemDetailsDiv.innerHTML = `Name: ${itemDetails.name} <br> Description: ${itemDetails.description}`;
}


