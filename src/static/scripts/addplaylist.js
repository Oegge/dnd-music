 src="https://unpkg.com/dragula/dist/dragula.min.js"


 var drake =  dragula([document.getElementById("song-list"), document.getElementById("playlist")])
 drake.on('drop', function(el, target, source, sibling) {
    // Check if the element was dropped in the playlist
    if (target.id === 'playlist') {
        var songId = el.dataset.id; // Get the song ID
        var input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'song_ids[]';
        input.value = songId;
        document.getElementById('playlist-form').appendChild(input);
    } else if (source.id === 'playlist') {
        // Handle removing elements from the playlist
        var inputs = document.getElementById('playlist-form').querySelectorAll('input');
        Array.from(inputs).forEach(input => {
            if (input.value === el.dataset.id) {
                input.remove(); // Remove the input if the song is dragged out
            }
        });
    }
});

drake.on('drag', function(el) {
    // Play the audio associated with the element being dragged
    var audioId = 'audio-' + el.dataset.id;
    var audio = document.getElementById(audioId);
    if (audio) {
        audio.play();
    }
});

drake.on('dragend', function(el) {
    // Stop the audio when dragging stops
    var audioId = 'audio-' + el.dataset.id;
    var audio = document.getElementById(audioId);
    if (audio) {
        audio.pause();
        audio.currentTime = 0;  // Reset the audio to start
    }
});

function filterSongs() {
    var input = document.getElementById('song-filter');
    var filter = input.value.toLowerCase();
    var nodes = document.getElementById('song-list').getElementsByTagName('div');
    for (i = 0; i < nodes.length; i++) {
        if (nodes[i].innerText.toLowerCase().includes(filter)) {
            nodes[i].style.display = "block";
        } else {
            nodes[i].style.display = "none";
        }
    }
}