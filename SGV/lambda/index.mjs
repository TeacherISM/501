export async function handler() {
    const response = {
        statusCode: 200,
        body: JSON.stringify(22+22),
    };
    return response;
}
