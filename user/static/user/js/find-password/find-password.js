// 이메일 입력창 테두리
const emailWrap = document.querySelector(".email-input-wrap");

// 입력칸 + 버튼
const emailContainer = document.querySelector(".email-input-container");

// 이메일 입력칸
const emailInput = document.querySelector(".email-input-area");

// 확인 버튼
const emailButton = document.querySelector(".email-input-button");

// 인증코드 받기 버튼
const verifyButton = document.querySelector(".verify-button");

// 회원 조회 성공 시 버튼에 들어갈 텍스트
const complete = "확인완료";

// 입력창 아래에 에러 메세지를 표시하는 div 태그
const errorTextArea = document.querySelector(".not-verified");

// 입력 에러 텍스트
const valueNone = "필수 입력 항목입니다.";
const notRegistered = "등록된 이메일 주소가 아닙니다.";

// 올바른 이메일 (임시)
const testEmail = "test@test.com";

// 이메일 검증 함수
const emailVerification = (e) => {
  // 만약 input 창에 value가 없다면
  if (!e.target.value) {
    // 테두리 색깔 변경
    if (!emailWrap.classList.contains("error")) {
      emailWrap.classList.add("error");
    }

    // 에러 메세지 표시
    errorTextArea.innerText = valueNone;
    errorTextArea.style.display = "block";

    // 이메일 버튼 기능 정지
    emailButton.disabled = true;
    return;
  }
  // 만약 어떤 값이라도 있다면
  // 테두리 색상 원복
  emailWrap.classList.remove("error");

  // 이메일 버튼 활성화
  emailButton.disabled = false;

  // 에러 메세지 숨김
  errorTextArea.style.display = "none";
};

// 이메일 입력창에서 keyup 또는 blur 발생 시, 위 함수 실행
emailInput.addEventListener("keyup", emailVerification);
emailInput.addEventListener("blur", emailVerification);

// email-input-button 클릭 이벤트
emailButton.addEventListener("click", (e) => {
  // 만약 input에 입력한 값이 DB에 있다면
  if (emailInput.value === testEmail) {
    // 아래쪽 인증 버튼 활성화
    verifyButton.disabled = false;

    // "확인" 버튼 안 글자를 "확인완료" 로 변경
    e.target.innerText = "확인완료";

    // input과 확인 버튼 부분 비활성화
    // wrap, input 부분 배경색 변경
    emailWrap.style.background = "rgb(247, 248, 250)";
    emailInput.style.webkitBoxShadow = "0 0 0 30px rgb(247, 248, 250) inset";
    e.target.disabled = true;
    emailInput.disabled = true;

    return;
  }
  // 만약 DB 조회에 실패했다면 확인 버튼 비활성화
  e.target.disabled = true;

  // 테두리 색상 변경
  if (!emailWrap.classList.contains("error")) {
    emailWrap.classList.add("error");
  }

  // 에러 메세지 표시
  errorTextArea.innerText = notRegistered;
  errorTextArea.style.display = "block";

  return;
});

/*
  이메일 인증번호

  제한시간 3분
  3분 지나면 자동으로 버튼 disabled + 입력값 있어도 disabled 유지
  
  재발급받으면 3분 타이머 초기화, 입력하면 disabled 해제됨


  인증 완료 시, 이메일 인증버튼 내 텍스트가 "이메일 인증완료" 로 변경
  이메일 입력창 비활성화
*/

// 인증번호 입력칸 전체
const emailCodeWrap = document.querySelector(".email-code-wrap");

// 인증번호 입력창, 입력창을 감싸는 테두리
const codeInput = document.querySelector(".code-input");
const codeWrap = document.querySelector(".code-input-wrap");

// 타이머 표시할 span 태그
let leftTime = document.querySelector(".left-time");

// 비밀번호 재설정하기 버튼
const confirmButton = document.querySelector(".confirm-button");

// 에러 텍스트를 표시할 div 태그
const errorArea = document.querySelector(".error-text");

// 이메일 재전송 버튼(a 태그)
const resend = document.querySelector(".resend");

// 상황별 에러 텍스트
const invalidMsg = "올바른 인증 번호가 아닙니다.";
const timeoverMsg = "유효시간이 지났어요. '이메일 재전송하기'를 눌러주세요.";

// 올바른 인증번호(임시)
const correctCode = "123456";

