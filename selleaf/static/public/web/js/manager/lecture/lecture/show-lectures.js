// 개설된 강의 목록을 화면에 띄우는 함수
const showLecture = (lectures_info) => {
    // HTML 코드를 담기 위한 빈 문자열
    let text = ``;

    // 받아온 데이터들 중 'lectures' 만 따로 가져옴
    const lectures = lectures_info.lectures;

    // 받아온 회원 정보로 화면에 뿌릴 HTML 태그 생성
    lectures.forEach((lecture) => {
        text += `
                  <li class="list-content ${lecture.id}">
                    <input type="checkbox" class="checkbox-input" />
                    <a class="class-info-wrap">
                      <div class="class-info title">
                          <p class="content-name">${lecture.lecture_title}</p>
                          <p class="content-name-detail">${lecture.lecture_title}</p>
                      </div>
                      <div class="class-info">${lecture.teacher_name}</div>
                      <div class="class-info">${lecture.lecture_headcount}명</div>
                      <div class="class-info">${lecture.lecture_price}원</div>
                      <div class="class-info">${lecture.lecture_place}</div>
                      <div class="class-info">${lecture.created_date}</div>
                    </a>
                  </li>
        `;
    });

    // 완성된 HTML 코드 반환
    return text;
}