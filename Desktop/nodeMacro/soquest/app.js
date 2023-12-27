const Web3 = require('web3');


// Polygon 네트워크에 연결
const web3 = new Web3('https://polygon-mainnet.g.alchemy.com/v2/40NSN2OM3ynZLiG5cwMgpBmIyEsI0iZx'); // 이 주소는 Polygon RPC 주소로, 필요에 따라 변경하세요.

// 컨트랙트 ABI와 주소
const contractABI = [{"inputs":[{"internalType":"address","name":"logic","type":"address"},{"internalType":"address","name":"admin","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"admin_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"implementation_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}];

const contractAddress = '0x7B36dFD5304562952E2B4DE9C8048ED155c6115d'; // 컨트랙트 주소를 여기에 입력하세요.

// 컨트랙트 인스턴스 생성
const contract = new web3.eth.Contract(contractABI, contractAddress);

// 함수 호출
const amount = '0x106505e1a19c0dff8'; // 호출할 때 사용할 amount 값

contract.methods.swapEth(amount).send({ from: '0xAEf30fEcf1792Eed810F5fab03c0eB584E83FB91' }) // 지갑 주소를 여기에 입력하세요.
  .then(function(receipt){
      console.log(receipt);
  });
