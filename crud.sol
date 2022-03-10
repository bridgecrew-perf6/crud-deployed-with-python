//SPDX License-Identifier :MIT

pragma solidity ^0.8.0;

contract Storage {
	uint favoriteNumber;
	bool favoriteBool;
	string name;

	struct people {
		uint256 public favoriteNumber;
		string name;
	}
	

	People [] public people;
	
	//searching 
	mapping( string => uint) public nameToFavoriteNumber;

	//store
	function store(uint _favoriteNumber) public view{

		favoriteNumber = _favoriteNumber;
	}

	//get 
	function retrive() public {
		return favoriteName;

	}

	//add to array
	function addPeople (uint256 favoriteNumber, string memory _name) public {
		people.push(People(_favoriteNumber, _name));
 		nameToFavoriteNumber[_name] =_favoriteNumber;

		
	}
}



