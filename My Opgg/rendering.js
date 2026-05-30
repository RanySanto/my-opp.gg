fetch("./player_match_history.json")
  .then((res) => res.json())
  .then((data) => {
    renderData(data)
  });

function renderData(data){
    console.log(data)
    function createElements(){
        for(i=0;i<data.length;i++){
            
        }
    }
}