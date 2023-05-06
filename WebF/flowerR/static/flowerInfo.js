const searchParams = new URLSearchParams(window.location.search);
const flowerID = searchParams.get("flowerID");
const updateFlowerInfoAPI = `http://127.0.0.1:5000/getAFlower/${flowerID}`

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

const backButton = document.getElementById('backButton');

backButton.addEventListener('click', (event) =>{
    window.history.back()
})

function resetForm() {
    if (flowerID) {
        const updateFlowerAPI = `http://127.0.0.1:5000/getAFlower/${flowerID}`
        fetch(updateFlowerAPI, { method: 'GET' })
            .then(Response => Response.json())
            .then(Response => {
                if (Response.flowerTen) flowerTenInput.innerHTML = Response.flowerTen;
                else flowerTenInput.innerHTML = "Không có";
                if (Response.flowerTenKH) flowerTenKHInput.innerHTML = Response.flowerTenKH;
                else flowerTenKHInput.innerHTML = "Không có";
                if (Response.flowerLop) flowerLopInput.innerHTML = Response.flowerLop;
                else flowerLopInput.innerHTML = "Không có";
                if (Response.flowerGioi) flowerGioiInput.innerHTML = Response.flowerGioi;
                else flowerGioiInput.innerHTML = "Không có";
                if (Response.flowerBo) flowerBoInput.innerHTML = Response.flowerBo;
                else flowerBoInput.innerHTML = "Không có";
                if (Response.flowerHo) flowerHoInput.innerHTML = Response.flowerHo;
                else flowerHoInput.innerHTML = "Không có";
                if (Response.flowerNganh) flowerNganhInput.innerHTML = Response.flowerNganh;
                else flowerNganhInput.innerHTML = "Không có";
                if (Response.flowerMota) flowerMotaInput.innerHTML = Response.flowerMota;
                else flowerMotaInput.innerHTML = "Không có";
                if (Response.flowerDacdiem) flowerDacdiemInput.innerHTML = Response.flowerDacdiem;
                else flowerDacdiemInput.innerHTML = "Không có";
                if (Response.flowerNoipb) flowerNoipbInput.innerHTML = Response.flowerNoipb;
                else flowerNoipbInput.innerHTML = "Không có";
            })
    }
}

resetForm()