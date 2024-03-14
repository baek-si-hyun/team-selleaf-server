let page = 1

const showAlarm = (alarms) => {
  let text = ``
  alarms.forEach((alarm) => {
      text += `
        <div>    
          <div class="notice-contents">
            <a href="" class="notice-profile-box">
              <img src="{% static 'public/web/images/common/blank-image.png' %}" alt="" class="notice-profile" />
            </a>
            <a href="" class="notice-content-box">
              <div class="inner-txt-wrap">
                <span class="inner-txt">
                  <strong>${alarm.sender}</strong>
                    ${alarm.message}                  
                </span>
                <span class="last-time">${timeForToday(alarm.updated_date)}</span>
              </div>
              <img src="{% static 'public/web/images/common/blank-image.png' %}" alt="" class="notice-img" />
            </a>
          </div>
        <div>`


  });
  return text;
}

const target = document.querySelector('.here')

alarmService.alarmList(page++,showAlarm).then((text)=>{
  target.innerHTML += text
})

window.addEventListener("scroll", () => {
    // 맨위
    const scrollTop = document.documentElement.scrollTop;
    // 페이지 높이
    const windowHeight = window.innerHeight;
    // 암튼 높이
    const totalHeight = document.documentElement.scrollHeight;
    // 전체 높이에서 내가 보는 스크롤이 total보다 크면 추가

    if (scrollTop + windowHeight >= totalHeight) {

    alarmService.alarmList(page++,showAlarm()).then((text)=>{
      target.innerHTML += text
    })


    }
});


function timeForToday(datetime) {
    const today = new Date();
    const date = new Date(datetime);

    let gap = Math.floor((today.getTime() - date.getTime()) / 1000 / 60);

    if (gap < 1) {
        return "방금 전";
    }

    if (gap < 60) {
        return `${gap}분 전`;
    }

    gap = Math.floor(gap / 60);

    if (gap < 24) {
        return `${gap}시간 전`;
    }

    gap = Math.floor(gap / 24);

    if (gap < 31) {
        return `${gap}일 전`;
    }

    gap = Math.floor(gap / 31);

    if (gap < 12) {
        return `${gap}개월 전`;
    }

    gap = Math.floor(gap / 12);

    return `${gap}년 전`;


}