function formData(event) {
    event.preventDefault();
    console.log("Täällä ollaan!")

    var formData = new FormData(document.getElementById("formi"));

    fetch("/submit", {
        method: "POST",
        luku: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            document.getElementById("luku").value = data.annettu_luku;
            document.getElementById("mista").value = data.mista;
            document.getElementById("mihin").value = data.mihin;
        }
    })
    .catch(error => console.error('Error:', error));
}