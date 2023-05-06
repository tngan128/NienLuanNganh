const logoutLink = document.getElementById('logout');

const logoutAPI = 'http://127.0.0.1:5000/api/admin/logout'

logoutLink.addEventListener('click', logOut)

function logOut(evevt) {
    evevt.preventDefault()
    Swal.fire({
        title: 'Bạn chắc chứ?',
        text: `Phiên quản trị của bạn sẽ kết thúc ngay lập tức`,
        icon: 'question',
        iconColor: '#463B3F',
        showCancelButton: true,
        confirmButtonColor: '#2B884E',
        cancelButtonColor: '#AC2626',
        confirmButtonText: 'Chắc chắn',
        cancelButtonText: 'Hủy bỏ',
    })
        .then((result) => {
            if (result.isConfirmed) {
                fetch(logoutAPI, {
                    method: 'POST',
                    credentials: 'same-origin'
                })
                window.location = '/'
            }
        });
}