global.fetch = jest.fn();
global.fetch.mockResolvedValue({ json: () => Promise.resolve({}) });