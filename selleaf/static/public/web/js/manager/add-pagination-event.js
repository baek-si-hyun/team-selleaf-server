// 페이지네이션 버튼 클릭 시 발생하는 이벤트 추가하는 함수 - 페이지네이션 dict 데이터 가져와서 키로 접근
// 관리자 페이지 내 모든 페이지네이션에 대해서 공통으로 사용하기 때문에 내부 변수명 바꿀 필요 없음
const addPaginationEvent = (pageInfo) => {
    // 앞으로 가기, 뒤로 가기 버튼, 숫자 페이지 버튼, 페이지 수 표시되는 span 태그
    const pageCountPrev = document.querySelector(".page-count-prev");
    const pageCountNext = document.querySelector(".page-count-next");
    const pageCountNumBtns = document.querySelectorAll("button.page-count-num");
    const pageCountNumSpans = document.querySelectorAll("span.page-count-num");

    // 현재 페이지(받아온 dict 데이터의 page)가 1보다 클 때
    if (pageInfo.page > 1) {
        // 뒤로 가기 버튼 클릭 이벤트 추가 - 이전 페이지의 데이터 요청(키워드는 그대로 유지)
        pageCountPrev.addEventListener("click", async () => {
            // 이렇게 await 요청 보낸 곳은 현재 눌린 버튼에 따라 다른 리스트 요청하게 if문 분기 만들기
            await manageReply.getReply(keyword, --page, createHTML.showList);
        });
    }

    // 현재 페이지가 맨 끝 페이지가 아닐 때
    if (pageInfo.page !== pageInfo.realEnd){
        // 앞으로 가기 버튼 누르면 다음 페이지 데이터 요청
        pageCountNext.addEventListener("click", async () => {
            await manageReply.getReply(keyword, ++page, createHTML.showList);
        });
    }

    // 페이지 숫자 버튼 각각에 클릭 이벤트 추가
    pageCountNumBtns.forEach((btn, i) => {
        // 버튼 클릭 시 해당 버튼 안 숫자를 가져와서 page에 할당 -> 해당 페이지의 데이터 요청
        btn.addEventListener("click", async () => {
            page = pageCountNumSpans[i].innerText;
            await manageReply.getReply(keyword, page, createHTML.showList);
        });
    });
}