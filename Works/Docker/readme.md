# Docker

## Docker file nədir?

* Docker Image build etmək üçün commandları yazdığımız yerdir. Dockerfile'da yazdığımız image əgər docker daemonda varsa oradan, yoxdursa, docker hub'dan götürülür.

## Docker Image nədir?

* Dockerfile'ın build olunmuş formasıdır. Container yaratmaq üçün run edirik.

## Docker Container nədir?

* Docker Container OS'i əvəz edən bir mühit yaradır. Bunun sayəsində fərqli operation system'lərdə çalışan developerlər eyni mühitdə işləyə bilirlər. Bunun ən böyük faydası daha sürətli sistem olmağıdır.

## Virtual maşın nədir?

* Bir əməliyyat sistemində işləyərkən, digər bir əməliyyat sistemini istifadə etmək üçün yüklədiyimiz proqramdır. Bu proqram defoult əməliyyat sisteminin içərisində digər əməliyyat sistemi üçün yaddaş və ram ayırmağa imkan yaradır.

## Virtual maşın, Docker və virtual environement arasında fərqlər nələrdir?

* Virtual maşın bizə virtualda əməliyyat sistemi yaratmağa, docker isə işlədiyimiz proyektin fərqli əməliyyat sistemlərində kompüterimizə əlavə os yükləmədən işləməsinə kömək edir. Bunların virtual enviroment'dən fərqi isə hər ikisi kompüterimizə yüklənir lakin, venv isə yalnız proyekt daxilində yüklənir və istifadə etdiyimiz package'lər üçün yer ayırır.