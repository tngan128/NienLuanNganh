const getFlowerInfoAPI = "http://127.0.0.1:5000/getAllFlowers"

flowers = []
fetch(getFlowerInfoAPI)
    .then(response => response.json())
    .then(function (result) {
        for (var i = 0; i < result.length; i++) {
            flowers.push(result[i])
        }
        console.log(flowers)
        var servicebottom = document.querySelector('.service-bottom')
        var htmls = flowers.map((flower) => {
            return `
            <div class="service-item">
                <h2>${flower.flowerTen}</h2>
                <p>Tên khoa học: ${flower.flowerTenKH}</p>
                <p>Giới: ${flower.flowerGioi}</p>
                <p>Nghành: ${flower.flowerNganh}</p>
                <p>Lớp: ${flower.flowerLop}</p>
                <p>Bộ: ${flower.flowerBo}</p>
                <p>Họ: ${flower.flowerHo}</p>
                <a href="/flowers/info?flowerID=${flower.flowerID}" class = 'cta'>Xem thêm</a>
            </div>
            `
        })
        servicebottom.innerHTML = htmls.join('');
    })
    .catch(error => console.log('error', error));