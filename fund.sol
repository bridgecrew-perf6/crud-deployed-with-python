//SPDX-License-Identifier : MIT
pragma solidity ^0.8.0;
import '@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol';

contract FundMe {

	mapping(address => uint256) public addressToAmountFunded;

	function fund() public payable{
		addressToAmountFunded[msg.sender] += msg.value;
		
	}

	function getVersion()public view returns(uint256) {
		AggregatorV3Interface priceFeed = AggregatorV3Interface();
		return priceFeed.version();	
	}

	function getPrice() public view returns(uint256) {
		AggregatorV3Interface priceFeed = AggregatorV3Interface();
		(,int256 answer,,,) = priceFeed.latestRoundData();
		return uint256(answer * 100000000);

	}
	
	function getConversionRate(uint256 ethAmount) public view returns(uint256) {
		uint256 getPrice = getPrice();
		uint256 amountInUsd = (getPrice * ethAmount)/ 1000000000000000000;
		

		return amountInUsd;
	} 
}

