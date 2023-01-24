var list = document.querySelector('.list');
var menus = list.querySelectorAll('.li_name');
for (let i = 0; i < menus.length; i++) {
    menus[i].addEventListener('click', function() {
        alinks = this.nextElementSibling.children;
        if (this.className == 'li_name') {
            this.className = 'li_name current';
            for (let k = 0; k < alinks.length; k++) {
                alinks[k].style.height = '38px';
            }
        } else {
            this.className = 'li_name';
            for (let k = 0; k < alinks.length; k++) {
                alinks[k].style.height = '0';
            }
        }
    })
}

document.querySelector('#tklb').addEventListener('click', function () {
    document.querySelector('.content').src="addProblem.html";
})

document.querySelector('#tjtm').addEventListener('click', function () {
    document.querySelector('.content').src="addProblemBank.html";
})

document.querySelector('#kslb').addEventListener('click', function () {
    document.querySelector('.content').src="examList.html";
})


