from blockchain_block import Block
import datetime as date

def new_block(last_block):
	my_index = last_block.index + 1
	my_timestamp = date.datetime.now()
	my_data = "Block No." + str(my_index)
	previous_hash = last_block.hash

	return Block(my_index, my_timestamp, my_data, previous_hash)