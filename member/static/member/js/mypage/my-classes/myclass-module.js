const classService = (()=> {

    const classList = async (page, callback) => {
        const response = await fetch(`/member/mypage/show/teachers/${page}`);
        const applies = await response.json();
        if (callback) {
            return callback(applies)
        };
        return applies

    };

    return {classList:classList}
})()