# Create project files for Djinn Express landing page
index_html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Джин Express – Фулфилмент для маркетплейсов</title>
    <meta name="description" content="Фулфилмент-услуги для селлеров маркетплейсов: приёмка, хранение, упаковка и отгрузка товаров.">
    <meta name="keywords" content="фулфилмент, Джин Express, складская логистика, FBS, FBO, упаковка для маркетплейсов, логистика для селлеров">
    <link rel="preload" href="assets/hero-bg.jpg" as="image">
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <header class="header" id="top">
        <div class="container header__content">
            <a class="logo" href="#top">
                <img src="assets/logo.png" alt="Логотип Джин Express" class="logo__img">
                <span class="logo__text">Джин Express</span>
            </a>
            <nav class="nav" id="nav">
                <ul class="nav__list">
                    <li><a href="#services">Услуги</a></li>
                    <li><a href="#benefits">Преимущества</a></li>
                    <li><a href="#prices">Цены</a></li>
                    <li><a href="#contact">Контакты</a></li>
                </ul>
            </nav>
            <button class="burger" id="burger" aria-label="Открыть меню"><span></span><span></span><span></span></button>
        </div>
    </header>

    <section class="hero">
        <div class="hero__overlay">
            <div class="container hero__content">
                <h1>Ваш экспертный фулфилмент<br>для маркетплейсов</h1>
                <p>Приёмка, хранение, упаковка и отгрузка товаров — всё в одном месте.</p>
                <a href="#contact" class="btn-primary">Получить расчёт</a>
            </div>
        </div>
    </section>

    <!-- Секции услуг, преимуществ, цен и контактов можно добавлять по мере заполнения контентом -->

    <footer class="footer">
        <div class="container footer__content">
            <small>© 2025 ООО «Джин». Все права защищены.</small>
            <a href="privacy.html">Политика конфиденциальности</a>
        </div>
    </footer>
</body>
</html>
'''

styles_css = '''/* === CSS-переменные для быстрой настройки === */
:root {
    --primary: #0c5ff5;
    --accent:  #ff6f3d;
    --bg:      #ffffff;
    --text:    #1a1a1a;
    --header-h: 72px;
    font-size: 16px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', Arial, sans-serif;
    color: var(--text);
    background: var(--bg);
    scroll-behavior: smooth;
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }

/* === Header & Logo === */
.header { position: fixed; top: 0; left: 0; width: 100%; height: var(--header-h); background: rgba(255,255,255,0.95); box-shadow: 0 2px 4px rgba(0,0,0,0.08); z-index: 100; }
.header__content { display: flex; align-items: center; justify-content: space-between; height: 100%; }

.logo { display: flex; align-items: center; gap: .5rem; text-decoration: none; color: var(--primary); font-weight: 700; font-size: 2.2rem; }
@media (max-width: 768px) { .logo { font-size: 1.8rem; } }
@media (max-width: 480px) { .logo { font-size: 1.5rem; } }
.logo__img { width: 48px; height: auto; }

/* === Navigation === */
.nav__list { display: flex; gap: 2rem; list-style: none; }
.nav a { text-decoration: none; color: var(--text); font-weight: 500; transition: color .3s; }
.nav a:hover { color: var(--primary); }

/* Burger menu */
.burger { display: none; flex-direction: column; justify-content: center; gap: 4px; background: none; border: none; width: 24px; height: 24px; cursor: pointer; }
.burger span { display: block; width: 100%; height: 3px; background: var(--text); transition: .3s; }
@media (max-width: 768px) {
    .nav { display: none; }
    .burger { display: flex; }
    .nav.open { display: block; position: absolute; top: var(--header-h); right: 1rem; background: var(--bg); padding: 1rem 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .nav__list { flex-direction: column; gap: 1rem; }
}

/* === Hero Section === */
.hero { height: 100vh; background: url('assets/hero-bg.jpg') center/cover no-repeat; position: relative; }
.hero__overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.4), rgba(0,0,0,0.6)); display: flex; align-items: center; color: #fff; }
.hero__content { text-align: left; }
.hero h1 { font-size: 3rem; margin-bottom: 1rem; line-height: 1.2; }
.hero p { font-size: 1.125rem; margin-bottom: 2rem; max-width: 480px; }
@media (max-width: 480px) { .hero h1 { font-size: 2rem; } }

/* === Buttons === */
.btn-primary { display: inline-block; background: var(--accent); color: #fff; padding: 1rem 2rem; border-radius: .25rem; text-decoration: none; font-weight: 600; transition: background .3s; }
.btn-primary:hover { background: #ff824f; }

/* === Footer === */
.footer { background: var(--bg); padding: 2rem 0; text-align: center; border-top: 1px solid #e5e5e5; margin-top: 4rem; }
.footer a { color: var(--primary); text-decoration: none; }
.footer a:hover { text-decoration: underline; }
'''

script_js = '''// == Бургер-меню ==
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
'''

# Write files
after_write = {}
for filename, content in {
    'index.html': index_html,
    'styles.css': styles_css,
    'script.js': script_js
}.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    after_write[filename] = len(content)

after_write