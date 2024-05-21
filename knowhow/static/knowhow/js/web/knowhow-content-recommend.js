// 전역 변수 선언
const recommendList = document.querySelector('ul.ai-recommended-list');
const recommendButton = document.querySelector('.content-recommendation');

// li 태그 클릭 이벤트 - 클릭한 내용 textarea에 innerText로 삽입
const addListClickEvent = () => {
    const lists = document.querySelectorAll('.recommended-contents-wrap');

    // 각 리스트에 클릭 이벤트 추가
    lists.forEach((list) => {
        list.addEventListener('click', ()  => {
            // 아래 함수로 추가한 리스트의 번호를 가져옴
            const listNum = list.classList[1];

            // 디버깅
            console.log(listNum);
        });
    });
}

// li 태그 (추천받은 내용) 생성 모듈
const createRecommendedList = (() => {
    const showList = async (knowhows) => {
        // HTML 코드를 담을 빈 문자열
        let text = ``;

        // 리스트 번호 - 1 ~ 5번
        listNum = 0;

        // 각 노하우의 내용이 담긴 li 태그 추가
        for (let knowhow of knowhows) {
            text += `
                <li class="recommended-contents-wrap ${++listNum}">
                  <div class="recommended-contents-container">
                    <div class="recommended-contents-inner">
                      <div class="recommended-content-num">
                        추천 내용 ${listNum}
                      </div>
                      <div class="ai-recommended-content">
                        ${knowhow.knowhow_content}
                      </div>
                    </div>
                  </div>
                </li>
            `
        }
        // ul 태그 안에 리스트 표시
        recommendList.innerHTML = text;

        // 리스트 클릭 이벤트 추가
        addListClickEvent();
    }

    return {showList: showList}
})();

// 제목 작성 후 버튼 클릭했을 때 발생하는 이벤트
const recommendButtonClickEvent = () => {
    // 제목 입력 태그에서 현재 입력된 텍스트 가져오기
    const titleInput = document.querySelector('input.title-input');
    const title = titleInput.value;

    // 입력값이 있을 때만 입력한 텍스트로 모듈로 fetch 요청해서 ul 태그 안에 리스트 뿌리기
    if (title) {
        console.log('AI 추천 이벤트 발생!')
        recommendService.getRecommends(title, createRecommendedList.showList);
    }
}

// AI 내용 추천 버튼 클릭 시 위 이벤트 발동
recommendButton.addEventListener('click', recommendButtonClickEvent);