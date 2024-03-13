// 강의 리뷰 목록을 화면에 띄우는 함수
const showTrainees = (trainees_info) => {
    // HTML 코드를 담기 위한 빈 문자열
    let text = ``;

    // 받아온 데이터들 중 'trainees' 만 따로 가져옴
    const trainees = trainees_info.trainees;

    // 받아온 리뷰 정보로 화면에 뿌릴 HTML 태그 생성
    trainees.forEach((trainee) => {
        text += `
                  <li class="list-content">
                    <input type="checkbox" class="checkbox-input" />
                    <div class="trainee-info-wrap">
                      <div class="trainee-info title">
                          <p class="trainee-title">${trainee.trainee_title}</p>
                          <p class="trainee-content">${trainee.trainee_content}</p>
                      </div>
                      <div class="trainee-info">${trainee.member_name}</div>
                      <div class="trainee-info">${trainee.trainee_rating}</div>
                      <div class="trainee-info">${trainee.created_date}</div>
                    </div>
                  </li>
        `;
    });

    // 완성된 HTML 코드 반환
    return text;
}