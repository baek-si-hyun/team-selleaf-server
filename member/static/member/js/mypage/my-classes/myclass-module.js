const classService = (()=> {

    const classList = async (page, callback) => {
        const response = await fetch(`/member/mypage/show/teachers/${page}`);
        const applies = await response.json();
        if (callback) {
            return callback(applies)
        };
        return applies

    };

    const traineeList = async (applyID,page) =>{
        const response = await fetch(`member/mypage/teachers/show/apply/${applyID}/${page}`);
        const trainees = await response.json();
        if(callback){
            return callback(trainees)
        };
        return trainees
    }

    return {classList:classList, traineeList:traineeList}
})()