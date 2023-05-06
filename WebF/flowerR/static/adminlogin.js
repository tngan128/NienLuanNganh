const adminLoginaApi = 'http://127.0.0.1:5000/api/admin/login'

const form = document.getElementById('adminLoginForm');
const adminUNInput = document.getElementById('adminUN');
const adminPwInput = document.getElementById('adminPw');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = {
        'adminUN': adminUNInput.value,
        'adminPw': adminPwInput.value
    };

    fetch(adminLoginaApi, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(res =>{
        if (res.ok)
            window.location = '/admin';
        else return res.json();
    })
    .then(res => {
        Swal.fire({
            title: 'Đăng nhập thất bại!',
            text: `Lỗi: ${res.message}`,
            icon: 'error',
            iconColor: '#AC2626'}
        )
    })
    .catch(error => {
        Swal.fire({
            title: 'Thất bại!',
            text: `Dữ liệu của ${flowerTenInput.value} chưa được thêm vào cơ sở dữ liệu`,
            icon: 'error',
            iconColor: '#AC2626'}
        )
    })
});