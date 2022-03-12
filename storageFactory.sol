//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;
import "./crud.sol";

contract StorageFactory {

	Storage[] public storageArray;

	function createStorageContract() public {
		Storage simpleStorage = new Storage();
		storageArray.push(simpleStorage);


	}

	function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
		Storage simpleStorage = Storage(address(storageArray[_simpleStorageIndex]));
		simpleStorage.store(_simpleStorageNumber);

	}

	function sfGet(uint256 _simpleStorageIndex) public view returns(uint256){
		Storage simpleStorage = Storage(address(storageArray[_simpleStorageIndex]));
		return simpleStorage.retrive();
	}
}




