
#1.  static 파일 기본 설정
STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]

#2.  media 파일 기본 설정
MEDIA_ROOT = BASE_DIR / 'uploaded_files'
MEDIA_URL = 'uploaded_files/'
