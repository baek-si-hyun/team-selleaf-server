const days = document.querySelectorAll(".weekday-selection");
const timeSection = document.querySelector(".product-option-second-wrap");
const inputTarget = document.querySelector(".selected-product-name");
const sidebarInputTarget = document.querySelector(
  ".sidebar-selected-product-option"
);

days.forEach((day) => {
  day.addEventListener("click", (e) => {
    // 모든 요일에서 clicked 클래스를 제거
    days.forEach((otherday) => {
      otherday.classList.remove("clicked");
    });
    // 클릭된 요일에만 clicked 클래스 추가
    day.classList.add("clicked");
    const selectedDay = day.querySelector("span").textContent;
    var inner = inputTarget.querySelector(".selected-date");
    var sidebarInner = sidebarInputTarget.querySelector(".selected-date");
    inner.innerHTML = `${selectedDay}`;
    sidebarInner.innerHTML = `${selectedDay}`;
    // 시간 섹션을 보이거나 숨김
    if (day.classList.contains("clicked")) {
      timeSection.style.display = "block";
    } else {
      timeSection.style.display = "none";
    }
  });
});

// 시간 선택 시 색 변하게
const times = document.querySelectorAll(".time-selection");
const check = document.querySelector(".selected-product-list-container");
const sidebarselectBox = document.querySelector(
  ".sidebar-selected-product-wrap"
);
times.forEach((time) => {
  time.addEventListener("click", (e) => {
    // 모든 시간 요소에서 clicked 클래스를 제거
    times.forEach((othertime) => {
      othertime.classList.remove("clicked");
    });

    // 클릭된 시간에만 clicked 클래스 추가
    time.classList.add("clicked");
    const selectedTime = time.querySelector("span").textContent;
    var inner = inputTarget.querySelector(".selected-time");
    var sidebarInner = sidebarInputTarget.querySelector(".selected-time");
    inner.innerHTML = `${selectedTime}`;
    sidebarInner.innerHTML = `${selectedTime}`;
    // 체크 요소를 보이거나 숨김
    if (time.classList.contains("clicked")) {
      check.style.display = "block";
      sidebarselectBox.style.display = "block";
    } else {
      check.style.display = "none";
      sidebarselectBox.style.display = "none";
    }
  });
});