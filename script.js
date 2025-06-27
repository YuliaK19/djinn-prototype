// == Бургер-меню ==
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
if (burger) {
  burger.addEventListener('click', () => {
    nav.classList.toggle('open');
  });
}

// == Пример отправки формы ==
function sendForm(event, formId) {
  event.preventDefault();
  const form = document.getElementById(formId);
  const data = new FormData(form);
  fetch(form.action, { method: 'POST', body: data })
    .then(() => {
      alert('Спасибо! Мы свяжемся с вами.');
      form.reset();
    })
    .catch(() => alert('Ошибка отправки. Попробуйте позже.'));
}

// == Плейс-холдеры аналитики ==
// -- Яндекс.Метрика --
// (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
// m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1;k.src=r;a.parentNode.insertBefore(k,a)})
// (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
// ym(YOUR_METRIKA_ID, "init", { clickmap:true, trackLinks:true, accurateTrackBounce:true });

// -- Google Analytics --
// window.dataLayer = window.dataLayer || [];
// function gtag(){dataLayer.push(arguments);} gtag('js', new Date());
// gtag('config', 'GA_MEASUREMENT_ID');
