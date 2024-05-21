

document.addEventListener("DOMContentLoaded", function () {
    var playlist = document.getElementById('playlist');
    var saveOrderButton = document.getElementById('saveOrderButton');
    saveOrderButton.addEventListener('click', saveOrder);
    let repeat = false;
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
    function saveOrder() {
        var pathname = window.location.pathname;

        // Split the pathname into segments
        var segments = pathname.split('/');

        // Get the last segment, handling any potential trailing slash
        var lastSegment = segments.pop() || segments.pop();  // Handles trailing slash if present

        console.log(lastSegment);
        const order = Array.from(songs).map(song => parseInt(song.getAttribute('id'), 10));
        console.log(songs)
        fetch('/api/update_order/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken'),  // CSRF token for Django
            },
            body: new URLSearchParams({

                'order[]': order,
                'playlist': lastSegment
            }).toString()
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    console.log('Order saved successfully');
                } else {
                    console.log('Failed to save order');
                }
            });
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


