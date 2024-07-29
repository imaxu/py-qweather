const crypto = require('crypto')

let privateKey = 'xxxx';
let parameters = {
  lang: 'zh-hans',
  unit: 'm'
};
parameters['location'] = '101010100';
parameters['publicid'] = 'xxxx';
parameters['t'] = '1722043603';
// 接口必要的参数
parameters['required'] = " ";

function md5(something) {

  return crypto.createHash('md5').update(something).digest("hex")
}

function getSignature(parameterObject, privateKey) {
    var keys = [];
    for (let k in parameterObject) {
        if (k !== 'key' && k !== 'sign' && !/^\s+$/.test(k) && !/^\s+$/.test(parameterObject[k])) {
            keys.push(k);
        }
    }

    keys.sort();

    let str = '';
    for (let i in keys) {
        let k = keys[i];
        if (!/\s+/.test(parameterObject[k])) {
            str += k + '=' + parameterObject[k] + '&';
        }
    }
    str = str.substr(0, str.length - 1) + privateKey;
    console.log(str)
    return md5(str);
}


console.log(getSignature(parameters, privateKey));
