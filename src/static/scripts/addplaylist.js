 src="https://unpkg.com/dragula/dist/dragula.min.js"


 var drake =  dragula([document.getElementById("song-list"), document.getElementById("playlist")])
 .on('drag', function (el) {
   el.className = el.className.replace('ex-moved', '');
 }).on('drop', function (el) {
   el.className += ' ex-moved';
 }).on('over', function (el, container) {
   container.className += ' ex-over';
 }).on('out', function (el, container) {
   container.className = container.className.replace('ex-over', '');
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
    var input = document.getElementById('filter');
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