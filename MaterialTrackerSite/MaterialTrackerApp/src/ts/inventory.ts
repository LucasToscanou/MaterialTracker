document.addEventListener('DOMContentLoaded', () => {
  document.getElementById("request-selection-btn")?.addEventListener("click", requestSelection);
  document.getElementById("edit-selection-btn")?.addEventListener("click", editSelection);
  document.getElementById("delete-selection-btn")?.addEventListener("click", deleteSelection);
  document.getElementById("request-selection")?.addEventListener("change", requestSelection);
  
  document.getElementById("clear-btn")?.addEventListener("click", clearSelection);

  const checkboxes = document.querySelectorAll<HTMLInputElement>('.checkbox');
  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateSelectedCount);
  });
});

function clearSelection(){
  const checkboxes = document.querySelectorAll<HTMLInputElement>('.checkbox');
  checkboxes.forEach(checkbox => {
    checkbox.checked = false;
  });
  updateSelectedCount();
}

function updateSelectedCount(){
  const selectedCountElement = document.getElementById('qty-selected');
  const selectedCount = getSelectedItems().length;

  if(selectedCountElement){
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
};

function requestSelection(){
    let requestSelection = document.getElementById("request-selection") as HTMLSelectElement;
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
    } else {
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
function getCSRFToken(): string {
  const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
  if (!csrfToken) {
      console.error('CSRF token not found!');
      return '';
  }
  return csrfToken;
}

function getSelectedItems(){
  const checkboxes = document.querySelectorAll<HTMLInputElement>('.checkbox');
  const selectedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);
  const selectedItems = selectedCheckboxes.map(checkbox => checkbox.id);
  return selectedItems;
}