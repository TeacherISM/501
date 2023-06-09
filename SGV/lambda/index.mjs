export async function handler(event) {
    const response = {
        statusCode: 200,
        body: JSON.stringify(22+22),
    };
    return response;
}
