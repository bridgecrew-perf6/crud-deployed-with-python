//SPDX-License-Identifier :MIT

pragma solidity ^0.8.0;

contract Storage {
	uint256 favoriteNumber;
	bool favoriteBool;

	struct People {
		uint256 favoriteNumber;
		string name;
	}
	

	People[] public people;
	
	//searching 
	mapping( string => uint256) public nameToFavoriteNumber;

	//store
	function store(uint256 _favoriteNumber) public{

		favoriteNumber = _favoriteNumber;
	}

	//get 
	function retrive() public view  returns(uint256){
		return favoriteNumber;

	}

	//add to array
	function addPeople(uint256 _favoriteNumber, string memory _name) public {
		people.push(People(_favoriteNumber, _name));
	}



}
