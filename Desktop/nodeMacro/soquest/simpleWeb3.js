import Web3 from 'web3';
import dotenv from 'dotenv';

dotenv.config();

const { ADDRESS,PRIVATE_KEY, INFURA_API_KEY } = process.env;
// Web3 인스턴스를 생성하고 이더리움 노드에 연결합니다.

const networkURI = 'https://polygon-mainnet.infura.io/v3/';
const web3 = new Web3(networkURI+INFURA_API_KEY);

// 트랜잭션을 전송하는 함수
async function sendTransaction(fromAddress,toAddress, amountInEther, data, privateKey) {
    // 이더리움 단위를 Wei로 변환
    const amountInWei = web3.utils.toWei(amountInEther, 'ether');
    const nonce = await web3.eth.getTransactionCount(fromAddress);
    const maxPriorityFeePerGas = web3.utils.toWei('40', 'gwei'); // 예시 값
    const maxFeePerGas = web3.utils.toWei('200', 'gwei');

    const transaction = {
        from: fromAddress,
        to: toAddress,
        value: amountInWei,
        gas: 200000,
        maxFeePerGas: maxFeePerGas,
        maxPriorityFeePerGas:maxPriorityFeePerGas,
        nonce: nonce,  // 적절한 nonce 값으로 설정
        data: data,    // 필요한 데이터가 있으면 여기에 추가
        chainId: 137  // Polygon 네트워크의 Chain ID
    };
    
    // 가스 추정
    const estimatedGas = await web3.eth.estimateGas(transaction);

    
    // 이제 'gas' 필드에 추정된 가스 값을 설정
    transaction.gas = estimatedGas;
    
    // 거래에 서명
    const signedTransaction = await web3.eth.accounts.signTransaction(transaction, privateKey);

    // 서명된 트랜잭션 전송
    const receipt = await web3.eth.sendSignedTransaction(signedTransaction.rawTransaction);

    return receipt;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


for(var i=0; i<20;i++ ){
    
    // W-MATIC TO MATIC
    await sendTransaction(
        ADDRESS,
        '0x7B36dFD5304562952E2B4DE9C8048ED155c6115d', 
        '0', 
        '0x98cf9d5100000000000000000000000000000000000000000000000106505e1a19c0dff8',
        PRIVATE_KEY)
        .then(receipt => console.log('Transaction successful: W-MATIC TO MATIC '+i))
        .catch(error => {
            console.error('Error sending transaction:', error);
            throw Error(error);

    });


    await sleep(2000);
    
    
    // MATIC TO W-MATIC
    await sendTransaction(
        ADDRESS,
        '0x7B36dFD5304562952E2B4DE9C8048ED155c6115d', 
        '19.996020692399520915', 
        '0x98cf9d51000000000000000000000000000000000000000000000001141eb3e5945f4018',
        PRIVATE_KEY)
        .then(receipt => console.log('Transaction successful: MATIC TO W-MATIC '+i))
        .catch(error => {
            console.error('Error sending transaction:', error);
            throw Error(error);
    })
}