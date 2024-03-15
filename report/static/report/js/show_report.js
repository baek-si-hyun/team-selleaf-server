// 신고 내역을 화면에 띄우는 함수
const showReports = (reports_info) => {
    // HTML 코드를 담기 위한 빈 문자열
    let text = ``;

    // 받아온 데이터들 중 'reports' 만 따로 가져옴
    const reports = reports_info.reports;

    // 받아온 신고 내역으로 화면에 뿌릴 HTML 태그 생성
    reports.forEach((report) => {
        const reportStatus = report.report_status ? "게시 중" : "삭제됨";

        text += `
                  <li class="list-content ${report.id}">
                    <input type="checkbox" class="checkbox-input" />
                    <div class="report-info-wrap">
                      <div class="report-info">${report.report_target}</div>
                      <div class="report-info">${report.report_content}</div>
                      <div class="report-info">${report.report_member}</div>
                      <div class="report-info">${reportStatus}</div>
                      <div class="report-info">${report.created_date}</div>
                    </div>
                  </li>
        `;
    });

    // 완성된 HTML 코드 반환
    return text;
}
