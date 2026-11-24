# SigmaBall for Powerball — 공식 웹사이트 & 개인정보처리방침 & app-ads.txt

Google Play Console 조직 계정 웹사이트 인증, 앱 심사, Google AdMob 수익화 승인을 위한 공식 영문 소개 페이지 및 필수 인증 정적 파일 패키지입니다.

---

## 📁 디렉터리 및 파일 구조

```text
├── index.html                      # 메인 소개페이지 (URL: /)
├── privacy/
│   ├── sigmaball/
│   │   └── index.html              # 영문 개인정보처리방침 (URL: /privacy/sigmaball/ 또는 /privacy/sigmaball)
│   └── sigmaball.html              # 영문 개인정보처리방침 단일 파일 (URL: /privacy/sigmaball fallback)
├── app-ads.txt                     # AdMob 개발자 인증 파일 (URL: /app-ads.txt)
├── public/
│   └── app-ads.txt                 # 빌드 도구 / 정적 호스팅(Vercel, Vite 등) 루트 배포용 복사본
├── assets/
│   ├── css/
│   │   └── style.css               # 다크 네이비(#0B1120) 통계 유틸리티 반응형 디자인
│   └── images/
│       ├── sigmaball-logo.png      # 공식 앱 로고
│       └── favicon.svg             # 브라우저 탭 아이콘 (SVG)
├── scripts/
│   └── verify.py                   # 빌드 무결성, 필수 면책조항, 파일 검증 스크립트
├── package.json                    # 프로젝트 메타데이터 및 빌드/테스트 스크립트
└── README.md                       # 교체 가이드 및 배포 안내 문서
```

---

## ⚡ 1분 완료: 실제 값 교체 가이드 (PLACEHOLDER)

코드 에디터(VS Code 등)에서 **전체 파일 검색 (`Ctrl + Shift + F`)**으로 아래 4개 키워드를 찾아 실제 값으로 교체하세요:

| 검색 키워드 | 교체할 내용 | 예시 |
|:---|:---|:---|
| `YOUR_ENGLISH_BUSINESS_NAME` | 홈택스 영문 사업자등록증명에 기재된 영문 상호 | `Sigma Studio LLC` 또는 `Hong Gil Dong` |
| `YOUR_CONTACT_EMAIL` | 스토어 개발자 연락처 및 개인정보 문의용 공식 이메일 | `support@sigmaball.app` 또는 `contact@yourdomain.com` |
| `YOUR_SITE_URL` | 배포할 웹사이트 도메인 주소 (끝에 슬래시 제외) | `https://sigmaball.app` |
| `YOUR_ADMOB_APP_ADS_TXT_LINE` | Google AdMob 콘솔의 `app-ads.txt` 탭에서 복사한 1줄 | `google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0` |

### 1) AdMob `app-ads.txt` 복사 방법
1. [Google AdMob 콘솔](https://apps.admob.com) 접속 &rarr; 좌측 메뉴 **앱(Apps)** &rarr; **app-ads.txt** 클릭.
2. 상단에 표시되는 코드 스니펫(예: `google.com, pub-XXXX, DIRECT, f08c47fec0942fa0`)을 복사.
3. 프로젝트 루트의 `app-ads.txt` 및 `public/app-ads.txt` 파일 내 `YOUR_ADMOB_APP_ADS_TXT_LINE` 부분을 지우고 붙여넣기.

---

## 🌐 연결 URL 및 경로 매핑

배포 후 웹 브라우저에서 아래 3개 주소로 정상 접근되는지 확인하세요:

1. **메인 소개페이지**: `https://<도메인>/`
   - 앱 명칭(`SigmaBall for Powerball`), 패키지명(`com.sigmaball.app`)
   - 5대 핵심 기능 요약 (통계 분석, 필터/프리셋, 흔들기, 백테스팅, 다국어 지원)
   - 공공데이터(`data.ny.gov`) 출처 및 비공식 도구 면책 문구 (과장 광고·당첨 보장 문구 배제)
2. **영문 개인정보처리방침**: `https://<도메인>/privacy/sigmaball`
   - 기기 로컬 데이터 저장(Zero-Cloud), Google AdMob SDK 데이터 수집 안내
   - COPPA 아동 보호, 사용자 데이터 삭제 권리, 문의 이메일 안내
3. **AdMob 개발자 인증 파일**: `https://<도메인>/app-ads.txt`
   - AdMob 크롤러가 직접 읽을 수 있는 평문 텍스트(`text/plain`) 제공

---

## 🚀 추천 배포 방법

순수 정적(HTML/CSS) 구조이므로 별도의 복잡한 백엔드 서버 없이 무료 호스팅 서비스에 1분 만에 배포할 수 있습니다:

### 옵션 A. GitHub Pages
1. 저장소(GitHub Repo)를 생성하고 본 폴더의 파일들을 커밋/푸시합니다.
2. 저장소의 `Settings` &rarr; `Pages` &rarr; `Branch: main`, `Folder: / (root)` 선택 후 저장.
3. 제공되는 도메인 또는 맞춤 도메인(Custom Domain)을 연결합니다.

### 옵션 B. Cloudflare Pages / Vercel / Netlify
1. 대시보드에서 `New Project` 클릭 후 저장소를 연동하거나 폴더를 직접 드래그 앤 드롭합니다.
2. 빌드 설정(Build command)은 비워두거나 `python scripts/verify.py` 입력, 출력 디렉터리는 `.` (루트)로 설정합니다.

---

## 🛡️ 빌드 및 무결성 검증

로컬 환경에서 다음 명령어로 모든 필수 파일, 면책 조항, 링크 연결 상태를 검증할 수 있습니다:

```bash
python scripts/verify.py
```
*(검증 결과: 0 Errors, 0 Warnings)*
