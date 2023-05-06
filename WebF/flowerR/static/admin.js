const getFlowerInfoAPI = "http://127.0.0.1:5000/getAllFlowers"

flowers = []

fetch(getFlowerInfoAPI, {method: 'GET'})
    .then(response => response.json())
    .then(function (result) {
        for (var i = 0; i < result.length; i++) {
            flowers.push(result[i])
        }
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
                <div class="admin-option">
                    <div class="btn btn-more" onclick="watchFlower(${flower.flowerID})">
                        <div class="inner"></div>
                        <button>Xem thêm</button>
                    </div>
                    <div class="btn btn-modify" onclick="updateFlower(${flower.flowerID})">
                        <div class="inner"></div>
                        <button>Chỉnh sửa</button>
                    </div>
                    <div class="btn btn-cancel" onclick="deleteFlower(${flower.flowerID})">
                        <div class="inner"></div>
                        <button>Xóa</button>
                    </div>
                </div>

            </div>
            `
        })
        servicebottom.innerHTML = htmls.join('');
    })
    .catch(error => console.log('error', error));

const addButton = document.getElementById('addButton');
addButton.addEventListener('click', (event) => {
    window.location = "/flowers/add"
});

function watchFlower(flowerID){
    window.location = `/flowers/info?flowerID=${flowerID}`
}

function updateFlower(flowerID){
    console.log("Update")
    Swal.fire({
        title: 'Bạn chắc chứ?',
        text: "Bạn có chắc chắn để chỉnh sửa các thông tin của hoa này không?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#497980',
        cancelButtonColor: '#AC2626',
        confirmButtonText: 'chắc chắn',
        cancelButtonText: 'Hủy bỏ',
    }) .then((result) => {
        if (result.isConfirmed) {
            window.location = `/flowers/update?flowerID=${flowerID}`;
        }
    });
}

function deleteFlower(flowerID) {
    Swal.fire({
        title: 'Bạn chắc chứ?',
        text: "Bạn có chắc chắn để xóa tất cả thông tin của hoa này không?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#497980',
        cancelButtonColor: '#AC2626',
        confirmButtonText: 'chắc chắn',
        cancelButtonText: 'Hủy bỏ',
    }).then((result) => {
        if (result.isConfirmed) {
            const deleteFlowerAPI = `http://127.0.0.1:5000/deleteAFlower/${flowerID}`
            fetch(deleteFlowerAPI, { method: 'DELETE' })
                .then(response => {
                    if (response.ok) {
                        Swal.fire({
                            title: 'Thành công!',
                            text: `Thông tin đã được xóa khỏi cơ sở dữ liệu`,
                            icon: 'success',
                            iconColor: '#2B884E'
                        }
                        ).then(() => {
                            location.reload()
                        });
                    } else {
                        Swal.fire({
                            title: 'Thất bại!',
                            text: `Thông tin chưa được xóa khỏi cơ sở dữ liệu`,
                            icon: 'error',
                            iconColor: '#AC2626'}
                        )
                    }
                })
                .catch(error => {
                    Swal.fire({
                        title: 'Thất bại!',
                        text: `Thông tin chưa được xóa khỏi cơ sở dữ liệu`,
                        icon: 'error',
                        iconColor: '#AC2626'}
                    )
                })
        }
    })
}