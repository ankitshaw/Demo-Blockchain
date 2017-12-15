from blockchain_block import Block
import datetime as date

def genesis_block():
	return Block(0, date.datetime.now(), "Genesis Block", "0")