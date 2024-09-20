import request from '@/common/request/request.js'

export function searchDestiny(name) {
  return request.get('/app/babyname/status',{ params: { param: name }})
}

export function createName(xing, male, source) {
  return request.get('/app/babyname/names',{ params: {param: xing,gender: male,source: source }})
}

