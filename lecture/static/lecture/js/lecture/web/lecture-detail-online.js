// 필요한 DOM 요소들을 가져옴
const days = document.querySelectorAll(".weekday-selection"); // 요일 선택 요소들
const timeSection = document.querySelector(".product-option-second-wrap"); // 시간 선택 섹션
const kitSection = document.querySelector(".product-option-third-wrap"); // 키트 선택 섹션
const inputTarget = document.querySelector(".selected-product-name"); // 선택된 정보를 표시할 곳
const sidebarInputTarget = document.querySelector(".sidebar-selected-product-option"); // 사이드바에 선택된 정보를 표시할 곳

// 날짜 선택 시 동작
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
    // if (day.classList.contains("clicked")) {
    //   timeSection.style.display = "block";
    //   kitSection.style.display = "none"; // 시간 선택 시에는 키트 선택 섹션을 숨김 ***********8
    // } else {
    //   timeSection.style.display = "none";
    // }
  });
});

// 시간 선택 시 동작
const times = document.querySelectorAll(".time-selection"); // 시간 선택 요소들
const check = document.querySelector(".selected-product-list-container"); // 체크 요소
const sidebarselectBox = document.querySelector(".sidebar-selected-product-wrap"); // 사이드바에 선택된 정보를 표시할 요소

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
    // if (time.classList.contains("clicked")) {
    //   console.log("dasdasda")
    //   check.style.display = "block";
    //   sidebarselectBox.style.display = "block";
    //   kitSection.style.display = "block"; // 시간 선택 시에는 키트 선택 섹션을 보이게 함
    // } else {
    //   check.style.display = "none";
    //   sidebarselectBox.style.display = "none";
    // }
  });
});

// 키트 선택 시 동작
const kits = document.querySelectorAll(".kit-selection"); // 키트 선택 요소들
const infoContainer = document.querySelector(".selected-product-list-container"); // 선택된 정보를 표시할 컨테이너

kits.forEach((kit) => {
  kit.addEventListener("click", (e) => {
    // 모든 키트 요소에서 clicked 클래스를 제거
    kits.forEach((otherkit) => {
      otherkit.classList.remove("clicked");
    });

    // 클릭된 키트에만 clicked 클래스 추가
    kit.classList.add("clicked");
    const selectedKit = kit.querySelector(".kit-title").textContent;
    var inner = inputTarget.querySelector(".selected-kit");
    var sidebarInner = sidebarInputTarget.querySelector(".selected-kit");
    inner.innerHTML = `${selectedKit}`;
    sidebarInner.innerHTML = `${selectedKit}`;

    // 정보 컨테이너를 보이거나 숨김
    if (kit.classList.contains("clicked")) {
      infoContainer.style.display = "block";
    } else {
      infoContainer.style.display = "none";
    }
  });
});
