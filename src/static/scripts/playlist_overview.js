document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.delete-icon').forEach(deleteIcon => {
        deleteIcon.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the default action
            event.stopPropagation(); // Stop the event from bubbling up

            const playlistId = this.closest('.playlist').getAttribute('data-playlist-id');
            deletePlaylist(playlistId, this.closest('.playlist'));
        });
    });
});

function deletePlaylist(playlistId, playlistElement) {
    fetch(`/delete/playlist/${playlistId}`, {
        method: 'DELETE', headers: {
            'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') // Add the CSRF token if needed
        }
    })
        .then(response => {
            if (response.ok) {
                playlistElement.remove(); // Remove the playlist element from the DOM
            } else {
                console.error('Failed to delete the playlist.');
            }
        })
        .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
