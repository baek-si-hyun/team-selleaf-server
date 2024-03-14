// 다른 파일에서 postService.메소드명 형식으로 사용할 수 있도록 모듈화
const postService = (() => {
    // 전체 게시물 목록 조회 - 한 번에 10개씩
    const getEntireList = async (page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/posts/${page}`);
        const posts = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(posts);
        }

        // 콜백함수를 받지 않았다면 데이터만 반한
        return posts;
    }

    // 커뮤니티 게시물 목록 조회 - 한 번에 10개씩
    const getCommunityList = async (page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/posts/${page}`);
        const posts = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(posts);
        }

        // 콜백함수를 받지 않았다면 데이터만 반한
        return posts;
    }

    // 노하우 게시물 목록 조회 - 한 번에 10개씩
    const getKnowhowList = async (page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/posts/${page}`);
        const posts = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(posts);
        }

        // 콜백함수를 받지 않았다면 데이터만 반한
        return posts;
    }

    // 거래 게시물 목록 조회 - 한 번에 10개씩
    const getTradeList = async (page, callback) => {
        // API에 데이터 요청
        const response = await fetch (`/admin/posts/${page}`);
        const posts = await response.json();

        // 콜백함수를 인자로 받았다면 콜백함수에 처리를 넘김
        if (callback) {
            return callback(posts);
        }

        // 콜백함수를 받지 않았다면 데이터만 반한
        return posts;
    }

    // 모듈 반환
    return {
        getEntireList: getEntireList,
        getCommunityList: getCommunityList,
        getKnowhowList: getKnowhowList,
        getTradeList: getTradeList
    }
})();