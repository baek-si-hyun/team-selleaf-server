const alarmService = (()=> {

    const alarmList = async (page, callback) => {
        const response = await fetch(`/alarm/show/main/${page}`);
        const alarms = await response.json();
        if (callback) {
            return callback(alarms)
        };
        return alarms

    };

    return {alarmList:alarmList}
})()