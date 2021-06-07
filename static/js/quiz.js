const choices = document.getElementsByClassName('answer-input');
const url = window.location.href.slice(0, window.location.href.lastIndexOf('/'));

window.onload = prepareData;


function prepareData(){

    retrievedAnswer = localStorage[choices[0].name];
    if(typeof(retrievedAnswer) != 'undefined'){

        answer = JSON.parse(retrievedAnswer);

        for(var i = 0; i < answer.length; i++){
            {
                for(var j = 0; j < choices.length; j++){
                    if(choices[j].value == answer[i]){
                        choices[j].checked = true
                    }
                    
                }
            
            }
        }
    }
    
    submit = document.querySelector('.submit_btn');
    submit.addEventListener("click", sendAnswers);
}


const sendAnswers = (e) => {
    e.preventDefault();
    this.storeAnswers();
    const csrf = document.getElementsByName('csrfmiddlewaretoken')

    const answers = {}
    answers['csrfmiddlewaretoken'] = csrf[0].value
    for(var i = 0; i < localStorage.length; i++){

        ans = JSON.parse(localStorage.getItem(localStorage.key(i)))
        answers[localStorage.key(i)] = ans
    }
    answers['url'] = url.slice(url.lastIndexOf('/') + 1)
    $.ajax({
    type: 'POST',
    url:`${url}/result/`,
    dataType: "html",
    data: answers,
    success: function(response){
        window.history.pushState('','', `${url}/result/`)
        container  = document.querySelector('.container')
        container.innerHTML = response
        localStorage.clear()
        },
    error: function(error){
        console.log(error)
        }

    });
    

}


function storeAnswers(){

    var answers = [];
    for(var i = 0; i < choices.length; i++){
        if(choices[i].checked){
            answers.push(choices[i].value);
        }
    }
    localStorage.setItem(choices[0].name, JSON.stringify(answers));

}

window.addEventListener('unload', storeAnswers);
