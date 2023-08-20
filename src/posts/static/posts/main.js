//function updateText(btn, newCount, verb){
//    btn.text(newCount + ' ' + verb)
//}


logo = document.querySelectorAll('.s-btn')
counter  = document.querySelectorAll('.counter')

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



$('form').submit(function(e){

    e.preventDefault()
    const csrftoken = getCookie('csrftoken')
     $.ajax({
         type: "POST",
         url: 'http://127.0.0.1:8000/api/create/'+$(this)[0].name,
         data: {"comment": $(this)[0].comment.value},
         headers: {"X-CSRFToken": csrftoken}
    })
    $(this)[0].reset()

    return false;


})

$('.like-btn').click(function(e){
       e.preventDefault()
        e.stopPropagation()
    var this_ = $(this)
    console.log(this_)
    var likeUrl = this_.attr('data-href')
    var likeCount = parseInt(this_.attr('data-likes'))
    console.log(this_[0].children[1])
    console.log(likeCount)
    $.ajax({
    url: likeUrl,
    method: "GET",
    data: {},
    success: function(data){
        console.log()
        var newLikes;
        if(data.liked){

               newLikes = likeCount + 1
                this_[0].setAttribute('data-likes', newLikes )

                this_[0].children[0].classList.remove('like')
                this_[0].children[0].classList.add('liked')


               console.log("Unlike", newLikes)

                this_[0].parentElement.previousElementSibling.innerHTML = newLikes + " " + "Likes"
//               updateText(this_, newLikes, 'Unlike')


        }else{

        console.log('LIKED')

            newLikes = likeCount - 1

                this_[0].setAttribute('data-likes', newLikes )

                this_[0].children[0].classList.remove('liked')
                this_[0].children[0].classList.add('like')

                console.log("Like",newLikes)
                this_[0].parentElement.previousElementSibling.innerHTML = newLikes + " " + "Likes"
         //   updateText(this_, newLikes, 'Like')


        }

    }, error: function(error){
    console.log(error)

    }

    })
})


const glass = document.getElementsByClassName('glass')
const comment = document.getElementById('comment')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
const box = document.getElementById('C')
let visible = 1
console.log(glass[0])
nop = glass.length
console.log(glass[0].children[6].children[1])

let temp = 0
let n = 0
$('.load').click(function(e){

n = e.target.dataset.href
console.log(n)
temp = parseInt(e.target.dataset.visible)+1
e.target.dataset.visible= temp.toString()
visible = temp

console.log(e.target.dataset.visible, "-----------")

$.ajax({

    type: "GET",
    url: `/posts-json/${visible}/${n}`,
    success: function(response){

        console.log(response)
        max_size = response.max

        const data=JSON.parse(response.data)
        console.log(e.target.name)
           glass[e.target.name -1].children[6].children[0].classList.remove('not-visible')
        console.log(data)

        setTimeout(()=>{
               glass[e.target.name -1].children[6].children[0].classList.add('not-visible')

            data.map((p,i) =>{
            let x = new Date ((data[i].fields.date))

        glass[e.target.name - 1].children[5].innerHTML += `
        <div class="comment">

        <div class="user-info">
            <img src= ${ response.urls[i]}>
<div class="sub-info">
            <p class="username">
               ${ response.commenters[i]}
            </p>
            <p class="date">
               ${(x.toUTCString().split(" ").slice(0,4).join(" "))}


            </p>
    </div>
        </div>
        <p>
${data[i].fields.comment}

    </p>
        </div>`
        })

        if(response.max){
               glass[e.target.name -1].children[6].children[1].innerHTML = `<div class="loaded">No more comments to load</div>`

            console.log('DONE')
        }
        }, 500)

    },
    error: {
    function(error){
        console.log(error)
    }}
})
})
//const handleGetData = (n,o) => {
//    console.log(n)
//$.ajax({
//
//    type: "GET",
//    url: `/posts-json/${visible}/${n}`,
//    success: function(response){
//        console.log(response)
//        max_size = response.max
//
//        const data=JSON.parse(response.data)
//        console.log(data)
//            console.log(o-1)
//           glass[o-1].children[6].children[0].classList.remove('not-visible')
//        console.log(data)
//
//        setTimeout(()=>{
//               glass[o-1].children[6].children[0].classList.add('not-visible')
//
//            data.map((p,i) =>{
//            let x = new Date ((data[i].fields.date))
//
//        glass[o-1].children[5].innerHTML += `
//        <div class="comment">
//
//        <div class="user-info">
//            <img src= ${ response.urls[i]}>
//<div class="sub-info">
//            <p class="username">
//               ${ response.commenters[i]}
//            </p>
//            <p class="date">
//               ${(x.toUTCString().split(" ").slice(0,4).join(" "))}
//
//
//            </p>
//    </div>
//        </div>
//        <p>
//${data[i].fields.comment}
//
//    </p>
//        </div>`
//        })
//
//        if(response.max){
//               glass[o-1].children[6].children[1].innerHTML = `<div class="loaded">No more comments to load</div>`
//
//            console.log('DONE')
//        }
//        }, 500)
//
//    },
//    error: {
//    function(error){
//        console.log(error)
//    }}
////})$.ajax({
////
////    type: "GET",
////    url: `/posts-json/${visible}/${n}`,
////    success: function(response){
////        console.log(response)
////        max_size = response.max
////
////        const data=JSON.parse(response.data)
////        console.log(data)
////            console.log(o-1)
////           glass[o-1].children[6].children[0].classList.remove('not-visible')
////        console.log(data)
////
////        setTimeout(()=>{
////               glass[o-1].children[6].children[0].classList.add('not-visible')
////
////            data.map((p,i) =>{
////            let x = new Date ((data[i].fields.date))
////
////        glass[o-1].children[5].innerHTML += `
////        <div class="comment">
////
////        <div class="user-info">
////            <img src= ${ response.urls[i]}>
////<div class="sub-info">
////            <p class="username">
////               ${ response.commenters[i]}
////            </p>
////            <p class="date">
////               ${(x.toUTCString().split(" ").slice(0,4).join(" "))}
////
////
////            </p>
////    </div>
////        </div>
////        <p>
////${data[i].fields.comment}
////
////    </p>
////        </div>`
////        })
////
////        if(response.max){
////               glass[o-1].children[6].children[1].innerHTML = `<div class="loaded">No more comments to load</div>`
////
////            console.log('DONE')
////        }
////        }, 500)
////
////    },
////    error: {
////    function(error){
////        console.log(error)
////    }}
////})
//}
//for(var i=1;i<=nop;i++){
//    o = i
//    handleGetData(i,o)
//}
//loadBtn.addEventListener('click', getData)
//
//function getData(e){
//    visible +=1
//    console.log("-------x-----------",e.target.name)
//    handleGetData(e.target.name, e.target.name)
//
//}


window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.querySelector(".navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}