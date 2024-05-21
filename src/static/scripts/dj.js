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
                    // Check for autoplay issues
                    if (error.name === 'NotAllowedError') {
                        console.warn('Autoplay was prevented.');
                        // Consider showing a UI element to encourage user interaction
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
        // Find the next song to play when current song ends
        const currentSong = document.querySelector(".song.current");
        let nextSong = currentSong.nextElementSibling;
        if (!nextSong || !nextSong.classList.contains('song')) {
            // If no next song in this playlist, go to the first song
            nextSong = currentSong.parentNode.querySelector('.song');
            console.log(nextSong);
        }
        nextSong.click();  // Simulate click on next song
    });

    audioPlayer.addEventListener('error', (e) => {
        console.error("Error loading the audio:", e);
    });
});
