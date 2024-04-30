const filter = document.getElementById("searchMovie");
const items = document.querySelectorAll("a div");

filter.addEventListener("input", (s) => searchData(s.target.value));

function searchData(search){
    items.forEach((item) => {
        if(item.innerText.toLowerCase().includes(search.toLowerCase())){
            item.classList.remove("d-none");
        }else{
            item.classList.add("d-none");
        }
    });
}