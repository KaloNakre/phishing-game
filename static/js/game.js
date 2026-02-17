function sendAnswer(ans){

fetch("/answer",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({name:player,answer:ans})
})
.then(r=>r.json())
.then(data=>{

if(data.finished){
window.location="/result/"+player
return
}

alert(data.correct ? "✔ Correct" : "✖ Wrong")

document.getElementById("url").innerText=data.next
document.getElementById("q").innerText=data.q

})
}
