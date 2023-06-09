import { handler } from './index';
import { describe, expect, it } from '@jest/globals';

describe('handler', () => {
  it('should return a response with status code 200 and performing a sum of 22 + 22', async () => {
    const event = {}; // Add your event payload here if needed
    const expectedResponse = {
      statusCode: 200,
      body: JSON.stringify(44),
    };

    const response = await handler(event);

    expect(response).toEqual(expectedResponse);
  });
});
