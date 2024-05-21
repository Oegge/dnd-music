function toggleSongs(header) {
    // Toggle the display of the adjacent 'songs' list
    var songList = header.nextElementSibling;
    if (songList.style.display === "none") {
        songList.style.display = "block";
    } else {
        songList.style.display = "none";
    }
}
