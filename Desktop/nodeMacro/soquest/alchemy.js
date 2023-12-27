import { Network, Alchemy, Wallet, Utils } from "alchemy-sdk";
import dotenv from "dotenv";
dotenv.config();

const { API_KEY, PRIVATE_KEY } = process.env;

const settings = {
  apiKey: API_KEY,
  network: Network.MATIC_MAINNET, // Replace with your network.
};

const alchemy = new Alchemy(settings);
const wallet = new Wallet(PRIVATE_KEY);



async function transactionFactory(to, value, data){

    const transaction = {
        to: to,
        value: value,
        gasLimit: "200000",
        maxPriorityFeePerGas: Utils.parseUnits("100", "gwei"),
        maxFeePerGas: Utils.parseUnits("500", "gwei"),
        nonce: 481,
        type: 2,
        data: data,
        chainId: 137, // Corresponds to 
      };
    return transaction;
}

const rawTransaction = await wallet.signTransaction(
    await transactionFactory(
        "0x7B36dFD5304562952E2B4DE9C8048ED155c6115d",
        Utils.parseEther("0"),
        "0x98cf9d51000000000000000000000000000000000000000000000001141eb3e5945f4018")
    );
await alchemy.transact.sendTransaction(rawTransaction);


/*
0x98cf9d5100000000000000000000000000000000000000000000000106505e1a19c0dff8

Function: swapEth(uint256 amount)

MethodID: 0x98cf9d51
[0]:  00000000000000000000000000000000000000000000000106505e1a19c0dff8

*/