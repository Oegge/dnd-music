

document.addEventListener("DOMContentLoaded", function () {
    var playlist = document.getElementById('playlist');

    var sortable = new Sortable(playlist, {
        animation: 150,
        onEnd: function (evt) {
            console.log(`Moved from ${evt.oldIndex} to ${evt.newIndex}`);
            updateSongsOrder();
            updateCurrentSongIndex(evt.oldIndex, evt.newIndex);
        }
    });
    const audioPlayer = document.getElementById("audioPlayer");
    const audioSource = document.getElementById("audioSource");
    let songs = document.querySelectorAll("#playlist .song");
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
        songs.forEach((song, idx) => {
            if (idx === index) {
                song.classList.add("current");
            } else {
                song.classList.remove("current");
            }
        });
    }

    audioPlayer.addEventListener("ended", function () {
        currentSongIndex = (currentSongIndex + 1) % songs.length;
        loadSong(currentSongIndex);
    });

    function updateSongsOrder() {
        songs = document.querySelectorAll("#playlist .song");
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