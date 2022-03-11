const csrftoken = getCookie('csrftoken');
const formPopup = document.getElementById("form-popup");


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


function deleteItem(clicked_id){
    fetch('/api/' + clicked_id, {
    method: 'DELETE',
    headers: {
        'X-CSRFToken': csrftoken,
      },
  }, 3000);
    setTimeout(function(){location.reload()}, 10);
  }


function addMovie(clicked_id) {
    let title = document.getElementById("title");
    let year = document.getElementById("year");
    let rating = document.getElementById("rating");
    let notes = document.getElementById("notes");

    fetch('/api/', {
      method: 'POST',
      headers: {
          'content-type': 'application/json',
          'X-CSRFToken': csrftoken,
      },

      body: JSON.stringify({
          "title": title.value,
          "year": year.value,
          "rating": rating.value,
          "notes": notes.value
      }),
  }),
  closeForm();
  setTimeout(function(){location.reload()}, 100);
}


function editItem(clicked_id) {
    openForm()
    console.log(clicked_id);
}


function openForm() {
    formPopup.classList.add('active');
    overlay.classList.add('active');
}


function closeForm() {

    formPopup.classList.remove('active');
    overlay.classList.remove('active');
}