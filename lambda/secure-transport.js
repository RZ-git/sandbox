// Lambda@Edgeを使った「HTTPセキュリティヘッダー」の付与
exports.handler = async (event, context) => {
    const response = event.Records[0].cf.response;
    const headers = response.headers;

    const headerNameSrc = 'X-Amz-Meta-Last-Modified';
    const headerNameDst = 'Last-Modified';

    if (headers[headerNameSrc.toLowerCase()]) {
        headers[headerNameDst.toLowerCase()] = [{
            key: headerNameDst,
            value: headers[headerNameSrc.toLowerCase()][0].value,
        }];
        console.log(`Response header "${headerNameDst}" was set to ` +
            `"${headers[headerNameDst.toLowerCase()][0].value}"`);
    }

    return response;
};

exports.handler = (event, context, callback) => {

    const response = event.Records[0].cf.response;
    const headers = response.headers;

    // ヘッダー付与
    headers['strict-transport-security'] = [{
        key: 'Strict-Transport-Security',
        value: 'max-age= 63072000; includeSubdomains; preload'
    }];
    headers['content-security-policy'] = [{
        key: 'Content-Security-Policy',
        value: "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'"
    }];
    headers['x-content-type-options'] = [{key: 'X-Content-Type-Options', value: 'nosniff'}];
    headers['x-frame-options'] = [{key: 'X-Frame-Options', value: 'DENY'}];
    headers['x-xss-protection'] = [{key: 'X-XSS-Protection', value: '1; mode=block'}];
    headers['referrer-policy'] = [{key: 'Referrer-Policy', value: 'same-origin'}];

    // セキュリティヘッダー付与済みのレスポンスを返す
    callback(null, response);
};
