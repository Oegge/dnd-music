document.addEventListener("DOMContentLoaded", function () {
    const audioPlayer = document.getElementById("audioPlayer");
    const playlists = document.querySelectorAll(".playlist");

    playlists.forEach((playlist) => {
        let songs = playlist.querySelectorAll(".song");

        songs.forEach((song) => {
            song.addEventListener("click", () => {
                loadSong(song);
            });
        });
    });

    function loadSong(song) {
        const audioUrl = song.getAttribute("data-audio");
        if (audioUrl) {
            audioPlayer.src = audioUrl;
            audioPlayer.load();
            audioPlayer.play()
                .catch(error => {
                    console.error("Error playing the file:", error);
                    if (error.name === 'NotAllowedError') {
                        console.warn('Autoplay was prevented.');
                    }
                });
            highlightCurrentSong(song);
        }
    }

    function highlightCurrentSong(selectedSong) {
        document.querySelectorAll('.song').forEach(song => {
            song.classList.remove("current");
        });
        selectedSong.classList.add("current");
    }

    audioPlayer.addEventListener("ended", function () {
        const currentSong = document.querySelector(".song.current");
        if(repeat){
            currentSong.click();
            return;
        }
        let nextSong = currentSong.nextElementSibling;
        if (!nextSong || !nextSong.classList.contains('song')) {
            nextSong = currentSong.parentNode.querySelector('.song');
            console.log(nextSong);
        }
        nextSong.click(); 
    });

   let repeat=false;
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
});
