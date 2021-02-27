// Timeout Chip: handles multiple messages.
setTimeout(() => {
    let chip_message = document.getElementsByClassName("messages");

    for (let i = 0; i < chip_message.length; i++) {
        chip_message[i].style.display = "none";
    }
}, 5000);