// 이메일 인증 버튼 - click 이벤트(활성화 상태일 때만)
verifyButton.addEventListener("click", () => {
  // 활성화 상태인지 검사
  if (!verifyButton.disabled) {
    // 인증버튼 비활성화
    verifyButton.disabled = true;

    // 인증번호 입력칸 표시
    emailCodeWrap.style.height = "222px";
    emailCodeWrap.style.marginBottom = "20px";

    // 인증 타이머 시작
    validationTimer();
  }
});

/*
  타이머 이벤트
  
  인증 버튼 or 재발급 버튼 눌렀을 때 작동할 3분 타이머
*/
// 아래에서 setInterval 기능을 할당할 변수 - 선언
let timerInterval;

// 타이머 함수
function validationTimer() {
  // 타이머 작동시, 기존에 작동중이던 타이머 종료
  clearInterval(timerInterval);

  // 에러 메세지 삭제 및 테두리 색상 원복
  codeWrap.classList.remove("error");
  errorArea.style.display = "none";

  // 인증번호 입력칸에 keyup 이벤트 부여
  codeInput.addEventListener("keyup", inputKeyupEvent);

  // 현재 입력창 안에 입력값이 있다면 버튼 활성화
  document.querySelector(".code-input").value
    ? (confirmButton.disabled = false)
    : false;

  // 타이머의 초기 설정 시간(초)
  // 버튼 누르고 1초 뒤에 실행되므로, 타이머 초기 시간은 2분 59초로 설정
  let time = 179;

  // 남은 분, 초를 담을 변수를 빈 문자열로 선언
  let min = "";
  let sec = "";

  // setInterval 기능을 변수에 할당 - 새로운 타이머 실행
  // clearInterval로 이전에 작동 중이던 타이머를 초기화하기 위함
  timerInterval = setInterval(() => {
    /*
      남은 시간 표시

      분 - 남은 시간(초) / 60
      초 - 남은 시간 / 60 하고 남은 나머지(0~59)

      공통 - 숫자 값이 10 미만이면 앞에 "0"을 붙여줌
    */
    min = parseInt(time / 60);
    min = min < 10 ? "0" + min : min;

    sec = time % 60;
    sec = sec < 10 ? "0" + sec : sec;

    // 남은 시간을 표시하는 span 태그 안에 "분:초" 형식으로 표기
    leftTime.innerText = min + ":" + sec;

    // 남은 시간 - 1초
    --time;

    // 만약 시간이 다 되었다면
    if (time < 0) {
      // 타이머 기능 종료
      clearInterval(timerInterval);

      // 입력창 keyup 이벤트 삭제
      // 유효 시간이 지났으면, 값을 입력해도 확인 버튼이 비활성화 상태로 유지되도록 하기 위함
      codeInput.removeEventListener("keyup", inputKeyupEvent);

      // 인증번호 입력란 테두리 빨간색으로
      if (!codeWrap.classList.contains("error")) {
        codeWrap.classList.add("error");
      }

      // 인증번호 확인 버튼 비활성화
      confirmButton.disabled = true;

      // 에러 텍스트 표시
      errorArea.innerText = timeoverMsg;
      errorArea.style.display = "block";
    }
  }, 1000);
}

// 인증번호 입력창 - keyup 이벤트에 사용할 함수
const inputKeyupEvent = (e) => {
  // 입력창이 눌릴 때마다, 값이 있는지 검사
  if (e.target.value) {
    // 값이 있을 때 실행
    // 테두리 색상 원복
    codeWrap.classList.remove("error");

    // 에러 텍스트 숨김
    errorArea.style.display = "none";

    // 버튼 disabled 해제
    confirmButton.disabled = false;
    return;
  }
  // 값이 없으면 버튼 disabled
  confirmButton.disabled = true;
};

// 확인 버튼 - click 이벤트
confirmButton.addEventListener("click", () => {
  // 클릭 시점에서 인증번호랑 입력값 비교
  if (codeInput.value === correctCode) {
    // 타이머 종료
    clearInterval(timerInterval);

    // 이메일 입력창 숨김
    emailCodeWrap.style.height = 0;
    emailCodeWrap.style.marginBottom = 0;

    return;
  }
  // 불일치 시, 테두리 색상 빨간색으로
  if (!codeWrap.classList.contains("error")) {
    codeWrap.classList.add("error");
  }

  // 에러 텍스트 지정 및 표시
  errorArea.innerText = invalidMsg;
  errorArea.style.display = "block";
});

// 재전송 버튼 - click 이벤트
resend.addEventListener("click", (e) => {
  // a 태그의 링크 이동 기능 방지
  e.preventDefault();

  // 여기서 타이머 리셋 - 함수 사용
  validationTimer();
});
