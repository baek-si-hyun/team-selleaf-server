const reportService = (() => {
    // 강의 신고 내역 조회
    const getLectureReports = async (keyword, page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/report/lecture/?keyword=${keyword}&page=${page}`);
        const lectureReports = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(lectureReports);
        }

        // 콜백함수를 받지 않았다면 데이터만 반환
        return lectureReports;
    }

    // 거래 신고 내역 조회
    const getTradeReports = async (keyword, page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/report/trade/?keyword=${keyword}&page=${page}`);
        const tradeReports = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(tradeReports);
        }

        // 콜백함수를 받지 않았다면 데이터만 반환
        return tradeReports;
    }

    // 일반 게시물 신고 내역 조회
    const getPostReports = async (keyword, page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/report/post/?keyword=${keyword}&page=${page}`);
        const postReports = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(postReports);
        }

        // 콜백함수를 받지 않았다면 데이터만 반환
        return postReports;
    }

    // 일반 게시물 댓글 신고 내역 조회
    const getPostReplyReports = async (keyword, page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/report/post-reply/?keyword=${keyword}&page=${page}`);
        const postReplyReports = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(postReplyReports);
        }

        // 콜백함수를 받지 않았다면 데이터만 반환
        return postReplyReports;
    }

    // 노하우 게시물 신고 내역 조회
    const getKnowhowReports = async (keyword, page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/report/knowhow/?keyword=${keyword}&page=${page}`);
        const knowhowReports = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(knowhowReports);
        }

        // 콜백함수를 받지 않았다면 데이터만 반환
        return knowhowReports;
    }

    // 노하우 게시물 댓글 신고 내역 조회
    const getKnowhowReplyReports = async (keyword, page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/report/knowhow-reply/?keyword=${keyword}&page=${page}`);
        const knowhowReplyReports = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(knowhowReplyReports);
        }

        // 콜백함수를 받지 않았다면 데이터만 반환
        return knowhowReplyReports;
    }

    // 모듈 반환
    return {
        getLectureReports: getLectureReports,
        getTradeReports: getTradeReports,
        getPostReports: getPostReports,
        getPostReplyReports: getPostReplyReports,
        getKnowhowReports: getKnowhowReports,
        getKnowhowReplyReports: getKnowhowReplyReports
    }
})();