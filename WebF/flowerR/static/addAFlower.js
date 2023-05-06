const addFlowerAPI = "http://127.0.0.1:5000/postAFlower"

const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
    tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
    tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
    this.style.height = 0;
    this.style.height = (this.scrollHeight) + "px";
    var pr = this.parentNode.getElementsByTagName('label');
    pr[0].style.setProperty('transform', `translateY(-${this.scrollHeight - 15}px)`);
}

const form = document.getElementById('flower-form');
const flowerTenInput = document.getElementById('flowerTen');
const flowerTenKHInput = document.getElementById('flowerTenKH');
const flowerGioiInput = document.getElementById('flowerGioi');
const flowerBoInput = document.getElementById('flowerBo');
const flowerHoInput = document.getElementById('flowerHo');
const flowerNganhInput = document.getElementById('flowerNganh');
const flowerLopInput = document.getElementById('flowerLop');
const flowerMotaInput = document.getElementById('flowerMota');
const flowerDacdiemInput = document.getElementById('flowerDacdiem');
const flowerNoipbInput = document.getElementById('flowerNoipb');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    Swal.fire({
        title: 'Bạn chắc chứ?',
        text: `Bạn có chắc chắn muốn thêm thông tin cho ${flowerTenInput.value}?`,
        icon: 'question',
        iconColor: '#463B3F',
        showCancelButton: true,
        confirmButtonColor: '#2B884E',
        cancelButtonColor: '#AC2626',
        confirmButtonText: 'Chắc chắn',
        cancelButtonText: 'Hủy bỏ',
    }).then((result) => {
        if (result.isConfirmed) {
            const formData = {
                'flowerTen': flowerTenInput.value,
                'flowerTenKH': flowerTenKHInput.value,
                'flowerGioi': flowerGioiInput.value,
                'flowerBo': flowerBoInput.value,
                'flowerHo': flowerHoInput.value,
                'flowerNganh': flowerNganhInput.value,
                'flowerLop': flowerLopInput.value,
                'flowerMota': flowerMotaInput.value,
                'flowerDacdiem': flowerDacdiemInput.value,
                'flowerNoipb': flowerNoipbInput.value,
            };

            fetch(addFlowerAPI, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Thêm hoa thành công:', data);
                    Swal.fire({
                        title: 'Thành công!',
                        text: `Dữ liệu của ${flowerTenInput.value} đã được thêm vào cơ sở dữ liệu`,
                        icon: 'success',
                        iconColor: '#2B884E'}
                    ).then(() => {
                        window.location = "/admin"
                    });
                })
                .catch(error => {
                    Swal.fire({
                        title: 'Thất bại!',
                        text: `Dữ liệu của ${flowerTenInput.value} chưa được thêm vào cơ sở dữ liệu`,
                        icon: 'error',
                        iconColor: '#AC2626'}
                    )
                });
        }
    })
});