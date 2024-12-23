export function setupEventListeners() {
    const wrapper = document.querySelector('.wrapper');
    const loginLink = document.querySelector('.login-link');
    const registerLink = document.querySelector('.register-link');
    const btnPopupLog = document.querySelector('.btnLogin-popup');
    const btnPopupReg = document.querySelector('.btnRegister-popup');

    registerLink.addEventListener('click', () => {
        wrapper.classList.add('active');
    });

    loginLink.addEventListener('click', () => {
        wrapper.classList.remove('active');
    });

    btnPopupLog.addEventListener('click', () => {
        if(wrapper.classList.contains('active')){
            wrapper.classList.remove('active')
        } else{
            wrapper.classList.add('active-popup');
        }
    });

    btnPopupReg.addEventListener('click', () => {
        wrapper.classList.add('active-popup', 'active');
    });
}




