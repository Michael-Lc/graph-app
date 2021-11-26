function submitform(event) {
  const { data } = event.target;
  console.log(data.value);
  return false;
}

function clearForm() {
  const elements = document.getElementsByClassName("form-control")

  for (const el of elements) {
    el.value = ""
  }
}

// Get the modal
const modal = document.getElementById("error-modal");

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
