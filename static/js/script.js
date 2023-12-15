const popUp = document.getElementById("pop-up");
const darkBackdrop = document.getElementById("dark-backdrop");

const openPopUp = () => {
    try {
        popUp.classList.replace("opacity-0", "opacity-1")
        darkBackdrop.classList.replace("opacity-0", "opacity-1")
        darkBackdrop.classList.replace("pointer-events-none", "pointer-events-default")

    } catch (error) {

    }
}

const closePopUp = () => {
    try {
        popUp.classList.replace("opacity-1", "opacity-0")
        darkBackdrop.classList.replace("opacity-1", "opacity-0")
        darkBackdrop.classList.replace("pointer-events-default", "pointer-events-none")

    } catch (error) {

    }
}