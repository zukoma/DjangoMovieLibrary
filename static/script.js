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
    fetch('/api/movies/' + clicked_id, {
    method: 'DELETE',
    headers: {
        'X-CSRFToken': csrftoken,
      }}
    );
    setTimeout(function(){location.reload()}, 50);
  }


function addMovie() {
    let title = document.getElementById("title");
    let year = document.getElementById("year");
    let rating = document.getElementById("rating");
    let notes = document.getElementById("notes");

    fetch('/api/movies/', {
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
    })
}


function editMovie(id) {
    let title = document.getElementById("title");
    let year = document.getElementById("year");
    let rating = document.getElementById("rating");
    let notes = document.getElementById("notes");

    fetch('/api/movies/' + id + '/', {
        method: 'PUT',
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
  })
}


function submit(){
    let id_value = document.getElementById("id").value
    if (id_value == ''){
        addMovie();
        setTimeout(function(){location.reload()}, 100);
        closeForm();
    } else{
        editMovie(id_value);
        setTimeout(function(){location.reload()}, 100);
        closeForm();
    }
}


function editForm(clicked_id) {
    let title = document.getElementsByClassName('div-title-'+clicked_id)[0].innerHTML;
    let year = document.getElementsByClassName('div-year-'+clicked_id)[0].innerHTML;
    let rating = document.getElementsByClassName('div-rating-'+clicked_id)[0].innerHTML;
    let notes = document.getElementsByClassName('div-notes-'+clicked_id)[0].innerHTML;
    document.getElementById("title").setAttribute('value', title);
    document.getElementById("year").setAttribute('value', year);
    document.getElementById("rating").setAttribute('value', rating);
    document.getElementById("notes").setAttribute('value', notes);
    document.getElementById("id").setAttribute('value', clicked_id);
    openForm()
}


function openForm() {
    formPopup.classList.add('active');
    overlay.classList.add('active');
}


function closeForm() {
    document.getElementById("id").setAttribute('value', '');
    document.getElementById("title").setAttribute('value', '');
    document.getElementById("year").setAttribute('value', '');
    document.getElementById("notes").setAttribute('value', '');
    document.getElementById("rating").setAttribute('value', '');
    formPopup.classList.remove('active');
    overlay.classList.remove('active');
}