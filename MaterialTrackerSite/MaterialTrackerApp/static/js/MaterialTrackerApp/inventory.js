"use strict";
document.addEventListener('DOMContentLoaded', () => {
    var _a, _b, _c, _d, _e;
    (_a = document.getElementById("request-selection-btn")) === null || _a === void 0 ? void 0 : _a.addEventListener("click", requestSelection);
    (_b = document.getElementById("edit-selection-btn")) === null || _b === void 0 ? void 0 : _b.addEventListener("click", editSelection);
    (_c = document.getElementById("delete-selection-btn")) === null || _c === void 0 ? void 0 : _c.addEventListener("click", deleteSelection);
    (_d = document.getElementById("request-selection")) === null || _d === void 0 ? void 0 : _d.addEventListener("change", requestSelection);
    (_e = document.getElementById("clear-btn")) === null || _e === void 0 ? void 0 : _e.addEventListener("click", clearSelection);
    const checkboxes = document.querySelectorAll('.checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateSelectedCount);
    });
});
function clearSelection() {
    const checkboxes = document.querySelectorAll('.checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    });
    updateSelectedCount();
}
function updateSelectedCount() {
    const selectedCountElement = document.getElementById('qty-selected');
    const selectedCount = getSelectedItems().length;
    if (selectedCountElement) {
        if (selectedCount === 0) {
            selectedCountElement.innerText = '';
        }
        else if (selectedCount === 1) {
            selectedCountElement.innerText = '1 item selected';
        }
        else {
            selectedCountElement.innerText = `${selectedCount} items selected`;
        }
    }
}
;
function requestSelection() {
    let requestSelection = document.getElementById("request-selection");
    console.log("requestSelection");
    // let selectedValue = requestSelection.options[requestSelection.selectedIndex].value;
    // console.log(selectedValue);
    const selectedCheckboxes = getSelectedItems();
}
function editSelection() {
    const selectedItems = getSelectedItems();
    console.log(JSON.stringify({
        action: 'delete',
        selectedItems,
    }));
    fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({
            action: 'edit',
            selectedItems,
        }),
    })
        .then(response => {
        console.log(response);
        if (response.redirected) {
            window.location.href = response.url; // Navigate to the new page
        }
        else {
            return response.json(); // Only parse JSON if it's not a redirect
        }
    })
        .catch(error => console.error('Error:', error));
}
function deleteSelection() {
    const selectedItems = getSelectedItems();
    fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({
            action: 'delete',
            selectedItems,
        }),
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}
// Utility function to get CSRF token
function getCSRFToken() {
    var _a;
    const csrfToken = (_a = document.querySelector('meta[name="csrf-token"]')) === null || _a === void 0 ? void 0 : _a.getAttribute('content');
    if (!csrfToken) {
        console.error('CSRF token not found!');
        return '';
    }
    return csrfToken;
}
function getSelectedItems() {
    const checkboxes = document.querySelectorAll('.checkbox');
    const selectedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);
    const selectedItems = selectedCheckboxes.map(checkbox => checkbox.id);
    return selectedItems;
}
