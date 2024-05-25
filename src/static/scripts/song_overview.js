

document.addEventListener("DOMContentLoaded", function () {
    let repeat = false;
   
    const audioPlayer = document.getElementById("audioPlayer");
    const audioSource = document.getElementById("audioSource");
   let currentSongIndex = 0;
    updateSongsOrder();
    function loadSong(index) {
        const song = songs[index];

        audioSource.src = song.getAttribute("data-audio");
        audioPlayer.load();
        audioPlayer.play();
        highlightCurrentSong(index);
    }

    function highlightCurrentSong(index) {
    songs.forEach((pElement, idx) => {
        // Access the parent .song element using closest() method
        const song = pElement.closest('.song');
        if (song) {  // Ensure that the .song parent was found
            if (idx === index) {
                song.classList.add("current");  // Add 'current' to the parent .song of the targeted p element
            } else {
                song.classList.remove("current");  // Remove 'current' from other .song parents
            }
        }
    });
}

    const button = document.querySelector('.repeat-btn');
    button.addEventListener('click', toggleRepeat);
    function toggleRepeat() {
        let button = document.querySelector('.repeat-btn'); // Select the button by its class
        repeat = !repeat; // Toggle the repeat variable
        if (repeat) {
            button.classList.add('active'); // Add 'active' class when repeat is true
        } else {
            button.classList.remove('active'); // Remove 'active' class when repeat is false
        }
    }
    

    audioPlayer.addEventListener("ended", function () {
        if (!repeat) {
            currentSongIndex = (currentSongIndex + 1) % songs.length;
        }
        loadSong(currentSongIndex);
    });

    function updateSongsOrder() {
        songs = document.querySelectorAll("#playlist .song p");
        songs.forEach((song, index) => {
            song.addEventListener("click", () => {
                currentSongIndex = index;
                loadSong(currentSongIndex);
            });
        });
    }

    function updateCurrentSongIndex(oldIndex, newIndex) {
        if (currentSongIndex === oldIndex) {
            currentSongIndex = newIndex;
        } else if (oldIndex < currentSongIndex && newIndex >= currentSongIndex) {
            currentSongIndex--;
        } else if (oldIndex > currentSongIndex && newIndex <= currentSongIndex) {
            currentSongIndex++;
        }
    }

});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


