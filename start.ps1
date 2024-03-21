$env:CLIENT_SECRET=''
$env:CLIENT_ID = ''
$env:ACCESS_TOKEN = ''
$env:API_KEY = ''
$env:REPO_URL = 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}'
$env:USER_URL = 'https://api.github.com/search/users?q={query}{&page}'
$env:BASE_URL = 'https://api.github.com/JKKimani77/grupe-project?access_token='

$env:MAIL_USERNAME=''
$env:MAIL_PASSWORD=''


python manage.py server
