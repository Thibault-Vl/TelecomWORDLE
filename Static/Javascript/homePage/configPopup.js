/*
 * Copyright (c) 2022/3/16.
 */

// Handle opening the config panel
document.getElementById("config-button").addEventListener("click", function () {
    document.querySelector(".popup-form.config-form").classList.add("active");
    document.querySelectorAll('.under-popup-content').forEach(element => element.classList.add("active"));
})

// Handle the close of the config panel
document.querySelector(".config-form .close-btn").addEventListener("click", function () {
    closeConfigPanel();
})

// Function to handle close of the config panel
function closeConfigPanel() {
    document.querySelector(".popup-form.config-form").classList.remove("active");
    document.querySelectorAll('.under-popup-content').forEach(element => element.classList.remove("active"));
}

// Handle submit config modification
function sendConfigModification() {
    const maxLength = document.getElementById("config-maxletters").value;

    const data = {
        "maxletters": maxLength
    }

    $.ajax({
        type: "POST",
        url: baseUrl + "/modify-config",
        data: data,
        success: function (result) {
            if (result['statement']) {
                closeConfigPanel();
                document.location.reload();
            }
        }
    });
}
